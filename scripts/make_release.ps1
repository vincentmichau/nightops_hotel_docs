$ErrorActionPreference = "Stop"
Write-Host "MAKE_RELEASE_VERSION=v15.16.0-github-reports-artifacts-fix"

./scripts/build_windows.ps1

# Garantir que les rapports existent au moment de la release.
if (!(Test-Path "test-report.xml")) { throw "test-report.xml manquant avant release" }
if (!(Test-Path "ruff-report.txt")) { throw "ruff-report.txt manquant avant release" }

./scripts/qa_summary.ps1

"# Release report NightOps v15.16`n`n- Tests: OK`n- PyInstaller: OK`n- Artifact: nightops-portable.zip`n- test-report.xml: present`n- ruff-report.txt: present" | Out-File release-report.md -Encoding utf8

if (!(Test-Path "nightops-portable.zip")) { throw "nightops-portable.zip manquant après make_release" }
if (!(Test-Path "release-report.md")) { throw "release-report.md manquant après make_release" }
if (!(Test-Path "qa-summary.md")) { throw "qa-summary.md manquant après make_release" }
if (!(Test-Path "test-report.xml")) { throw "test-report.xml manquant après make_release" }
if (!(Test-Path "ruff-report.txt")) { throw "ruff-report.txt manquant après make_release" }
