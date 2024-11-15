#!/bin/bash

# Stop the script if any command fails
set -e

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv env

# Detect OS and provide the activation command
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
    # Linux or Mac
    ACTIVATE_SCRIPT="source env/bin/activate"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows (Git Bash or Cygwin)
    ACTIVATE_SCRIPT="env\\Scripts\\activate"
else
    echo "Unsupported OS. Please activate the virtual environment manually."
    exit 1
fi

echo "To activate the virtual environment, run:"
echo "$ACTIVATE_SCRIPT"

# Activate the virtual environment
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
    source env/bin/activate
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    source env/Scripts/activate
fi

# Upgrade pip and install dependencies
echo "Upgrading pip and installing dependencies..."
pip install --upgrade pip
pip install fastapi uvicorn[standard] pandas

echo "Setup complete! To activate the virtual environment, run:"
echo "$ACTIVATE_SCRIPT"
