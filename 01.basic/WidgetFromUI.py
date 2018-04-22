#-*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot

class WidgetFromUI( QtWidgets.QDialog ):
    def __init__( self ):
        super().__init__()
        self.ui = uic.loadUi("01.basic/WidgetFromUI.ui" , self )
        self.show()

    @pyqtSlot()
    def slot_first( self ):
        self.ui.label.setText("First")
    
    @pyqtSlot()
    def slot_second( self ):
        self.ui.label.setText("Second")