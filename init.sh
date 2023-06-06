#!/bin/bash

virtualenv venv
source ./venv/bin/activate  

pip install django
pip install setuptools==44.1.0
pip install --upgrade pip