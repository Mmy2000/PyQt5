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
btn = QPushButton('login' , window)
btn.move(200,200)
btn.resize(200,60)
btn.setToolTip('Press to print')

def button_clicked():
    print('Button Clicked')

btn.clicked.connect(button_clicked)

window.show()
## Main Loop
app.exec_()
