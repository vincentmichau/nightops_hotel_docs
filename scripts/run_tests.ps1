$ErrorActionPreference = "Stop"

Write-Host "== NightOps run_tests.ps1 v15.16 =="
Write-Host "RUN_TESTS_VERSION=v15.16.0-github-reports-artifacts-fix"

# Nettoyage contrôlé des rapports pour éviter de publier des anciens fichiers.
if (Test-Path "test-report.xml") { Remove-Item "test-report.xml" -Force }
if (Test-Path "ruff-report.txt") { Remove-Item "ruff-report.txt" -Force }

# 1) Rapport Ruff toujours généré.
# On ne bloque pas ici si Ruff détecte un souci : on écrit le rapport puis on laisse pytest/compileall s'exécuter.
# La quality gate pourra ensuite décider si Ruff doit devenir bloquant.
try {
  python -m ruff check src tests *> ruff-report.txt
  $RuffExitCode = $LASTEXITCODE
  if ($RuffExitCode -ne 0) {
    Write-Warning "Ruff a retourné le code $RuffExitCode. Voir ruff-report.txt."
  }
} catch {
  "Ruff indisponible ou erreur Ruff : $($_.Exception.Message)" | Out-File ruff-report.txt -Encoding utf8
}

if (!(Test-Path "ruff-report.txt")) {
  "Ruff report placeholder - aucun rapport généré automatiquement" | Out-File ruff-report.txt -Encoding utf8
}

# 2) Rapport Pytest JUnit XML toujours demandé.
python -m pytest -q --junitxml=test-report.xml

if (!(Test-Path "test-report.xml")) {
  throw "test-report.xml n'a pas été généré par pytest"
}

# 3) Compilation Python.
python -m compileall src

# 4) Vérification finale des rapports attendus.
if (!(Test-Path "ruff-report.txt")) { throw "ruff-report.txt manquant après run_tests" }
if (!(Test-Path "test-report.xml")) { throw "test-report.xml manquant après run_tests" }

Write-Host "== Rapports tests présents =="
Get-Item test-report.xml | Format-List FullName,Length
Get-Item ruff-report.txt | Format-List FullName,Length
