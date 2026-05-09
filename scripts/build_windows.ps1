$ErrorActionPreference = "Stop"

Write-Host "== NightOps build_windows.ps1 v15.14 =="
Write-Host "Repository root: $PWD"

./scripts/run_tests.ps1

$SpecPath = "packaging/pyinstaller/nightops_hotel.spec"
$EntryPoint = "src/nightops_hotel/cli.py"

if (!(Test-Path $SpecPath)) {
  throw "Spec PyInstaller manquant: $SpecPath"
}
if (!(Test-Path $EntryPoint)) {
  throw "Entrée PyInstaller manquante: $EntryPoint"
}

if (Test-Path "build") { Remove-Item "build" -Recurse -Force }
if (Test-Path "dist") { Remove-Item "dist" -Recurse -Force }
if (Test-Path "nightops-portable.zip") { Remove-Item "nightops-portable.zip" -Force }

python -m PyInstaller --clean --noconfirm $SpecPath

if (!(Test-Path "dist")) {
  throw "Dossier dist manquant après PyInstaller"
}

Write-Host "== Contenu du dossier dist =="
Get-ChildItem "dist" -Recurse -Force | Format-List FullName,Length

$exeCandidates = Get-ChildItem "dist" -Recurse -Filter "*.exe" -File -ErrorAction SilentlyContinue
if ($exeCandidates.Count -eq 0) {
  throw "Aucun .exe généré par PyInstaller. Vérifier $SpecPath et $EntryPoint"
}

Write-Host "== EXE détectés =="
$exeCandidates | Format-List FullName,Length

$portableRoot = "dist/nightops"
if (Test-Path $portableRoot) {
  Compress-Archive -Path "$portableRoot/*" -DestinationPath "nightops-portable.zip" -Force
} else {
  Compress-Archive -Path "dist/*" -DestinationPath "nightops-portable.zip" -Force
}

if (!(Test-Path "nightops-portable.zip")) {
  throw "nightops-portable.zip non généré"
}

Write-Host "== Build portable OK =="
Get-Item "nightops-portable.zip" | Format-List FullName,Length
