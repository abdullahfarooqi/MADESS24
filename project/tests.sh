#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define the project directory
PROJECT_DIR=$(dirname "$0")

# Define the virtual environment directory
VENV_DIR="$PROJECT_DIR/venv"

# Check if virtual environment exists, if not, create one
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install required packages
echo "Installing required packages..."
pip install -r "$PROJECT_DIR/requirements.txt"

# Run pytest
echo "Running tests..."
pytest "$PROJECT_DIR/data_test.py" --no-header --no-summary -q

# Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate

echo "Test run complete."
