$ErrorActionPreference = "Stop"
./scripts/build_windows.ps1
"NightOps v15.11" | Out-File release-report.md -Encoding utf8
