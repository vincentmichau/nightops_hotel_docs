$ErrorActionPreference = "Stop"
./scripts/run_tests.ps1
python -m PyInstaller packaging/pyinstaller/nightops_hotel.spec
if (!(Test-Path dist)) { throw "Dossier dist manquant après PyInstaller" }
if (Test-Path nightops-portable.zip) { Remove-Item nightops-portable.zip -Force }
if (Test-Path dist/nightops) {
  Compress-Archive -Path dist/nightops/* -DestinationPath nightops-portable.zip -Force
} elseif (Test-Path dist/nightops.exe) {
  Compress-Archive -Path dist/nightops.exe -DestinationPath nightops-portable.zip -Force
} else {
  throw "Sortie PyInstaller introuvable : attendu dist/nightops ou dist/nightops.exe"
}
if (!(Test-Path nightops-portable.zip)) { throw "nightops-portable.zip non généré" }
