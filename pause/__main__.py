import sys
import runpy
import code

RESET = "\033[0m"
LGREEN = "\033[92m"
LWHITE = "\033[97m"

class SilentInteractiveConsole(code.InteractiveConsole):
    def interact(self, banner=None, exitmsg=None):
        exitmsg = ""
        super().interact(banner=banner, exitmsg=exitmsg if exitmsg is not None else '')

def help():
    print("uso: p1inter <modulo.py>", file=sys.stderr)

def main():
    if len(sys.argv) < 2:
        help()
        sys.exit(1)

    py_module = sys.argv[1]
    module_globals = runpy.run_path(py_module)
    #code.interact(local=module_globals)
    console = SilentInteractiveConsole(locals=module_globals)
    banner = f"{LWHITE}=== {py_module} executado e pausado{RESET}"
    exitmsg = ""
    console.interact(banner, exitmsg)


if __name__ == '__main__':
    main()
