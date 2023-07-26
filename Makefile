.DEFAULT_GOAL := help

SHELL=/bin/bash


.PHONY: install
install:  ## Install a virtual environment
	@poetry install -vv

.PHONY: fmt
fmt:  ## Run autoformatting and linting
	@poetry run pre-commit run --all-files

.PHONY: clean
clean:  ## Clean up caches and build artifacts
	@rm -rf .pytest_cache/
	@rm -rf .ruff_cache/
	@rm -f **cqo1.ptf
	@find . -type f -name '*.py[co]' -delete -or -type d -name __pycache__ -delete


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
