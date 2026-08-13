# Contributing Guide

Welcome — thank you for contributing. This guide covers the workflow, standards, and expectations.

1) Getting started
- Fork the repo and create a branch: feature/short-description or fix/short-description
- Run `make install` to install dev dependencies
- Run `pre-commit install` to enable hooks

2) Code style and checks
- Use Black and isort for formatting
- Run `pre-commit run --all-files` before committing
- Type-check with `make typecheck` (mypy)

3) Tests
- Add unit tests to `tests/`. Keep tests deterministic. Use pytest fixtures for setup.
- Run `make test` and ensure coverage is acceptable

4) PRs
- Open a pull request to `main` with a clear summary
- Link issues (if any) and include tests for new behavior
- CI must pass: lint, tests, coverage, security scans

5) Reviewing and merging
- At least one maintainer review required
- Address review comments, keep commits tidy (rebase or squash as requested)

6) Issue reporting
- Use ISSUE_TEMPLATE for bug reports and feature requests

7) Becoming a maintainer
- Contribute consistently, respond to reviews, and propose improvements. Maintainers will add collaborators via CODEOWNERS.

8) Security
- Report security issues privately via GitHub security advisories or contact maintainers.

Thanks for helping improve UPE!