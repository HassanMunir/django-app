# DJANGO CI Pipeline

This project defines a Continuous Integration (CI) pipeline for a Django application. The pipeline is configured using GitHub Actions and runs automated tests, checks code quality, builds a Docker image, and performs security scans.

## Features
- **Automated Testing**: Uses `pytest` to run tests with coverage and type checking with `mypy`.
- **Security Scanning**: Runs static application security testing (SAST) using `bandit`.
- **Code Quality**: Enforces code style using `flake8` and `black`.
- **Docker Support**: Builds a Docker image for the Django app.
- **Caching Dependencies**: Uses GitHub Actions caching to speed up dependency installation.

## CI Pipeline Workflow

The pipeline is triggered on push or pull request events to the `main` branch. The following steps are executed:

1. **Checkout Code**: The code is checked out from the repository.
2. **Setup Python**: Python 3.12 is set up.
3. **Install Dependencies**: All required Python dependencies are installed and outdated dependencies are updated.
4. **Cache Python Dependencies**: Caches pip dependencies to speed up subsequent runs.
5. **Run Bandit for SAST**: Runs `bandit` for security scanning to identify vulnerabilities in the code.
6. **Build Docker Image**: Builds a Docker image tagged with the current commit SHA.
7. **Run Flake8 & Black**: Runs `flake8` for linting and `black` for automatic code formatting.
8. **List Files in Repository**: Lists files in the repository.
9. **Set Python Path**: Configures the Python path for the app.
10. **Run Pytest**: Runs tests with `pytest` and generates a coverage report.
11. **Run Pytest with Coverage**: Runs tests with coverage and generates an HTML coverage report.
12. **Run Mypy for Type Checking**: Runs `mypy` to check types and verifies installed packages.

## Prerequisites

- Python 3.12 or higher
- Docker (for building the Docker image)
- GitHub Actions for CI integration

## Requirements

Ensure the following packages are installed in your environment (use `pip install -r requirements.txt`):

```txt
django==5.1.3
sqlparse==0.5.2
flake8==7.1.1
black==24.10.0
mypy==1.13.0
pytest==8.3.3
pytest-django==4.9.0
pytest-cov==6.0.0
coverage==7.6.8
gunicorn==23.0.0
django-stubs==5.1.1
sqlalchemy==2.0.34
bandit==1.8.0