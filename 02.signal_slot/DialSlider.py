#-*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDial
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt

class DialSlider(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.dial=QDial()
        self.slider=QSlider(Qt.Horizontal)
        self.setWindowTitle("DialSlider")
        box_layout=QBoxLayout(QBoxLayout.TopToBottom,parent=self)
        self.setLayout(box_layout)
        box_layout.addWidget(self.dial)
        box_layout.addWidget(self.slider)
        self.dial.valueChanged.connect(self.slider.setValue)
        self.slider.valueChanged.connect(self.dial.setValue)