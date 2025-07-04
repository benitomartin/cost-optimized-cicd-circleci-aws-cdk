# Cost-Optimized CI/CD Pipeline. Managing AWS Resources with CircleCI and AWS CDK

This project aims to create a cost-optimized CI/CD pipeline for managing AWS resources using CircleCI and the AWS Cloud Development Kit (CDK). The pipeline will automate the deployment and management of AWS infrastructure, ensuring efficient resource utilization and cost savings.

## Table of Contents

- [Cost-Optimized CI/CD Pipeline. Managing AWS Resources with CircleCI and AWS CDK](#cost-optimized-cicd-pipeline-managing-aws-resources-with-circleci-and-aws-cdk)
  - [Table of Contents](#table-of-contents)
  - [Project Structure](#project-structure)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [License](#license)

## Project Structure

```text
├── LICENSE
├── Makefile
├── README.md
├── cdk
│   ├── README.md
│   ├── app.py
│   ├── .env
│   ├── infrastructure
│   │   ├── __init__.py
│   │   ├── compute_stack.py
│   │   ├── monitoring_stack.py
│   │   └── vpc_stack.py
│   ├── requirements.txt
└── circleci
    ├── config.yml
```

## Prerequisites

- Python 3.12
- AWS CDK installed
- AWS CLI configured with appropriate credentials
- CircleCI account
- Node.js installed (for CDK)

## Installation

1. Clone the repository:

   ```bash
   git clone cost-optimized-cicd-circleci-aws-cdk.git 
   cd cost-optimized-cicd-circleci-aws-cdk
   ```

2. Create a virtual environment:

    ```bash
    cd cdk
    python -m venv .venv
    ```
  
    This will create a virtual environment in the `.venv` directory.

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
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the root directory:

   ```bash
    cp .env.example .env
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
