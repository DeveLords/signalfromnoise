import chunk
from PySide6 import QtWidgets
from PySide6 import QtCore

import pyqtgraph as pg
import numpy as np

class waveformWidget(QtWidgets.QWidget):
    def __init__(self, namePlot: str):
        super().__init__()

        # Значение для левой и правой границы x
        self.leftX = 0
        self.rightX = 10

        # Параметры графика
        self.waveform = pg.PlotWidget(title=namePlot, background="#efefef")
        self.waveform.showGrid(y=True)
        self.waveform.setLabel('bottom', 'time', 's')
        self.waveform.setYRange(-1, 1)
        self.waveform.setXRange(self.leftX, self.rightX, padding= 0)

        # Настройка макета
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.waveform, 0, 0)
        self.setLayout(layout)

        # Параметры данных
        self.chunkSize = 100
        self.maxChunks = 15
        self.dataScroll = np.array([[0,0]])
        # self.dataScroll = np.empty((self.chunkSize+1, 2))
        # self.curve = self.waveform.plot(self.data, pen='#000000')
        self.curves = []

        # Указатель на последний элемент при заполнении массива
        self.ptr = 0

    # Очистка графика от данных, точка отсчета (0, 0)
    def refreshWaveform(self):
        self.ptr = 0
        self.leftX = 0
        self.rightX = 10
        self.waveform.clear()
        self.curves.clear()
        self.dataScroll = np.array([[0,0]])
        self.waveform.setYRange(-1, 1)
        self.waveform.setXRange(0, 10)

    # Обновление графика одиночной парой данных. В аргументы передается пара значений x и y.
    # def updateWaveformBySingle(self, singleData):
    #     # print(self.ptr)
    #     if self.ptr < self.chunkSize:
    #         if self.ptr != 0:
    #             self.data = np.append(self.data, [[singleData[0],
    #                                                singleData[1]]], axis=0)
    #         else:
    #             self.data[self.ptr, 0] = singleData[0]
    #             self.data[self.ptr, 1] = singleData[1]
    #         self.ptr += 1
    #     else:
    #         self.data[:-1, 0] = self.data[1:, 0]
    #         self.data[:-1, 1] = self.data[1:, 1]
    #         self.data[-1, 0] = singleData[0]
    #         self.data[-1, 1] =  singleData[1]
    #     self.curve.setData(x=self.data[:, 0], y=self.data[:, 1])

    # Новая функция обновления графика
    def updateWaveformByScroll(self, singleData):
        # print(self.ptr)
        if self.ptr > 200:
            self.leftX += 0.05
            self.rightX += 0.05
            self.waveform.setXRange(self.leftX , self.rightX, padding= 0)
        i = self.ptr % self.chunkSize
        if i == 0:
            curve = self.waveform.plot(pen='#000000')
            self.curves.append(curve)
            last = self.dataScroll[-1]
            self.dataScroll = np.empty((self.chunkSize+1, 2))
            self.dataScroll[0] = last
            while len(self.curves) > self.maxChunks:
                c = self.curves.pop(0)
                self.waveform.removeItem(c)
        else:
            curve = self.curves[-1]
        self.dataScroll[i+1, 0] = singleData[0]
        self.dataScroll[i+1, 1] = singleData[1]
        curve.setData(x=self.dataScroll[:i+2, 0], y=self.dataScroll[:i+2, 1])
        self.ptr += 1