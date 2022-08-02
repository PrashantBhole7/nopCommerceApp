#!/bin/bash

source venv/bin/activate
python -m pytest -v -m "sanity" --html=Reports/report.html testCases/ --browser chrome
# pytest -v -m "sanity and regression" --html=Reports/report.html testCases/ --browser chrome
# pytest -v -m "sanity or regression" --html=Reports/report.html testCases/ --browser chrome
# pytest -v -m "regression" --html=Reports/report.html testCases/ --browser chrome

