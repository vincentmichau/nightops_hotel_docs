# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path

block_cipher = None
project_root = Path.cwd()

_datas = []
for item in ["README.md", "CHANGELOG.md", "LICENSE.txt", "VALIDATION_UPLOAD_XML.json"]:
    if (project_root / item).exists():
        _datas.append((item, "."))
for folder in ["docs", "templates", "assets", "examples"]:
    if (project_root / folder).exists():
        _datas.append((folder, folder))

a = Analysis(
    ["src/nightops_hotel/cli.py"],
    pathex=[str(project_root), str(project_root / "src")],
    binaries=[],
    datas=_datas,
    hiddenimports=["nightops_hotel"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="nightops",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name="nightops",
)
