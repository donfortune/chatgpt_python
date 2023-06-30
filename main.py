import typing
from PyQt6 import QtCore
from  PyQt6.QtWidgets import QMainWindow, QWidget, QTextEdit, QLineEdit, QPushButton, QApplication
import sys


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        self.chat_box = QTextEdit(self)
        self.input_box = QLineEdit(self)
        self.button = QPushButton('Submit', self)

        self.show()
    

class Chatbot:
    pass


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
    