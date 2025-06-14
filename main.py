# main.py

from biblioteca.cli import main as cli_main
from biblioteca.gui import iniciar_interface

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        cli_main()
    else:
        iniciar_interface()
