# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path
block_cipher = None
spec_dir = Path(SPECPATH).resolve()
project_root = spec_dir.parent.parent
src_root = project_root / "src"
entrypoint = src_root / "nightops_hotel" / "cli.py"
if not entrypoint.exists():
    raise FileNotFoundError(f"Entrée PyInstaller introuvable: {entrypoint}")
_datas = []
for item in ["README.md", "CHANGELOG.md", "LICENSE.txt", "VALIDATION_UPLOAD_XML.json"]:
    source = project_root / item
    if source.exists(): _datas.append((str(source), "."))
for folder in ["docs", "templates", "assets", "examples"]:
    source = project_root / folder
    if source.exists(): _datas.append((str(source), folder))
a = Analysis([str(entrypoint)], pathex=[str(project_root), str(src_root)], binaries=[], datas=_datas, hiddenimports=["nightops_hotel"], hookspath=[], hooksconfig={}, runtime_hooks=[], excludes=[], noarchive=False)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True, name="nightops", debug=False, bootloader_ignore_signals=False, strip=False, upx=True, console=True)
coll = COLLECT(exe, a.binaries, a.zipfiles, a.datas, strip=False, upx=True, name="nightops")
