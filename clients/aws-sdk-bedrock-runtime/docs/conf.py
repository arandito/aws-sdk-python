# Code generated by smithy-python-codegen DO NOT EDIT.

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "Amazon Bedrock Runtime"
author = "Amazon Web Services"
release = "0.0.1"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = []

autodoc_default_options = {
    "exclude-members": "deserialize,deserialize_kwargs,serialize,serialize_members"
}

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "logo": {
        "text": "Amazon Bedrock Runtime",
    }
}

autodoc_typehints = "description"
