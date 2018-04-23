#-*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from BarChartExample import BarChartExample

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = BarChartExample()
    sys.exit(app.exec())
    