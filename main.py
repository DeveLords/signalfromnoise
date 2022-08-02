from PySide6.QtWidgets import QApplication
# import pyqtgraph.examples
from mainWindow import MainWindow
import sys

def main():
    # Примеры pyqtgraph
    # pyqtgraph.examples.run()
    app = QApplication([])
    win = MainWindow()
    win.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()