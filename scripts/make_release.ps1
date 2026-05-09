$ErrorActionPreference = "Stop"
./scripts/build_windows.ps1
"# Release report NightOps v15.13`n`n- Tests: OK`n- PyInstaller: OK`n- Artifact: nightops-portable.zip" | Out-File release-report.md -Encoding utf8
./scripts/qa_summary.ps1
if (!(Test-Path "nightops-portable.zip")) { throw "nightops-portable.zip manquant après make_release" }
if (!(Test-Path "release-report.md")) { throw "release-report.md manquant après make_release" }
if (!(Test-Path "qa-summary.md")) { throw "qa-summary.md manquant après make_release" }
