import typing
from PyQt6 import QtCore
from  PyQt6.QtWidgets import QMainWindow, QWidget, QTextEdit, QLineEdit, QPushButton, QApplication
import sys
import openai 


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        self.chat_box = QTextEdit(self)
        self.chat_box.setGeometry(10, 10, 480, 320)
        self.chat_box.setReadOnly(True)



        self.input_box = QLineEdit(self)
        self.input_box.setGeometry(10, 340, 480, 35)


        self.button = QPushButton('Submit', self)
        self.button.setGeometry(500, 340, 100, 40)

        self.show()
    

class Chatbot:
    def __init__(self):
        openai.api_key = "xxxxxxxxxxxx"

    def receive_response(self, user_input):
        response = openai.Completion.create(
            engine = 'text-davinci-003',   #open ai model
            prompt = user_input,
            max_tokens = 4000,  #returns longer answers
            temperature = 0.5 #accuracy of answers

        ).choices[0].message.content
        return response

        
if __name__ == "__main__":
    Chatbot = Chatbot()
    response = Chatbot.receive_response('tell me a joke')
    print(response)

app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
    