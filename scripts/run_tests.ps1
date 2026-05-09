$ErrorActionPreference = "Stop"
python -m pytest -q --junitxml=test-report.xml
python -m compileall src
