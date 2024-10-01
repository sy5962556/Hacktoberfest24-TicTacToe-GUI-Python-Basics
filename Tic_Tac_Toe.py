from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        # Load the UI file

        # Adding the widgets to the file

        # Connecting the buttons

        # Show the window

    # New Game clears the whole Board
    def NewGame(self):
        pass

    # Check button checks if X's is winning or O's is winning
    def Check(self, btn):
        pass

    # Reaction when you push Buttons
    def PushingButton(self):
        pass

app = QApplication(sys.argv)

UIWindow = UI()

app.exec_()
