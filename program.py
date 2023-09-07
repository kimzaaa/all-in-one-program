from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import subprocess


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("all in one")
        self.setGeometry(700, 350, 600, 400)

        self.UiComponents()
        self.show()

    def UiComponents(self):
        button = QPushButton("Smart Notes", self)
        button2 = QPushButton("Calculator", self)
        button3 = QPushButton("Krixt Browser", self)
        button4 = QPushButton("Tic Tac Toe", self)
        button5 = QPushButton("Snake", self)

        button.setGeometry(50, 25, 100, 100)
        button2.setGeometry(150, 25, 100, 100)
        button3.setGeometry(250, 25, 100, 100)
        button4.setGeometry(350, 25, 100, 100)
        button5.setGeometry(450, 25, 100, 100)

        button.clicked.connect(self.smartnotes)
        button2.clicked.connect(self.calc)
        button3.clicked.connect(self.browser)
        button4.clicked.connect(self.tictactoe)
        button5.clicked.connect(self.snake)

    # action method
    def smartnotes(self):
        subprocess.run(["python", "smartnotes.py"])

    def calc(self):
        subprocess.run(["python", "calc.py"])

    def browser(self):
        subprocess.run(["python", "owser.py"])

    def tictactoe(self):
        subprocess.run(["python", "ictactow.py"])

    def snake(self):
        subprocess.run(["python", "snake.py"])


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
