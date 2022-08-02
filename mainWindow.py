from PySide6 import QtGui, QtWidgets, QtCore
import pyqtgraph as pg
import numpy as np
# import time

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SignalFromNoise')

        # Виджеты
        win = QtWidgets.QWidget()
        startBtn = QtWidgets.QRadioButton('Start')
        stopBtn = QtWidgets.QRadioButton('Stop')
        self.plt = pg.PlotWidget(background='#04005f')
        grp = QtWidgets.QGroupBox('Manage')

        # Макеты
        layout = QtWidgets.QGridLayout()
        layoutGrp = QtWidgets.QVBoxLayout()

        # Настройка отображения
        self.setCentralWidget(win)

        win.setLayout(layout)

        layoutGrp.addWidget(startBtn)
        layoutGrp.addWidget(stopBtn)

        grp.setLayout(layoutGrp)

        stopBtn.setChecked(True)
        stopBtn.setCheckable(True)

        layout.addWidget(grp, 1, 0, 3, 1)
        layout.addWidget(self.plt, 0, 1, 3, 1)

        self.plt.setXRange(-0.5, 0.5)
        self.plt.setYRange(0, 1.5)

        self.plt.setLabel('left',text = 'Y position (m)')
        self.plt.setLabel('bottom', text= 'X position (m)')
        self.plt.showGrid(x=True, y=True)

        # Указатель на новый график с точками
        self.new_points = self.plt.plot([], [], pen=None, symbol='o')

        # Таймер
        self.timer = QtCore.QTimer()
        self.timer.setInterval(16)
        self.timer.timeout.connect(self.updatePlot)

        # Сигналы на продолжение и приостановку генерации
        startBtn.clicked.connect(self.timer.start)
        stopBtn.clicked.connect(self.timer.stop)

    # Обновление графика
    def updatePlot(self):
        self.x = np.random.uniform(-0.5, 0.5, 24)
        self.y = np.random.uniform(0, 1.5, len(self.x))

        self.new_points.setData(self.x, self.y)
