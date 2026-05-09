$ErrorActionPreference = "Stop"

if (!(Test-Path "nightops-portable.zip")) { throw "nightops-portable.zip manquant" }
if (!(Test-Path "test-report.xml")) { throw "test-report.xml manquant" }
if (!(Test-Path "ruff-report.txt")) { throw "ruff-report.txt manquant" }
if (!(Test-Path "qa-summary.md")) { throw "qa-summary.md manquant" }
if (!(Test-Path "release-report.md")) { throw "release-report.md manquant" }

$ZipItem = Get-Item "nightops-portable.zip"
if ($ZipItem.Length -lt 1024) { throw "nightops-portable.zip semble trop petit" }

Write-Host "Release zip OK: $($ZipItem.FullName) - $($ZipItem.Length) bytes"
Write-Host "Reports OK: test-report.xml, ruff-report.txt, qa-summary.md, release-report.md"
