$ErrorActionPreference = "Stop"
if (!(Test-Path "nightops-portable.zip")) { throw "nightops-portable.zip manquant" }
$ZipItem = Get-Item "nightops-portable.zip"
if ($ZipItem.Length -lt 1024) { throw "nightops-portable.zip semble trop petit" }
Write-Host "Release zip OK: $($ZipItem.FullName) - $($ZipItem.Length) bytes"
