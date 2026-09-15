"""Application main window.

This is currently a placeholder shell: it proves the Qt stack is wired correctly and
gives the request editor, response viewer and collection tree a place to be mounted.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget

from route_tester import __version__

WINDOW_TITLE = "route_tester"
DEFAULT_SIZE = (1100, 700)


class MainWindow(QMainWindow):
    """Top-level window hosting the request/response workspace."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(WINDOW_TITLE)
        self.resize(*DEFAULT_SIZE)
        self.setCentralWidget(self._build_placeholder())
        self.statusBar().showMessage(f"route_tester {__version__}")

    def _build_placeholder(self) -> QWidget:
        """Build the temporary central widget shown until the workspace exists."""
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        message = QLabel("Workspace not implemented yet.")
        message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(message)

        return container
