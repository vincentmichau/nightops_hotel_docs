$ErrorActionPreference = "Stop"
if (!(Test-Path "nightops-portable.zip")) { throw "nightops-portable.zip manquant" }
$items = Get-ChildItem "nightops-portable.zip"
if ($items.Length -lt 1024) { throw "nightops-portable.zip semble trop petit pour contenir un build client valide" }
Write-Host "Release zip OK: $($items.FullName) - $($items.Length) bytes"
