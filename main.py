from PySide6.QtWidgets import QApplication
# import pyqtgraph.examples
from radarWindow import RadarWindow
import sys

def main():
    # Примеры pyqtgraph
    # pyqtgraph.examples.run()
    app = QApplication([])
    win = RadarWindow()
    win.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()