# Project Name

## Table of Contents

- [Project Name](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Project Structure](#project-structure)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Configuration](#configuration)
    - [Module 1](#module-1)
    - [Module 2](#module-2)
    - [Testing](#testing)
    - [Quality Checks](#quality-checks)
  - [License](#license)

## Overview

Briefly describe the project, its purpose, and key features.

## Project Structure

```text
├── .github
├── src
├── tests
├── LICENSE
├── Makefile
├── pyproject.toml
├── README.md
├── uv.lock
```

## Prerequisites

- Python 3.12
- XXX

## Installation

1. Clone the repository:

   ```bash
   git clone XXX
   cd XXX
   ```

   ```bash
    cd cdk
    cdk init app --language python
    ```

uv venv
uv pip install -r requirements.txt


CPUUtilization	0.25160913318

CPUUtilization value (e.g., 0.2516)
This number is a percentage expressed as a decimal fraction.
So, 0.2516 means ~0.25% CPU utilization — very low CPU use.

CloudWatch CPUUtilization metric measures how busy the CPU is over a given period (average).

# Install EPEL repo
sudo amazon-linux-extras install epel -y

# Install stress-ng
sudo yum install -y stress-ng


# Generate CPU load (will trigger scaling)
Generate CPU load (will trigger scaling)
Run stress-ng for 5 minutes on 4 CPU cores in background
stress-ng --cpu 4 --timeout 300s



















2. Create a virtual environment:

   ```bash
   uv venv
   ```

3. Activate the virtual environment:
   - On Windows:

     ```bash
     .venv\Scripts\activate
     ```

   - On Unix or MacOS:

     ```bash
     source .venv/bin/activate
     ```

4. Install the required packages:

   ```bash
   uv sync --all-groups --all-extra
   ```

5. Create a `.env` file in the root directory:

   ```bash
    cp .env.example .env
   ```

## Usage

### Configuration

Configure API keys, model names, and other settings by editing:

src/configs/settings.py
src/configs/config.yaml

### Module 1

(Add description or usage example)

### Module 2

(Add description or usage example)

### Testing

Run all tests:

```bash
make tests
```

### Quality Checks

Run all quality checks (lint, format, type check, clean):

```bash
make all
```

Individual Commands:

- Display all available commands:

    ```bash
    make help
    ```

- Check code formatting:

    ```bash
    make ruff-check
    ```

- Format code:

    ```bash
    make ruff-format
    ```

- Lint code:

    ```bash
    make ruff-lint
    ```

- Type check

    ```bash
    make mypy
  ```

- Clean cache and build files:

    ```bash
    make clean
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
