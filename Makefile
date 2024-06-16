.DEFAULT_GOAL := help

SHELL=/bin/bash


.PHONY: install
install:  ## Install a virtual environment
	@poetry install -vv


.PHONY: fmt
fmt:  ## Run autoformatting and linting
	@poetry run pip install pre-commit
	@poetry run pre-commit install
	@poetry run pre-commit run --all-files


.PHONY: clean
clean:  ## Clean up caches and build artifacts
	@git clean -X -d -f
	@git branch -v | grep "\[gone\]" | cut -f 3 -d ' ' | xargs git branch -D'


# Define the demo target
.PHONY: demo
demo: install ## Run a demo
	@poetry run demo


.PHONY: help
help:  ## Display this help screen
	@echo
	@echo -e "\033[1mAvailable commands:\033[0m"
	@echo
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}' | sort
	@echo


.PHONY: conduct
conduct: ## Generete CODE of CONDUCT and Contributing
	@poetry run pip install jinja2 toml
	@gh gist clone a4a054e3e80a8021c351b027280d3b09 tmp
	@poetry run python tmp/parse.py
	@rm -rf tmp
