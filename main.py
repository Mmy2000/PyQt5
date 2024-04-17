## Import Main PyQt Modules

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
window = QWidget()


window.setWindowTitle('Hello PyQt')
window.resize(600,600)
# window.move(500,500)

window.show()
## Main Loop
app.exec_()
