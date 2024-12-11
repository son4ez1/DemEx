from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication
)
from PyQt5.QtGui import QPixmap, QIcon
import sys

from pages.WelcomeScreen import WelcomeScreen

app = QApplication(sys.argv)

welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)

icon = QIcon()
icon.addPixmap(QPixmap("media/logo.png"), QIcon.Normal, QIcon.Off) 
widget.setWindowIcon(icon)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("You close")