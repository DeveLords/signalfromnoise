from platform import freedesktop_os_release
import numpy as np

from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtGui

from waveformWidget import waveformWidget

FONT_PARAMETERS = ('Arial', 20)

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
        pauseBtn = QtWidgets.QPushButton("Pause")
        pauseBtn.setEnabled(False)
        settingsBtn = QtWidgets.QPushButton("Settings")
        refreshBtn = QtWidgets.QPushButton("Refresh")

        breathingRateLabel = QtWidgets.QLabel("Breating rate")
        heartRateLabel = QtWidgets.QLabel("Heart rate")

        breathingRateLabel.setAlignment(QtCore.Qt.AlignCenter)
        heartRateLabel.setAlignment(QtCore.Qt.AlignCenter)

        breathingRateLabel.setFont(QtGui.QFont(FONT_PARAMETERS[0], FONT_PARAMETERS[1]))
        heartRateLabel.setFont(QtGui.QFont(FONT_PARAMETERS[0], FONT_PARAMETERS[1]))

        self.breathingRateSigns = QtWidgets.QLabel("0")
        self.heartRateSigns = QtWidgets.QLabel("0")

        self.breathingRateSigns.setAlignment(QtCore.Qt.AlignCenter)
        self.heartRateSigns.setAlignment(QtCore.Qt.AlignCenter)

        self.breathingRateSigns.setStyleSheet("background-color: #ffffff;" +
                                         "border: 1px solid #A5A5A5;")
        self.heartRateSigns.setStyleSheet("background-color: #ffffff;" +
                                     "border: 1px solid #A5A5A5;")

        self.breathingRateSigns.setFont(QtGui.QFont(FONT_PARAMETERS[0], FONT_PARAMETERS[1]))
        self.heartRateSigns.setFont(QtGui.QFont(FONT_PARAMETERS[0], FONT_PARAMETERS[1]))

        self.freq1 = 0
        self.freq2 = 0

        # Настройка макета группы
        menageGrpLayout = QtWidgets.QVBoxLayout()
        menageGrpLayout.addWidget(startBtn)
        menageGrpLayout.addWidget(pauseBtn)
        menageGrpLayout.addWidget(stopBtn)
        menageGrpLayout.addWidget(settingsBtn)
        menageGrpLayout.addWidget(refreshBtn)

        menageGrp = QtWidgets.QGroupBox()
        menageGrp.setLayout(menageGrpLayout)

        self.waveformBreating = waveformWidget("Breating waveform")
        self.waveformHeart = waveformWidget('Heart waveform')

        centralGridLayout.addWidget(breathingRateLabel, 0, 0)
        centralGridLayout.addWidget(heartRateLabel, 0, 1)
        centralGridLayout.addWidget(self.breathingRateSigns, 1, 0)
        centralGridLayout.addWidget(self.heartRateSigns, 1, 1)
        centralGridLayout.addWidget(self.waveformBreating, 2, 0)
        centralGridLayout.addWidget(self.waveformHeart, 2, 1)
        centralGridLayout.addWidget(menageGrp, 0, 2, 3, 1)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)

        self.counterTimer = 0

        # Signals to slots
        self.timer.timeout.connect(self.updatePlots)

        startBtn.clicked.connect(self.timer.start)
        stopBtn.clicked.connect(self.timer.stop)
        refreshBtn.clicked.connect(self.refreshWaveforms)

    # Обновление графиков
    def updatePlots(self):
        x_1, freq_1 = sinSignal(2, self.counterTimer, 1.5)
        x_2, freq_2 = sinSignal(1.5, self.counterTimer, 2)
        breathData = [self.counterTimer, x_1]
        heartData = [self.counterTimer, x_2]

        self.waveformBreating.updateWaveformBySingle(breathData)
        self.waveformHeart.updateWaveformBySingle(heartData)

        self.counterTimer += 0.05
        self.breathingRateSigns.setText(str(freq_1*60))
        self.heartRateSigns.setText(str(freq_2*60))

    # Вызов очистки графиков
    def refreshWaveforms(self):
        self.waveformBreating.refreshWaveform()
        self.waveformHeart.refreshWaveform()
        self.heartRateSigns.setText('0')
        self.breathingRateSigns.setText('0')
        self.counterTimer = 0

def sinSignal(amplitude, time, freq):
    y = amplitude * np.sin(2*np.pi*freq * time)
    return y, freq
