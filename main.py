import typing
from PyQt6 import QtCore
from  PyQt6.QtWidgets import QMainWindow, QWidget, QTextEdit, QLineEdit, QPushButton, QApplication
import sys
import openai 


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = Chatbot()
        self.setMinimumSize(700, 500)

        self.chat_box = QTextEdit(self)
        self.chat_box.setGeometry(10, 10, 480, 320)
        self.chat_box.setReadOnly(True)



        self.input_box = QLineEdit(self)
        self.input_box.setGeometry(10, 340, 480, 35)
        self.input_box.returnPressed.connect(self.submit_request)


        self.button = QPushButton('Submit', self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.submit_request)

        self.show()

    def submit_request(self):
        user_input = self.input_box.text().strip() #accept user input 
        self.chat_box.append(f"Prompt: {user_input}")
        self.input_box.clear()

        response = self.chatbot.receive_response(user_input)
        self.chat_box.append(f"Bot: {response}")



    

class Chatbot:
    def __init__(self):
        openai.api_key = "xxxxxxxxxxxxxx"

    def receive_response(self, user_input):
        response = openai.Completion.create(
            engine='text-davinci-003',  
            prompt=user_input,
            max_tokens=4000,  
            temperature=0.5 

        ).choices[0].message.content
        return response

        

app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
    
