from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip
from PyQt5.QtGui import QFont
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Абоба")
        self.setFixedSize(900, 600)

        button = QPushButton("Запустить ядерные боеголовки", self)
        button.resize(button.sizeHint())
        button.move(50, 50)

        QToolTip.setFont(QFont('SansSerif', 10))

        self.show()


def application():
    app = QApplication(sys.argv)

    mw = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()