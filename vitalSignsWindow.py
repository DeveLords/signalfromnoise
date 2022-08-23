from PySide6 import QtWidgets
from PySide6 import QtCore

from waveformWidget import waveformWidget

class vitalSignsWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        centralGridLayout = QtWidgets.QGridLayout()
        self.setLayout(centralGridLayout)
        self.setWindowTitle("Vital Signs Monitoring")

        startBtn = QtWidgets.QPushButton("Start")
        stopBtn = QtWidgets.QPushButton("Stop")
        refreshBtn = QtWidgets.QPushButton("Refresh")

        # self.secondsLabel = QtWidgets.QLabel('Seconds')
        # self.ptr = 0
        # self.seconds = 0

        menageGrpLayout = QtWidgets.QVBoxLayout()
        menageGrpLayout.addWidget(startBtn)
        menageGrpLayout.addWidget(stopBtn)
        menageGrpLayout.addWidget(refreshBtn
                                  )
        # menageGrpLayout.addWidget(self.secondsLabel)

        menageGrp = QtWidgets.QGroupBox()
        menageGrp.setLayout(menageGrpLayout)

        self.waveformBreating = waveformWidget("Breating")
        self.waveformHeart = waveformWidget('Heart beat', 2, 0.7)

        centralGridLayout.addWidget(self.waveformBreating, 0, 0)
        centralGridLayout.addWidget(self.waveformHeart, 0, 1)
        centralGridLayout.addWidget(menageGrp, 0, 2)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)

        # Signals to slots
        self.timer.timeout.connect(self.updatePlot)

        startBtn.clicked.connect(self.timer.start)
        stopBtn.clicked.connect(self.timer.stop)
        refreshBtn.clicked.connect(self.refreshWaveforms)

    def updatePlot(self):
        self.waveformBreating.updateWaveform()
        self.waveformHeart.updateWaveform()

        # if self.ptr == 20:
        #     self.seconds += 1
        #     self.secondsLabel.setText(str(self.seconds))
        #     self.ptr = 0
        # self.ptr += 1

    def refreshWaveforms(self):
        # self.timer.stop()

        self.waveformBreating.refreshWaveform()
        self.waveformHeart.refreshWaveform()

        # self.timer.start()