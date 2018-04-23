#-*- coding: utf-8 -*-

from PyQt5.QtChart import *
from PyQt5 import QtWidgets
from PyQt5 import Qt
from PyQt5.QtGui import QPainter

class BarChartExample(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.init_charts()

    def init_charts(self):
        set0 = QBarSet("Jane")
        set1 = QBarSet("John")
        set0.append(1)
        set0.append(2)
        set0.append(3)
        set1.append(5)
        set1.append(1)
        set1.append(4)

        series = QBarSeries()
        series.append(set0)
        series.append(set1)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("SampleBar")
        chart.setAnimationOptions(QChart.SeriesAnimations)
        
        axis = QBarCategoryAxis()
        axis.append(["1" , "2" , "3"])
        
        chart.createDefaultAxes()
        chart.setAxisX(axis,series)

        view = QChartView(chart)
        view.setRenderHint(QPainter.Antialiasing)

        layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.TopToBottom,parent=self)
        self.setLayout(layout)
        layout.addWidget(view)

        self.resize(420,300)
        self.show()
