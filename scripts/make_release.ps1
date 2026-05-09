Write-Host "Release NightOps v13"
./scripts/build_windows.ps1
"NightOps v13 release" | Out-File release-report.md
