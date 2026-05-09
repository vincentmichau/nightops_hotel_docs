# NightOps Hotel Documents 15.15.0-github-full-reload-production

Version complète pour rechargement total du dépôt GitHub.

## Objectif permanent
NightOps Hotel Documents est une application Windows portable destinée à la réception / night audit. L'application doit importer un XML Opera Cloud, normaliser les données réception, générer des documents hôtel via templates, produire des exports PDF avec WeasyPrint, Excel et DOCX, permettre l'impression, offrir un mode secours, respecter la RGPD avec rétention 30 jours, et rester simple pour un utilisateur néophyte.

## Architecture
```text
Controller -> Services -> Repositories -> DAO Factory -> SQLite
Views -> messages et parcours UX uniquement
```

## Démarrage local
```powershell
python -m venv .venv
. .venv/Scripts/Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
python -m pytest -q
python -m compileall src
python -m nightops_hotel --demo
```

## Build Windows portable
```powershell
./scripts/run_tests.ps1
./scripts/build_windows.ps1
./scripts/make_release.ps1
```

Résultat attendu : `nightops-portable.zip`.
