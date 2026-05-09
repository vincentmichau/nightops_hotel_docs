# Correction PyInstaller SPECPATH

Erreur corrigée :

```text
ERROR: script '...\packaging\pyinstaller\src\nightops_hotel\cli.py' not found
```

Cause : dans le fichier `.spec`, `Path.cwd()` était interprété par PyInstaller comme le dossier du spec (`packaging/pyinstaller`) au lieu de la racine du dépôt. Le chemin relatif `src/nightops_hotel/cli.py` devenait donc `packaging/pyinstaller/src/nightops_hotel/cli.py`.

Correction : le spec utilise maintenant la variable PyInstaller `SPECPATH` :

```python
spec_dir = Path(SPECPATH).resolve()
project_root = spec_dir.parent.parent
src_root = project_root / "src"
entrypoint = src_root / "nightops_hotel" / "cli.py"
```

Résultat attendu : PyInstaller doit trouver `src/nightops_hotel/cli.py`, produire un `.exe`, puis générer `nightops-portable.zip`.
