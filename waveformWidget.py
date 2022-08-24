from cmath import sin
from PySide6 import QtWidgets
from PySide6 import QtCore

import pyqtgraph as pg
import numpy as np

class waveformWidget(QtWidgets.QWidget):
    def __init__(self, namePlot: str):
        super().__init__()

        # Параметры графика
        self.waveform = pg.PlotWidget(title=namePlot, background="#efefef")
        self.waveform.showGrid(x=True, y=True)
        self.waveform.setLabel('bottom', 'time', 's')
        self.waveform.setLabel('left', 'Phase', 'radian')
        self.waveform.setYRange(-10, 10)

        # Настройка макета
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.waveform, 0, 0)
        self.setLayout(layout)

        # Параметры данных
        self.chunkSize = 100
        self.data = np.array([[0,0]])
        self.curve = self.waveform.plot(self.data, pen='#000000')

        # Указатель на последний элемент при заполнении массива
        self.ptr = 0

    # Очистка графика от данных, точка отсчета (0, 0)
    def refreshWaveform(self):
        self.ptr = 0
        self.waveform.clear()
        self.curve = self.waveform.plot(self.data, pen='#000000')
        self.data = self.data = np.array([[0,0]])
        self.curve.setPos(0, 0)

    # Обновление графика одиночной парой данных. В аргументы передается пара значений x и y.
    def updateWaveformBySingle(self, singleData):
        if self.ptr < self.chunkSize:
            if self.ptr != 0:
                self.data = np.append(self.data, [[singleData[0],
                                                   singleData[1]]], axis=0)
            else:
                self.data[self.ptr, 0] = singleData[0]
                self.data[self.ptr, 1] = singleData[1]
            self.ptr += 1
        else:
            self.data[:-1, 0] = self.data[1:, 0]
            self.data[:-1, 1] = self.data[1:, 1]
            self.data[-1, 0] = singleData[0]
            self.data[-1, 1] =  singleData[1]
        self.curve.setData(x=self.data[:, 0], y=self.data[:, 1])
