# Correction v15.16 - rapports manquants dans les artefacts

Problème constaté : `test-report.xml` et `ruff-report.txt` manquants dans certains artefacts.

Corrections :

- `scripts/run_tests.ps1` génère toujours `test-report.xml` via `pytest --junitxml=test-report.xml`.
- `scripts/run_tests.ps1` génère toujours `ruff-report.txt`, même si Ruff est indisponible ou retourne un code différent de zéro.
- `scripts/verify_release_zip.ps1` vérifie maintenant explicitement `test-report.xml` et `ruff-report.txt`.
- Les workflows utilisent `if-no-files-found: error` pour éviter un build vert avec fichiers manquants.
- Les artefacts `release-windows`, `nightops-portable` et les artefacts QA incluent désormais `test-report.xml` et `ruff-report.txt`.
