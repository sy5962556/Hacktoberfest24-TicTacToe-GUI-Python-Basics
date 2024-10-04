from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QColorDialog
from PyQt5.QtGui import QPalette, QColor
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        self.player_turn = True  # Player 1 starts
        self.player1_color = QColor('blue')  # Default color for Player 1
        self.player2_color = QColor('red')   # Default color for Player 2 

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

        # Color selection buttons
        self.player1_color_button = self.findChild(QPushButton, 'player1_color_button')  # Add a button for Player 1 color
        self.player2_color_button = self.findChild(QPushButton, 'player2_color_button')  # Add a button for Player 2 color

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

        # Connect color buttons to select colors
        self.player1_color_button.clicked.connect(self.SelectPlayer1Color)
        self.player2_color_button.clicked.connect(self.SelectPlayer2Color)

        # Set the label to display select color message
        self.label.setText("Select colors for Player 1 and player 2")
        self.DisableButtons() # Player cannot play till both select a color
        

        self.show()
        self.newGameButton.hide() # Initially hide the new game button

    def SelectPlayer1Color(self):
        color = QColorDialog.getColor() #opens dialogue box
        if color.isValid():
            self.player1_color = color
            self.player1_color_button.setStyleSheet(f"background-color: {self.player1_color.name()};")
            self.player1_color_button.setEnabled(False) #Disable the button after selection
            if not self.player1_color_button.isEnabled() and not self.player2_color_button.isEnabled():
                self.label.setText("Player 1 (X) turn") # When both colors are selected - display message for X to play
                self.EnableButtons() #Now player can play

    def SelectPlayer2Color(self):
        color = QColorDialog.getColor() #opens dialogue box
        if color.isValid():
            self.player2_color = color
            self.player2_color_button.setStyleSheet(f"background-color: {self.player2_color.name()};")
            self.player2_color_button.setEnabled(False) #Disable the button after selection
            if not self.player1_color_button.isEnabled() and not self.player2_color_button.isEnabled():
                self.label.setText("Player 1 (X) turn") # When both colors are selected - display message for X to play
                self.EnableButtons() #Now player can play

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
        
        # Reset the player color buttons to default color
        self.player1_color_button.setStyleSheet('')  # Reset to default style (original button color)
        self.player2_color_button.setStyleSheet('')  # Reset to default style (original button color)
        

        # Re-enable color buttons for a new game
        self.player1_color_button.setEnabled(True)
        self.player2_color_button.setEnabled(True)

        #Reset game state
        self.label.setText("Select colors for Player 1 and player 2")
        self.newGameButton.hide()  # Hide the new game button after resetting
        self.player_turn = True #Reset to player 1's turn
        self.DisableButtons() # Prevent players from playing until they select colors
        
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

    def EnableButtons(self):
        buttons_list = [
            self.pushButton_1, self.pushButton_2, self.pushButton_3,
            self.pushButton_4, self.pushButton_5, self.pushButton_6,
            self.pushButton_7, self.pushButton_8, self.pushButton_9
        ]

        for button in buttons_list:
            button.setEnabled(True)

            # Reaction when you push Buttons
    def PushingButton(self, btn):
        if btn.text() == "":
            # Player 1's turn (X)
            if self.player_turn:
                btn.setText("X")
                btn.setStyleSheet(f"color: {self.player1_color.name()};")
                self.label.setText("Player 2's turn (O)")
            # Player 2's turn (O)
            else:
                btn.setText("O")
                btn.setStyleSheet(f"color: {self.player2_color.name()};")
                self.label.setText("Player 1's turn (X)")
            
            # Toggle the turn
            self.player_turn = not self.player_turn
            
            btn.setEnabled(False)
            self.Check()


app = QApplication(sys.argv)


UIWindow = UI()

app.exec_()
