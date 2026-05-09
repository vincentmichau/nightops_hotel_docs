Write-Host "Run NightOps v13 tests"
ruff check src tests | Tee-Object -FilePath ruff-report.txt
pytest -q --junitxml=test-report.xml
python -m compileall src
