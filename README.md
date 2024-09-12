# AI test generation pipeline demo

This repository is a demo showcasing the integration of AI in development pipelines. Using GitHub Actions and ChatGPT, this project automatically generates unit tests from Python code. The workflow creates a new branch with the recommended unit tests and opens a pull request for review. This demonstration highlights the potential of AI to assist in software development by automating test creation, thus improving efficiency and code quality.

## Setup

1. **Configure GitHub Actions**:
    - In your project, go to ``` Settings ``` > ``` Actions ``` > ``` General ```
    - Scroll down to ``` Workflow permissions ```
    - Make sure that ``` Read and write permissions ``` and ``` Allow GitHub Actions to create and approve pull requests ``` are checked

2. **Add your ChatGPT API key**:
    - Go to ``` Settings ``` > ``` Secrets and variables ``` > ``` Actions ``` > ``` New repository secret ```
    - Make sure that the secret is named ``` CHATGPT_API_KEY ```, otherwise the workflow wont use it

## Usage

1. **Create a development branch**:
    ```bash
        git checkout -b dev
    ```

2. **Add some functions**:
    - Create new functions to a new python-file
    - In this demo you can uncomment the first function in ``` code_to_be_tested.py ``` file to simulate new functions

3. **Push changes**:
    ```bash
    git add .
    git commit -m "Add new functions"
    git push origin dev
    ```

After pushig you new code, GitHub Actions workflow is started that generates unit tests for your new python function file or ``` code_to_be_tested.py ``` using ChatGPT, and then creates a pull request with the recommended tests once they've been tested that they work.

Files that are used for test generation and testing can be found at ``` test-gen ```
