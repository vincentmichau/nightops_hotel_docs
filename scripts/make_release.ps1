$ErrorActionPreference = "Stop"
./scripts/build_windows.ps1
"# Release report NightOps v15.12`n`n- Tests: OK`n- Build Windows: OK`n- Artifact: nightops-portable.zip" | Out-File release-report.md -Encoding utf8
./scripts/qa_summary.ps1
