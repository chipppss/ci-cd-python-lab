![CI](https://img.shields.io/github/actions/workflow/status/chipppss/ci-cd-python-lab/ci.yml?branch=main)

# ci-cd-python-lab

A minimal Python package to demonstrate CI/CD with GitHub Actions.

## Local usage
```bash
pip install -e .[dev]  # if you define extras, else:
pip install -r requirements-dev.txt
python -m calc add 2 3
pytest


# PR Demo Change
