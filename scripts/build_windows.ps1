Write-Host "Build NightOps v13 portable Windows"
./scripts/run_tests.ps1
pyinstaller packaging/pyinstaller/nightops_hotel.spec
powershell Compress-Archive -Path dist/* -DestinationPath nightops-portable.zip
