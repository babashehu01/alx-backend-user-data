# # Basic authentication

This project implements a basic authentication system on a simple API.

## Requirements

* Python 3.5+
* Pipenv

## Setup

1. Clone the repository:

git clone https://github.com/babashehu01/basic-authentication.git


2. Install the dependencies:

pipenv install


3. Set the environment variable `AUTH_TYPE` to `basic`:

export AUTH_TYPE=basic


## Usage

1. Start the server:

pipenv run python3 app.py


2. The API is now running on port 5000. You can test it using curl:

curl http://localhost:5000/api/v1/status

This will return the status of the API.

    To access the /api/v1/users endpoint, you need to authenticate first. You can do this by passing the username and password in the Authorization header. For example:

curl -u username:password http://localhost:5000/api/v1/users

If the username and password are valid, you will be able to access the endpoint. Otherwise, you will get an error.
Documentation

The documentation for the API is available at http://localhost:5000/apidocs/.
Tests

The tests for the API are located in the tests directory. You can run them using the following command:

pipenv run python3 -m unittest tests.
