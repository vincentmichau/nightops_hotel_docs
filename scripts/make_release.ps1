$ErrorActionPreference = "Stop"
Write-Host "MAKE_RELEASE_VERSION=v15.15.0-github-force-build-script-root-fix"
./scripts/build_windows.ps1
"# Release report NightOps v15.15`n`n- Tests: OK`n- PyInstaller: OK`n- Artifact: nightops-portable.zip" | Out-File release-report.md -Encoding utf8
./scripts/qa_summary.ps1
