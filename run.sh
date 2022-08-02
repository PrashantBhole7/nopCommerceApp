#!/bin/bash

export WORKSPACE=`pwd`

# Create/Activate virtualenv
virtualenv testenv -p /path/to/python/bin
source testenv/bin/activate

pip install -U pytest

pytest -v -m "sanity" --html=Reports/report.html testCases/ --browser chrome
# pytest -v -m "sanity and regression" --html=Reports/report.html testCases/ --browser chrome
# pytest -v -m "sanity or regression" --html=Reports/report.html testCases/ --browser chrome
# pytest -v -m "regression" --html=Reports/report.html testCases/ --browser chrome

