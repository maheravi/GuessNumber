# This Python file uses the following encoding: utf-8
import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
import random


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.setWindowTitle("Guess Number")
        self.guess = random.randint(0, 30)
        self.wins = 0
        self.f = 5
        self.ui.check.clicked.connect(self.Play)
        self.ui.newgame.clicked.connect(self.New)
        self.ui.show()

    def Play(self):
        user_guess = int(self.ui.guess.text())
        print(user_guess)
        if self.guess == user_guess:
            self.guess = random.randint(0, 30)
            self.wins += 1
            self.ui.score.setText(str(self.wins))
            msg_box = QMessageBox()
            msg_box.setText("آفرین درست حدس زدی")
            msg_box.exec_()

        elif user_guess < self.guess:
            self.f -= 1
            self.ui.score.setText(str(self.f))
            msg_box = QMessageBox()
            msg_box.setText("برو بالاتر")
            msg_box.exec_()

        elif user_guess > self.guess:
            self.f -= 1
            self.ui.score.setText(str(self.f))
            msg_box = QMessageBox()
            msg_box.setText("بیا پایین تر")
            msg_box.exec_()

        if self.f <= 0:
            msg_box = QMessageBox()
            msg_box.setText(" نتونستی حدس بزنی " + str(self.guess))
            msg_box.exec_()
            self.New()

    def New(self):
        self.guess = random.randint(0, 30)
        self.f = 5
        self.ui.score.setText(str(self.f))


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    # window.show()
    sys.exit(app.exec_())
