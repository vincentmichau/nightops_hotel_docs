# Correction release-windows artifact

Le workflow `release-windows` doit produire et uploader `nightops-portable.zip`.

Le log précédent était en succès, mais il n'avait uploadé que `test-report.xml`, `ruff-report.txt` et `qa-summary.md`. Cette version force maintenant :

- l'exécution de `scripts/make_release.ps1` ;
- la vérification de `nightops-portable.zip` ;
- l'upload de `nightops-portable.zip`, `release-report.md`, `qa-summary.md`, `test-report.xml`, `ruff-report.txt`.
