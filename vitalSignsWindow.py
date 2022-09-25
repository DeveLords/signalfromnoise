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

        # Параметры
        saveDataCheck = QtWidgets.QCheckBox("Save data")
        loadConfigCheck = QtWidgets.QCheckBox("Load config file")

        plotRangeCheck = QtWidgets.QCheckBox("Plot range profile")
        plotDeplCheck = QtWidgets.QCheckBox("Plot deplacement")
        enabledPlotsCheck = QtWidgets.QCheckBox("Enable plots")
        fftBasedCheck = QtWidgets.QCheckBox("FFT_Based")

        # Запуск и остановка
        startBtn = QtWidgets.QPushButton("Start")
        stopBtn = QtWidgets.QPushButton("Stop")
        pauseBtn = QtWidgets.QPushButton("Pause")
        pauseBtn.setEnabled(False)
        settingsBtn = QtWidgets.QPushButton("Settings")
        settingsBtn.setEnabled(False)
        refreshBtn = QtWidgets.QPushButton("Refresh")

        breathingRateLabel = QtWidgets.QLabel("Breating rate")
        heartRateLabel = QtWidgets.QLabel("Heart rate")

        breathingRateLabel.setAlignment(QtCore.Qt.AlignCenter)
        heartRateLabel.setAlignment(QtCore.Qt.AlignCenter)

        breathingRateLabel.setFont(QtGui.QFont(FONT_PARAMETERS[0], FONT_PARAMETERS[1]))
        heartRateLabel.setFont(QtGui.QFont(FONT_PARAMETERS[0], FONT_PARAMETERS[1]))

        countTextEdit = QtWidgets.QLineEdit()
        brpkTextEdit = QtWidgets.QLineEdit()
        brftTextEdit = QtWidgets.QLineEdit()
        cmBreathTextEdit = QtWidgets.QLineEdit()
        thBreathTextEdit = QtWidgets.QDoubleSpinBox()

        indexTextEdit = QtWidgets.QLineEdit()
        hrpkTextEdit = QtWidgets.QLineEdit()
        hrftTextEdit = QtWidgets.QLineEdit()
        cmHeartTextEdit = QtWidgets.QLineEdit()
        thHeartTextEdit = QtWidgets.QDoubleSpinBox()

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

        # Настройка макета группы
        menageGrpLayout = QtWidgets.QVBoxLayout()
        menageGrpLayout.addWidget(startBtn)
        menageGrpLayout.addWidget(pauseBtn)
        menageGrpLayout.addWidget(stopBtn)
        menageGrpLayout.addWidget(settingsBtn)
        menageGrpLayout.addWidget(refreshBtn)

        paramsGrpLayout = QtWidgets.QVBoxLayout()
        paramsGrpLayout.addWidget(saveDataCheck)
        paramsGrpLayout.addWidget(loadConfigCheck)

        plotParamsGrpLayout = QtWidgets.QVBoxLayout()
        plotParamsGrpLayout.addWidget(plotRangeCheck)
        plotParamsGrpLayout.addWidget(plotDeplCheck)
        plotParamsGrpLayout.addWidget(enabledPlotsCheck)
        plotParamsGrpLayout.addWidget(fftBasedCheck)

        bottomParamsPlotLayout = QtWidgets.QGridLayout()
        bottomParamsPlotLayout.addWidget(QtWidgets.QLabel("Count"), 0, 0)
        bottomParamsPlotLayout.addWidget(countTextEdit, 0, 1)
        bottomParamsPlotLayout.addWidget(QtWidgets.QLabel("BR-pk"), 0, 2)
        bottomParamsPlotLayout.addWidget(brpkTextEdit, 0, 3)
        bottomParamsPlotLayout.addWidget(QtWidgets.QLabel("BR-ft"), 0, 4)
        bottomParamsPlotLayout.addWidget(brftTextEdit, 0, 5)
        bottomParamsPlotLayout.addWidget(QtWidgets.QLabel("CM Breath"), 0, 6)
        bottomParamsPlotLayout.addWidget(cmBreathTextEdit, 0, 7)
        bottomParamsPlotLayout.addWidget(QtWidgets.QLabel("TH Breath"), 0, 8)
        bottomParamsPlotLayout.addWidget(thBreathTextEdit, 0, 9)

        bottomParamsPlotLayout.addWidget(QtWidgets.QLabel("Index"), 1, 0)
        bottomParamsPlotLayout.addWidget(indexTextEdit, 1, 1)
        bottomParamsPlotLayout.addWidget(QtWidgets.QLabel("HR-pk"), 1, 2)
        bottomParamsPlotLayout.addWidget(hrpkTextEdit, 1, 3)
        bottomParamsPlotLayout.addWidget(QtWidgets.QLabel("HR-ft"), 1, 4)
        bottomParamsPlotLayout.addWidget(hrftTextEdit, 1, 5)
        bottomParamsPlotLayout.addWidget(QtWidgets.QLabel("CM Breath"), 1, 6)
        bottomParamsPlotLayout.addWidget(cmHeartTextEdit, 1, 7)
        bottomParamsPlotLayout.addWidget(QtWidgets.QLabel("TH Breath"), 1, 8)
        bottomParamsPlotLayout.addWidget(thHeartTextEdit, 1, 9)

        menageGrp = QtWidgets.QGroupBox()
        menageGrp.setLayout(menageGrpLayout)

        paramsGrp = QtWidgets.QGroupBox()
        paramsGrp.setLayout(paramsGrpLayout)

        plotParamsGrp = QtWidgets.QGroupBox()
        plotParamsGrp.setLayout(plotParamsGrpLayout)

        bottomParamsPlotGrp = QtWidgets.QGroupBox()
        bottomParamsPlotGrp.setLayout(bottomParamsPlotLayout)

        self.waveformBreating = waveformWidget("Breating waveform")
        self.waveformBreating.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.waveformHeart = waveformWidget('Heart waveform')
        self.chestDeplacement = waveformWidget('Chest Deplacement')
        self.chestDeplacement.waveform.setLabel("bottom", "frame")
        self.chestDeplacement.waveform.setLabel("left", "deplacement", "mm")
        self.rangeProfilePlt = waveformWidget('RangeProfile')
        self.rangeProfilePlt.waveform.setLabel("bottom", "range", "meter")

        centralGridLayout.addWidget(breathingRateLabel, 0, 0)
        centralGridLayout.addWidget(heartRateLabel, 0, 1)
        centralGridLayout.addWidget(self.breathingRateSigns, 1, 0)
        centralGridLayout.addWidget(self.heartRateSigns, 1, 1)
        centralGridLayout.addWidget(self.waveformBreating, 2, 0)
        centralGridLayout.addWidget(self.waveformHeart, 2, 1)
        centralGridLayout.addWidget(self.chestDeplacement, 3, 0)
        centralGridLayout.addWidget(self.rangeProfilePlt, 3, 1)
        centralGridLayout.addWidget(paramsGrp, 0, 2)
        centralGridLayout.addWidget(plotParamsGrp, 3, 2)
        centralGridLayout.addWidget(bottomParamsPlotGrp, 4, 0, 1, 2)
        centralGridLayout.addWidget(menageGrp, 1, 2, 2, 1)

        # Таймер обновления, с частотой 50 гц.
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

        # Получение данных из функции sinSignal. В данном блоке формируются данные,
        # которые будут отображаться на графиках
        y_1, freq_1 = sinSignal(.48, self.counterTimer, 4)
        y_2, freq_2 = sinSignal(.28, self.counterTimer, 3)
        y_3, _ = sinSignal(.11, self.counterTimer, 1.3)
        y_4, _ = sinSignal(.25, self.counterTimer, 1.1)

        # breathData = [self.counterTimer, y_1]
        # heartData = [self.counterTimer, y_2]

        # chestDeplacementData = [self.counterTimer, y_3]
        # rangeProfileData = [self.counterTimer, y_4]

        freq_1 = round(freq_1 * 60, 2)
        freq_2 = round(freq_2 * 60, 2)

        # Обновление верхних графиков
        self.waveformBreating.updateWaveformByScroll(self.counterTimer, y_1)
        self.waveformHeart.updateWaveformByScroll(self.counterTimer, y_2)

        # Обновление двух нижних графиков
        # self.chestDeplacement.updateWaveformByScroll(self.counterTimer, y_3)
        # self.rangeProfilePlt.updateWaveformByScroll(self.counterTimer, y_4)

        # Обновление счетчика времени для генерации данных
        self.counterTimer += 0.05

        # Обновление показаний частоты
        self.breathingRateSigns.setText(str(freq_1))
        self.heartRateSigns.setText(str(freq_2))

    # Сброс графиков
    def refreshWaveforms(self):
        self.waveformBreating.refreshWaveform()
        self.waveformHeart.refreshWaveform()
        self.chestDeplacement.refreshWaveform()
        self.rangeProfilePlt.refreshWaveform()

        self.heartRateSigns.setText('0')
        self.breathingRateSigns.setText('0')

        self.counterTimer = 0

# Генератор данных
def sinSignal(amplitude, time, freq):
    y = amplitude * np.sin(2*np.pi*freq * time)
    return y, freq
