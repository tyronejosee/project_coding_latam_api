#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

uvicorn app.main:app --host 0.0.0.0 --port 10000
