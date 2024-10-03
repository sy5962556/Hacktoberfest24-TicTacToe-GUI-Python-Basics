from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QPalette, QColor
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        self.player_turn = True  # Player 1 starts
         


        uic.loadUi('Tic_Tac_Toe_UI.ui', self)

        # Adding the widgets to the file
        self.pushButton_1 = self.findChild(QPushButton, 'pushButton')
        self.pushButton_2 = self.findChild(QPushButton, 'pushButton_2')
        self.pushButton_3 = self.findChild(QPushButton, 'pushButton_3')
        self.pushButton_4 = self.findChild(QPushButton, 'pushButton_4')
        self.pushButton_5 = self.findChild(QPushButton, 'pushButton_5')
        self.pushButton_6 = self.findChild(QPushButton, 'pushButton_6')
        self.pushButton_7 = self.findChild(QPushButton, 'pushButton_7')
        self.pushButton_8 = self.findChild(QPushButton, 'pushButton_8')
        self.pushButton_9 = self.findChild(QPushButton, 'pushButton_9')
        self.label = self.findChild(QLabel, 'label')
        self.newGameButton = self.findChild(QPushButton, 'pushButton_10')

        # Connecting the buttons
        self.pushButton_1.clicked.connect(lambda: self.PushingButton(self.pushButton_1))
        self.pushButton_2.clicked.connect(lambda: self.PushingButton(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.PushingButton(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: self.PushingButton(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.PushingButton(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.PushingButton(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda: self.PushingButton(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda: self.PushingButton(self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda: self.PushingButton(self.pushButton_9))
        self.newGameButton.clicked.connect(self.NewGame)

        # Set the label to display the first turn message
        self.label.setText("Player 1 (X) turn")

        
        self.show()
        self.newGameButton.hide() # Initially hide the new game button


    # New Game clears the whole Board
    def NewGame(self):
        button_list = [
            self.pushButton_1, self.pushButton_2, self.pushButton_3,
            self.pushButton_4, self.pushButton_5, self.pushButton_6,
            self.pushButton_7, self.pushButton_8, self.pushButton_9
        ]
        for button in button_list:
            button.setText('')  # Clear the text
            button.setEnabled(True)  # Ensure all buttons are enabled
            # Reset the button color to default
            palette = button.palette()
            palette.setColor(QPalette.Button, QColor(240, 240, 240))  # Default color, adjust as needed
            button.setPalette(palette)
            button.setAutoFillBackground(False)
        
        self.label.setText('X\'s turn')
        self.newGameButton.hide()  # Hide the new game button after resetting

    # Check button checks if X's is winning or O's is winning
    def Check(self):
        winning_combinations = [
            [self.pushButton_1, self.pushButton_2, self.pushButton_3],
            [self.pushButton_4, self.pushButton_5, self.pushButton_6],
            [self.pushButton_7, self.pushButton_8, self.pushButton_9],
            [self.pushButton_1, self.pushButton_4, self.pushButton_7],
            [self.pushButton_2, self.pushButton_5, self.pushButton_8],
            [self.pushButton_3, self.pushButton_6, self.pushButton_9],
            [self.pushButton_1, self.pushButton_5, self.pushButton_9],
            [self.pushButton_3, self.pushButton_5, self.pushButton_7]
        ]
        
        for combination in winning_combinations:
            text1 = combination[0].text()
            text2 = combination[1].text()
            text3 = combination[2].text()
            
            if text1 != '' and text1 == text2 == text3:
                for btn in combination:
                    palette = btn.palette()
                    palette.setColor(QPalette.Button, QColor(0, 255, 0))
                    btn.setPalette(palette)
                    btn.setAutoFillBackground(True)
                
                self.DisableButtons()
                self.newGameButton.show()
                self.label.setText(f"{text1} wins!")
                return
        
        all_filled = all(btn.text() != '' for btn in [
            self.pushButton_1, self.pushButton_2, self.pushButton_3,
            self.pushButton_4, self.pushButton_5, self.pushButton_6,
            self.pushButton_7, self.pushButton_8, self.pushButton_9
        ])
        
        if all_filled:
            self.label.setText("It's a draw!")
            self.newGameButton.show()

    def DisableButtons(self):
        button_list = [
            self.pushButton_1, self.pushButton_2, self.pushButton_3,
            self.pushButton_4, self.pushButton_5, self.pushButton_6,
            self.pushButton_7, self.pushButton_8, self.pushButton_9
        ]
        
        for button in button_list:
            button.setEnabled(False)

            # Reaction when you push Buttons
    def PushingButton(self, btn):
        if btn.text() == "":
            # Player 1's turn (X)
            if self.player_turn:
                btn.setText("X")
                self.label.setText("Player 2's turn (O)")
            # Player 2's turn (O)
            else:
                btn.setText("O")
                self.label.setText("Player 1's turn (X)")
            
            # Toggle the turn
            self.player_turn = not self.player_turn
            
            btn.setEnabled(False)
            self.Check()


app = QApplication(sys.argv)


UIWindow = UI()

app.exec_()
