from nightops_hotel import __version__
from nightops_hotel.app import run_demo

def main(argv=None):
    argv = argv or []
    if "--version" in argv:
        print(__version__)
        return 0
    result = run_demo()
    print(result.get("message", "NightOps OK"))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
