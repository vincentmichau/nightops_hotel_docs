$ErrorActionPreference = "Stop"
Write-Host "== NightOps qa_summary.ps1 v15.16 =="

$lines = @()
$lines += "# QA summary NightOps v15.16"
$lines += ""
$lines += "- test-report.xml: $((Test-Path 'test-report.xml'))"
$lines += "- ruff-report.txt: $((Test-Path 'ruff-report.txt'))"
$lines += "- generated: $(Get-Date -Format o)"
$lines | Out-File qa-summary.md -Encoding utf8

if (!(Test-Path "qa-summary.md")) { throw "qa-summary.md manquant" }
