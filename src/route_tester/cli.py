"""Console entry point.

Parses the command line and starts the graphical application. Phase 2 will extend the
parser with a prefill option so an agent can hand the app a ready-to-send request.
"""

import argparse
import sys

from route_tester import __version__


def build_parser() -> argparse.ArgumentParser:
    """Build the command line parser for the `route-tester` executable."""
    parser = argparse.ArgumentParser(
        prog="route-tester",
        description="A simple, agent-drivable HTTP route testing client.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"route-tester {__version__}",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the application. Returns the process exit code."""
    build_parser().parse_args(argv)

    # Imported lazily so that `--version` and `--help` do not require a display.
    from PySide6.QtWidgets import QApplication

    from route_tester.gui.main_window import MainWindow

    app = QApplication(sys.argv[:1])
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
