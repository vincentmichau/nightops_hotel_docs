$ErrorActionPreference = "Stop"
Write-Host "== NightOps build_windows.ps1 v15.15 =="
Write-Host "Repository root: $PWD"
Write-Host "BUILD_SCRIPT_VERSION=v15.15.0-github-force-build-script-root-fix"
./scripts/run_tests.ps1
$SpecPath = "packaging/pyinstaller/nightops_hotel.spec"
$EntryPoint = "src/nightops_hotel/cli.py"
if (!(Test-Path $SpecPath)) { throw "Spec PyInstaller manquant: $SpecPath" }
if (!(Test-Path $EntryPoint)) { throw "Entrée PyInstaller manquante: $EntryPoint" }
if (Test-Path "build") { Remove-Item "build" -Recurse -Force }
if (Test-Path "dist") { Remove-Item "dist" -Recurse -Force }
if (Test-Path "nightops-portable.zip") { Remove-Item "nightops-portable.zip" -Force }
python -m PyInstaller --clean --noconfirm $SpecPath
if (!(Test-Path "dist")) { throw "Dossier dist manquant après PyInstaller" }
Write-Host "== Contenu complet de dist =="
Get-ChildItem "dist" -Recurse -Force | Format-List FullName,Length
$exeCandidates = @(Get-ChildItem "dist" -Recurse -Filter "*.exe" -File -ErrorAction SilentlyContinue)
if ($exeCandidates.Count -eq 0) { throw "Aucun .exe généré par PyInstaller. Voir listing dist." }
Write-Host "== EXE détectés =="
$exeCandidates | Format-List FullName,Length
$MainExe = $exeCandidates | Select-Object -First 1
$PortableRoot = $MainExe.Directory.FullName
Write-Host "PortableRoot détecté: $PortableRoot"
Compress-Archive -Path "$PortableRoot\*" -DestinationPath "nightops-portable.zip" -Force
if (!(Test-Path "nightops-portable.zip")) { throw "nightops-portable.zip non généré" }
$ZipItem = Get-Item "nightops-portable.zip"
if ($ZipItem.Length -lt 1024) { throw "nightops-portable.zip semble trop petit" }
Write-Host "== Build portable OK =="
$ZipItem | Format-List FullName,Length
