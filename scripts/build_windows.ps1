$ErrorActionPreference = "Stop"
./scripts/run_tests.ps1
python -m PyInstaller packaging/pyinstaller/nightops_hotel.spec
