# Swag Labs Capybara

This project automates both API and UI tests for the Swag Labs website using Python. The tests are organized using the pytest framework, and can be executed locally or via Jenkins in a Docker container

Project Structure
```plaintext
├── api_methods          # Modules containing API interaction methods
├── pages                # Page Object Models representing UI components
├── swaglabs             # Core logic related to the Swag Labs application
├── test_data            # Test data for API and UI tests
│   ├── api
│   └── ui
├── tests                # Test cases for API and UI
│   ├── api
│   └── ui
├── .github              # GitHub workflows (CI/CD pipeline configurations)
├── .gitignore           # Files and directories to be ignored by git
├── Dockerfile           # Dockerfile for setting up the testing environment
├── pytest.ini           # Pytest configuration file
├── README.md            # Project documentation (this file)
├── requirements.txt     # Python dependencies
└── conftest.py          # Fixtures and configuration for pytest

```

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Docker (for running Jenkins and tests in a container)

## Installation
Follow these steps to set up the project on your local machine:
Clone the repository:
```bash
git clone https://github.com/VladislavSavchuk/swag_labs_kapibara.git
```
Create a Virtual environment:
```bash
python -m venv swag_labs_kapibara
```
Navigate to the project directory:
```bash
cd swag_labs_kapibara
```
Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests locally
To run the tests locally using pytest:

Run all tests:
```bash
pytest
```

Run specific tests:
To run tests in a specific directory (e.g., API tests):

```bash
pytest tests/api
```

To run a specific test file:

```bash
pytest tests/ui/test_example.py
```

To execute ALL tests w/ DEBUG log level:
```bash
pytest . --log-level=DEBUG
```

## Available markers:
Pytest markers allow you to select specific groups of tests to run. Here are the available markers in this project:
```
add_cart: Tests adding products to the cart.
login: All login tests.
login_success: Login tests with a user who is not locked out.
login_incorrect: Login tests with incorrect login credentials.
all_products_page: All products page-related tests.
product_page: Product page-related tests.
product_sort: All product page tests related to sorting.
shopping_cart: Tests related to the shopping cart.
checkout: All tests related to the checkout and payment process.
regression: Run the regression test suite.
smoke: Run the smoke test suite.
unittests: Run the unittest suite.
uitests: Run the UI test suite.
api: Run API tests.
pet_api: Run API tests for /pet endpoint.
user_api: Run API tests for /user endpoint.
order_api: Run API tests for /store/order endpoint.
```

## How to Use Docker to Run the Application
Follow these steps to build and run the application using Docker:

1. Build the Docker Image
Navigate to your project directory and build the Docker image:

```bash
docker build -t flask-app .
```

## Running Tests with Docker and Jenkins
You can also run the tests automatically using Jenkins in a Docker container. Here's how to set it up:

1. Build the Docker image:
Navigate to your project directory and build the Docker image:

```bash
docker build -t swag-labs-tests .
```

2. Run Jenkins in Docker:
Start a Jenkins container with Docker:

```bash
docker run -d -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```
Access Jenkins at http://localhost:8080 to configure your pipeline.

3. Configure Jenkins Pipeline:
- Create a new Jenkins pipeline.
- Use the Docker image swag-labs-tests to run the tests.
- Set up the pipeline script to execute the pytest command within the Docker container.

4. Trigger Tests Automatically:
- Once Jenkins is set up, you can trigger tests automatically on code commits or schedule them to run at specific intervals.
