#-*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt

class Lambda(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.label=QLabel()
        self.slider=QSlider(Qt.Horizontal)
        self.setWindowTitle("LabelSlide")
        box_layout=QBoxLayout(QBoxLayout.TopToBottom,parent=self)
        self.setLayout(box_layout)
        box_layout.addWidget(self.label)
        box_layout.addWidget(self.slider)
        self.slider.valueChanged.connect(
            lambda v : self.label.setText(str(v)))