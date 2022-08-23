from cmath import sin
from PySide6 import QtWidgets
from PySide6 import QtCore

import pyqtgraph as pg
import numpy as np

class waveformWidget(QtWidgets.QWidget):
    def __init__(self, namePlot: str, amplitude = 1., frequency = 1.):
        super().__init__()

        # Параметры графика
        self.waveform = pg.PlotWidget(title=namePlot, background="#efefef")
        # self.waveform.setAspectLocked()
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

        self.ptr = 0
        self.counterTime = 0

        # Параметры генерации синусоидального сигнала
        self.freq = frequency
        self.amplitude = amplitude

    def refreshWaveform(self):
        self.ptr = 0
        self.counterTime = 0
        self.waveform.clear()

        self.curve = self.waveform.plot(self.data, pen='#000000')

        self.data = self.data = np.array([[0,0]])
        self.curve.setPos(0, 0)

    def updateWaveform(self):
        if self.ptr < self.chunkSize:
            if self.ptr != 0:
                self.data = np.append(self.data, [[self.counterTime,
                                                   self.sinSignal(self.amplitude,
                                                                  self.counterTime,
                                                                  self.freq)]], axis=0)
            else:
                self.data[self.ptr, 0] = self.counterTime
                self.data[self.ptr, 1] = self.sinSignal(self.amplitude,
                                                        self.counterTime,
                                                        self.freq)
        else:
            self.data[:-1, 0] = self.data[1:, 0]
            self.data[:-1, 1] = self.data[1:, 1]
            self.data[-1, 0] = self.counterTime
            self.data[-1, 1] = self.sinSignal(self.amplitude,
                                              self.counterTime,
                                              self.freq)
        self.curve.setData(x=self.data[:, 0], y=self.data[:, 1])
        self.ptr += 1
        self.counterTime += 0.05

    def sinSignal(self, amplitude, time, freq):
        y = amplitude * np.sin(2*np.pi*freq * time)
        return y