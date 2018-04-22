#-*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets

from DialSlider import DialSlider
from Lambda import Lambda

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = Lambda()
    form.show()
    sys.exit(app.exec())
    