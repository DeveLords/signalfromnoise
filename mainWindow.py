from PySide6 import QtWidgets, QtCore
import pyqtgraph as pg
import numpy as np

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SignalFromNoise')

        # Виджеты
        centralWidget = QtWidgets.QWidget()
        startBtn = QtWidgets.QRadioButton('Start')
        stopBtn = QtWidgets.QRadioButton('Stop')
        self.plotRadar = pg.PlotWidget(background='#04005f')
        grp = QtWidgets.QGroupBox('Manage')

        self.plotRadar.setAspectLocked()

        self.plotRadar.addLine(x=0, pen=0.2)
        self.plotRadar.addLine(y=0, pen=0.2)
        for r in range(1, 20, 1):
            circle = QtWidgets.QGraphicsEllipseItem(-r, -r, r *2, r *2)
            circle.setPen(pg.mkPen(0.2))
            circle.setStartAngle(-480)
            circle.setSpanAngle(-1920)
            self.plotRadar.addItem(circle)
            circle = QtWidgets.QGraphicsEllipseItem(-r, -r, r *2, r *2)
            circle.setPen(pg.mkPen(0.2))
            circle.setStartAngle(-960)
            circle.setSpanAngle(-960)
            self.plotRadar.addItem(circle)

        # Макеты
        layout = QtWidgets.QGridLayout()
        layoutGrp = QtWidgets.QVBoxLayout()

        # Настройка отображения
        self.setCentralWidget(centralWidget)

        centralWidget.setLayout(layout)

        layoutGrp.addWidget(startBtn)
        layoutGrp.addWidget(stopBtn)

        grp.setLayout(layoutGrp)

        stopBtn.setChecked(True)
        stopBtn.setCheckable(True)

        layout.addWidget(grp, 0, 0)
        layout.addWidget(self.plotRadar, 0, 1)

        self.plotRadar.setXRange(-5, 5)
        self.plotRadar.setYRange(0, 10)

        self.plotRadar.setLabel('left',text = 'Y position (m)')
        self.plotRadar.setLabel('bottom', text= 'X position (m)')
        self.plotRadar.showGrid(x=True, y=True)

        # Указатель на новый график с точками
        self.new_points = self.plotRadar.plot([], [], pen=None, symbol='o')

        # Таймер
        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.updatePlot)

        # Сигналы на продолжение и приостановку генерации
        startBtn.clicked.connect(self.timer.start)
        stopBtn.clicked.connect(self.timer.stop)

    # Обновление графика
    def updatePlot(self):
        theta = np.linspace(np.pi/6, (5*np.pi)/6, 20)
        radius = np.random.uniform(0, 10, size=20)

        # Transform to cartesian and plot
        self.x = radius * np.cos(theta)
        self.y = radius * np.sin(theta)

        self.new_points.setData(self.x, self.y)
