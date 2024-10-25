# Advanced Python Calculator

This project is an advanced calculator application developed in Python, featuring various mathematical operations and a plugin system for extending functionality. The calculator supports operations such as addition, subtraction, multiplication, and division, along with a history manager to keep track of calculations.

## Features

- **Basic Operations**: Supports addition, subtraction, multiplication, and division.
- **Plugin System**: Extendable architecture to add new operations easily.
- **History Management**: Keeps track of past calculations.
- **Unit Testing**: Comprehensive test suite using `pytest` to ensure code quality.
- **Code Quality**: Uses `pylint` for linting to maintain high code standards.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Saitejanagapuri55/advanced_python_calculator.git
   cd advanced_python_calculator
Set up a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the calculator in your terminal:

bash
Copy code
python main.py
Follow the on-screen instructions to perform calculations.

Running Tests
To run the test suite, execute:

bash
Copy code
pytest tests
Code Quality Checks
To check code quality with pylint, run:

bash
Copy code
pylint app