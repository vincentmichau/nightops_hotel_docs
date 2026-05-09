# Correction PyInstaller dist introuvable

Erreur corrigée : le script attendait `dist/nightops` ou `dist/nightops.exe`, mais PyInstaller terminait sans produire cette sortie attendue car le spec pouvait être vide ou invalide.

Corrections :

- `packaging/pyinstaller/nightops_hotel.spec` remplacé par un spec réel ;
- `src/nightops_hotel/cli.py`, `__main__.py`, `app.py` garantis ;
- `build_windows.ps1` nettoie `build/` et `dist/`, lance PyInstaller, affiche `dist`, cherche tout `.exe`, puis compresse la sortie réelle ;
- `verify_release_zip.ps1` vérifie que `nightops-portable.zip` existe et n'est pas vide.
