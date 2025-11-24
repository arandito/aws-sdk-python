"""
Generate API documentation for AWS SDK Python clients.

This script generates MkDocs Material documentation that matches the reference
documentation format. It analyzes Python client packages using griffe
and creates structured documentation with proper formatting.
"""

import logging
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

import griffe
import mkdocs_gen_files
from griffe import Alias, Class, Function, Module, Object, ExprBinOp, ExprSubscript, TypeAlias


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(name)s - %(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("generate_doc_stubs")

EVENT_STREAM_TYPES = ["InputEventStream", "OutputEventStream", "DuplexEventStream"]

class StreamType(Enum):
    """Type of event stream for operations."""

    NONE = "none"
    INPUT = "InputEventStream"  # Client-to-server streaming
    OUTPUT = "OutputEventStream"  # Server-to-client streaming
    DUPLEX = "DuplexEventStream"  # Bidirectional streaming

 
@dataclass(frozen=True)
class StructureInfo:
    """Information about a structure (dataclass)."""

    name: str
    module_path: str  # e.g., "aws_sdk_bedrock_runtime.models"


@dataclass
class UnionInfo:
    """Information about a union type."""

    name: str
    module_path: str
    members: list[StructureInfo]


@dataclass
class EnumInfo:
    """Information about an enum."""

    name: str
    module_path: str


@dataclass
class ErrorInfo:
    """Information about an error/exception."""

    name: str
    module_path: str


@dataclass
class ConfigInfo:
    """Information about a configuration class."""

    name: str
    module_path: str


@dataclass
class PluginInfo:
    """Information about a plugin type alias."""

    name: str
    module_path: str


@dataclass
class OperationInfo:
    """Information about a client operation."""

    name: str  # e.g., "converse"
    module_path: str # e.g., "aws_sdk_bedrock_runtime.client.BedrockRuntimeClient.converse"
    input: StructureInfo # e.g., "ConverseInput"
    output: StructureInfo # e.g., "ConverseOperationOutput"
    stream_type: StreamType.NONE
    event_input_type: str | None # For input/duplex streams
    event_output_type: str | None # For output/duplex streams


@dataclass
class ModelsInfo:
    """Information about all models."""

    structures: list[StructureInfo]
    unions: list[UnionInfo]
    enums: list[EnumInfo]
    errors: list[ErrorInfo]


@dataclass
class ClientInfo:
    """Complete information about a client package."""

    name: str  # e.g., "BedrockRuntimeClient"
    module_path: str # e.g., "aws_sdk_bedrock_runtime.client.BedrockRuntimeClient"
    package_name: str  # e.g., "aws_sdk_bedrock_runtime"
    config: ConfigInfo
    plugin: PluginInfo
    operations: list[OperationInfo]
    models: ModelsInfo


Member = Object | Alias

class DocStubGenerator:
    """Generates MkDocs stubs for AWS SDK client documentation."""

    def __init__(self, client_dir: Path, docs_dir: Path, service_name: str) -> None:
        """Initialize the documentation generator."""
        self.client_dir = client_dir
        self.service_name = service_name

    def generate(self) -> None:
        """Generate the documentation stubs to the output directory."""
        client_name = self.client_dir.name
        package_name = client_name.replace("-", "_")
        client_info = self._analyze_client_package(package_name)
        self._generate_client_docs(client_info)

    def _analyze_client_package(self, package_name: str) -> ClientInfo:
        """Analyze a client package using griffe."""
        logger.info(f"Analyzing package: {package_name}")
        package = griffe.load(package_name)

        # Parse submodules
        client_module = package.modules.get("client")
        config_module = package.modules.get("config")
        models_module = package.modules.get("models")

        client_class = self._find_class_with_suffix(client_module, "Client")       
        config_class = config_module.members.get("Config")
        plugin_alias = config_module.members.get("Plugin")
        config = ConfigInfo(
            name=config_class.name,
            module_path=config_class.path
        )
        plugin = PluginInfo(
            name=plugin_alias.name,
            module_path=plugin_alias.path
        )
        operations = self._extract_operations(client_class)
        models = self._extract_models(models_module, operations)

        return ClientInfo(
            name=client_class.name,
            module_path=client_class.path,
            package_name=package_name,
            config=config,
            plugin=plugin,
            operations=operations,
            models=models
        )

    def _find_class_with_suffix(self, module: Module, suffix: str) -> Class:
        """Find the class in the module with a matching suffix."""
        for cls in module.classes.values():
            if cls.name.endswith(suffix):
                return cls

    def _extract_operations(self, client_class: Class) -> list[OperationInfo]:
        """Extract operation information from client class."""
        operations = []
        for op in client_class.functions.values():
            if op.is_private or op.is_init_method:
                continue
            operations.append(self._analyze_operation(op))
        return operations

    def _analyze_operation(self, operation: Function) -> None:
        """Analyze an operation method to extract information."""
        stream_type = None
        event_input_type = None
        event_output_type = None

        input_param = operation.parameters["input"]
        input_info = StructureInfo(
            name=input_param.annotation.canonical_name,
            module_path=input_param.annotation.canonical_path
        )

        output_type = operation.returns.canonical_name
        if any(type in output_type for type in EVENT_STREAM_TYPES):
            stream_args = operation.returns.slice.elements

            if output_type == "InputEventStream":
                stream_type = StreamType.INPUT
                event_input_type = stream_args[0].canonical_name
            elif output_type == "OutputEventStream":
                stream_type = StreamType.OUTPUT
                event_output_type = stream_args[0].canonical_name
            elif output_type == "DuplexEventStream":
                stream_type = StreamType.DUPLEX
                event_input_type = stream_args[0].canonical_name
                event_output_type = stream_args[1].canonical_name

            output_info = StructureInfo(
                name=stream_args[-1].canonical_name,
                module_path=stream_args[-1].canonical_path
            )
        else:
            output_info = StructureInfo(
                name=output_type,
                module_path=operation.returns.canonical_path
            )

        return OperationInfo(
            name=operation.name,
            module_path=operation.path,
            input=input_info,
            output=output_info,
            stream_type=stream_type,
            event_input_type=event_input_type,
            event_output_type=event_output_type,
        )

    def _extract_models(self, models_module: Module, operations: list[OperationInfo]) -> ModelsInfo:
        """Extract structures, unions, enums, and errors from the models module."""
        structures, unions, enums, errors = [], [], [], []

        for member in models_module.members.values():
            # Skip imported and private members
            if member.is_imported or member.is_private:
                continue

            if self._is_union(member):
                unions.append(UnionInfo(
                    name=member.name,
                    module_path=member.path,
                    members=self._extract_union_members(member, models_module)
                ))
            elif self._is_enum(member):
                enums.append(EnumInfo(
                    name=member.name,
                    module_path=member.path
                ))
            elif self._is_error(member):
                errors.append(ErrorInfo(
                    name=member.name,
                    module_path=member.path
                ))
            else:
                if member.is_class:
                    structures.append(StructureInfo(
                        name=member.name,
                        module_path=member.path
                    ))
        
        duplicates = set()
        for structure in structures:
            if (self._is_operation_io_type(structure.name, operations) or 
                self._is_union_member(structure.name, unions)):
                duplicates.add(structure)
        
        structures = [struct for struct in structures if struct not in duplicates]

        return ModelsInfo(
            structures=structures,
            unions=unions,
            enums=enums,
            errors=errors
        )

    def _is_union(self, member: Member) -> bool:
        """Check if a type is a union type."""
        if member.is_attribute:   
            # Check for Union[...] syntax
            if isinstance(member.value, ExprSubscript):
                if member.value.left.name == "Union":
                    return True

            # Check for PEP 604 (X | Y) syntax
            if isinstance(member.value, ExprBinOp):
                return True

        return False

    def _extract_union_members(self, union_class: TypeAlias, models_module: Module) -> list[StructureInfo]:
        """Extract member types from a union."""
        members = []
        value_str = str(union_class.value)

        # Handle Union[X | Y | Z] syntax
        if value_str.startswith("Union[") and value_str.endswith("]"):
            value_str = value_str.removeprefix("Union[").removesuffix("]")

        member_names = [member.strip() for member in value_str.split("|")]
        
        for name in member_names:
            member_object = models_module.members.get(name)
            members.append(StructureInfo(
                name=member_object.name,
                module_path=member_object.path
            ))

        return members

    def _is_enum(self, member: Member) -> bool:
        """Check if a module member is an enum."""
        if not member.is_class:
            return False

        for base in member.bases:
            if base.name  in ('StrEnum', 'IntEnum'):
                return True

        return False
    
    def _is_error(self, member: Member) -> bool:
        """Check if a module member is an error."""
        if not member.is_class:
            return False

        for base in member.bases:
            if base.name  in ('ServiceError', 'ModeledError'):
                return True

        return False

    def _is_operation_io_type(self, type_name: str, operations: list[OperationInfo]) -> bool:
        """Check if a type is used as operation input/output."""
        for op in operations:
            if type_name == op.input.name or type_name == op.output.name:
                return True
        return False

    def _is_union_member(self, type_name:str, unions: list[UnionInfo]) -> bool:
        """Check if a type is used as union member."""
        for union in unions:
            for member in union.members:
                if type_name == member.name:
                    return True
        return False

    def _generate_client_docs(self, client_info: ClientInfo) -> None:
        """Generate all documentation files for a client."""
        logger.info(f"Writing files to mkdocs virtual filesystem for {self.service_name}")

        self._generate_index(client_info)
        self._generate_operations(client_info.operations)
        self._generate_structures(client_info.models.structures)
        self._generate_errors(client_info.models.errors)
        self._generate_unions(client_info.models.unions)
        self._generate_enums(client_info.models.enums)

    def _generate_index(self, client_info: ClientInfo) -> None:
        """Generate the main index.md file."""
        content = f"# {self.service_name}\n\n"

        # Client section
        content += "## Client\n\n"
        content += f"::: {client_info.module_path}\n"
        content += "    options:\n"
        content += "        merge_init_into_class: true\n"
        content += "        docstring_options:\n"
        content += "            ignore_init_summary: true\n"
        content += "        members: false\n"
        content += "        heading_level: 3\n\n"

        # Operations section
        if client_info.operations:
            content += "## Available Operations\n\n"
            for op in sorted(client_info.operations, key=lambda x: x.name):
                content += f"- [`{op.name}`](operations/{op.name}.md)\n\n"

        # Configuration section
        content += "## Configuration\n\n"
        content += f"::: {client_info.config.module_path}\n"
        content += "    options:\n"
        content += "        merge_init_into_class: true\n"
        content += "        docstring_options:\n"
        content += "            ignore_init_summary: true\n"
        content += "        heading_level: 3\n\n"
        content += f"::: {client_info.plugin.module_path}\n"
        content += "    options:\n"
        content += "        heading_level: 3\n\n"

        models = client_info.models

        # Structures section
        if models.structures:
            content += "## Structures\n\n"
            for struct in sorted(models.structures, key=lambda x: x.name):
                content += f"- [`{struct.name}`](structures/{struct.name}.md)\n\n"

        # Errors section
        if models.errors:
            content += "## Errors\n\n"
            for error in sorted(models.errors, key=lambda x: x.name):
                content += f"- [`{error.name}`](errors/{error.name}.md)\n\n"

        # Unions section
        if models.unions:
            content += "## Unions\n\n"
            for union in sorted(models.unions, key=lambda x: x.name):
                content += f"- [`{union.name}`](unions/{union.name}.md)\n\n"

        # Enums section
        if models.enums:
            content += "## Enums\n\n"
            for enum in sorted(models.enums, key=lambda x: x.name):
                content += f"- [`{enum.name}`](enums/{enum.name}.md)\n\n"

        docs_path = f"clients/{self.service_name}/index.md"
        with mkdocs_gen_files.open(docs_path, "w") as f:
            f.write(content)

        logger.info(f"Generated index.md")

    def _generate_operations(self, operations: list[OperationInfo]) -> None:
        """Generate operation documentation files."""
        for op in operations:
            content = f"# {op.name}\n\n"

            # Operation section
            content += "## Operation\n\n"
            content += f"::: {op.module_path}\n"
            content += "    options:\n"
            content += "        heading_level: 3\n\n"

            # Input section
            content += "## Input\n\n"
            content += f"::: {op.input.module_path}\n"
            content += "    options:\n"
            content += "        heading_level: 3\n\n"

            # Output section - handle all stream types
            content += "## Output\n\n"

            if op.stream_type == StreamType.INPUT:
                content += "This operation returns an `InputEventStream` for client-to-server streaming.\n\n"
                content += "### Event Stream Structure\n\n"
                content += "#### Input Event Type\n\n"
                content += f"[`{op.event_input_type}`](../unions/{op.event_input_type}.md)\n\n"
                content += "### Initial Response Structure\n\n"
                content += f"::: {op.output.module_path}\n"
                content += "    options:\n"
                content += "        heading_level: 4\n\n"
            elif op.stream_type == StreamType.OUTPUT:
                content += "This operation returns an `OutputEventStream` for server-to-client streaming.\n\n"
                content += "### Event Stream Structure\n\n"
                content += "#### Output Event Type\n\n"
                if op.event_output_type:
                    content += f"[`{op.event_output_type}`](../unions/{op.event_output_type}.md)\n\n"
                content += "### Initial Response Structure\n\n"
                content += f"::: {op.output.module_path}\n"
                content += "    options:\n"
                content += "        heading_level: 4\n\n"
            elif op.stream_type == StreamType.DUPLEX:
                content += "This operation returns a `DuplexEventStream` for bidirectional streaming.\n\n"
                content += "### Event Stream Structure\n\n"
                content += "#### Input Event Type\n\n"
                if op.event_input_type:
                    content += f"[`{op.event_input_type}`](../unions/{op.event_input_type}.md)\n\n"
                content += "#### Output Event Type\n\n"
                if op.event_output_type:
                    content += f"[`{op.event_output_type}`](../unions/{op.event_output_type}.md)\n\n"
                content += "### Initial Response Structure\n\n"
                content += f"::: {op.output.module_path}\n"
                content += "    options:\n"
                content += "        heading_level: 4\n\n"
            else:
                # No streaming
                content += f"::: {op.output.module_path}\n"
                content += "    options:\n"
                content += "        heading_level: 3\n\n"

            docs_path = f"clients/{self.service_name}/operations/{op.name}.md"
            with mkdocs_gen_files.open(docs_path, "w") as f:
                f.write(content)

        logger.info(f"Generated {len(operations)} operation files")

    def _generate_structures(self, structures: list[StructureInfo]) -> None:
        """Generate structure documentation files."""
        for struct in structures:
            content = f"::: {struct.module_path}\n"
            content += "    options:\n"
            content += "        heading_level: 1\n"

            docs_path = f"clients/{self.service_name}/structures/{struct.name}.md"
            with mkdocs_gen_files.open(docs_path, "w") as f:
                f.write(content)

        logger.info(f"Generated {len(structures)} structure files")

    def _generate_unions(self, unions: list[UnionInfo]) -> None:
        """Generate union documentation files."""
        for union in unions:
            content = f"::: {union.module_path}\n"
            content += "    options:\n"
            content += "        heading_level: 1\n\n"

            # Add union members
            if union.members:
                content += "## Union Members\n\n"
                for member in union.members:
                    content += f"::: {member.module_path}\n"
                    content += "    options:\n"
                    content += "        heading_level: 3\n\n"

            docs_path = f"clients/{self.service_name}/unions/{union.name}.md"
            with mkdocs_gen_files.open(docs_path, "w") as f:
                f.write(content)

        logger.info(f"Generated {len(unions)} union files")

    def _generate_enums(self, enums: list[EnumInfo]) -> None:
        """Generate enum documentation files."""
        for enum in enums:
            content = f"::: {enum.module_path}\n"
            content += "    options:\n"
            content += "        heading_level: 1\n"
            content += "        members: true\n"

            docs_path = f"clients/{self.service_name}/enums/{enum.name}.md"
            with mkdocs_gen_files.open(docs_path, "w") as f:
                f.write(content)

        logger.info(f"Generated {len(enums)} enum files")

    def _generate_errors(self, errors: list[ErrorInfo]) -> None:
        """Generate error documentation files."""
        for error in errors:
            content = f"::: {error.module_path}\n"
            content += "    options:\n"
            content += "        heading_level: 1\n"
            content += "        members: true\n"

            docs_path = f"clients/{self.service_name}/errors/{error.name}.md"
            with mkdocs_gen_files.open(docs_path, "w") as f:
                f.write(content)

        logger.info(f"Generated {len(errors)} error files")


def extract_service_name(package_name: str) -> str:
    """Extract service name from client package name."""
    return (
        package_name
        .replace("aws-sdk-", "")
        .replace("-", " ")
        .title()
    )


def main() -> int:
    """Main entry point for the documentation generator."""
    repo_root = Path(__file__).parent.parent.absolute()
    output_dir = repo_root / "docs" / "clients"
    clients_dir = repo_root / "clients"

    try:
        for client_dir in clients_dir.iterdir():
            if client_dir.is_dir() and client_dir.name != "aws-sdk-python":
                service_name = extract_service_name(client_dir.name)
                logger.info(f"Generating docs for {service_name}")
                generator = DocStubGenerator(client_dir, output_dir / service_name, service_name)
                generator.generate()

        return 0
    except Exception as e:
        logger.error(f"Error generating doc stubs: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
else:
    # When imported by mkdocs-gen-files, run the generation
    main()
