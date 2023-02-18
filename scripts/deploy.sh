#!/bin/bash

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Run Python script to retrieve OpenAI models and generate HTML output
python aidemo/app.py

# Copy HTML file to web server directory
cp output.html /var/www/html/

# Deactivate virtual environment
deactivate
