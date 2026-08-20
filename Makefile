DOCS_PORT ?= 8000
PYTHON_VERSION := 3.12

.PHONY: build-py check-py docs docs-serve docs-clean docs-install docs-lock \
	install lint-py test-py venv

install:
	uv sync --all-packages --all-extras
	@printf "\n\nWorkspace initialized, please run:\n\033[36msource .venv/bin/activate\033[0m"

lint-py:
	uv run ruff check packages --fix --config pyproject.toml
	uv run ruff format packages --config pyproject.toml

check-py:
	uv run ruff check packages --config pyproject.toml
	uv run ruff format --check packages --config pyproject.toml
	uv run pyright packages

test-py:
	uv run pytest packages

build-py:
	uv build --all-packages

venv:
	uv venv --python $(PYTHON_VERSION)

docs-lock: venv
	uv pip compile requirements-docs.in -o requirements-docs.txt

docs-install: venv
	uv pip install -r requirements-docs.txt
	uv pip install -e clients/*

docs-clean:
	rm -rf site docs/clients

docs-generate:
	uv run python scripts/docs/generate_all_doc_stubs.py
	uv run python scripts/docs/generate_nav.py

docs: docs-generate
	uv run zensical build

docs-serve:
	@[ -d site ] || $(MAKE) docs
	uv run python -m http.server $(DOCS_PORT) --bind 127.0.0.1 --directory site
