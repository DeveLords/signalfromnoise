import sys
import argparse

from PySide6.QtWidgets import QApplication
# import pyqtgraph.examples
from vitalSignsWindow import vitalSignsWindow
from radarWindow import RadarWindow


def main(debug_mode=None):
    # Примеры pyqtgraph
    # pyqtgraph.examples.run()
    app = QApplication([])
    if debug_mode.debug_radar:
        win = RadarWindow()
    elif debug_mode.debug_vital:
        win = vitalSignsWindow()
    else:
        win = vitalSignsWindow()
    win.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug-radar', action='store_true', help='debug mode for radar')
    parser.add_argument('--debug-vital', action='store_true', help='debug mode for vital signs radar')
    args = parser.parse_args()
    main(args)