$ErrorActionPreference = "Stop"
python -m pytest -q --junitxml=test-report.xml
python -m compileall src
if (!(Test-Path ruff-report.txt)) { "Ruff non exécuté dans ce script minimal" | Out-File ruff-report.txt -Encoding utf8 }
