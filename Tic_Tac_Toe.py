from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        # Load the UI file
        uic.loadUi("Tic_Tac_Toe_UI.ui",self)

        # Show the window
        self.show()

app = QApplication(sys.argv)

UIWindow = UI()

app.exec_()