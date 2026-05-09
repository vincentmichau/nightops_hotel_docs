$ErrorActionPreference = "Stop"
python -m pytest -q --junitxml=test-report.xml
python -m compileall src
if (!(Test-Path ruff-report.txt)) { "Ruff report placeholder" | Out-File ruff-report.txt -Encoding utf8 }
