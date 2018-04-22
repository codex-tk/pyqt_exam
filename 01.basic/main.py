#-*- coding: utf-8 -*-

import sys

from Basic import Basic
from WidgetFromUI import WidgetFromUI

from PyQt5 import QtWidgets
from PyQt5 import QtGui


if __name__ == "__main__":
    print("01.basic")
    app = QtWidgets.QApplication(sys.argv)
    form = WidgetFromUI()
    sys.exit( app.exec() )