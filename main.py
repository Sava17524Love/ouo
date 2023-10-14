from PyQt5.QtWidgets import QApplication

from random import  choice, shuffle
from time import sleep

app = QApplication([])

from qwq import *
from ууу import *

class Question
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3)
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_afk = 0
        self.count_right = 0
    def got_right(self):
        self.count_afk += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_afk += 1
q1 = Question('У виразі (50 - 1) + (21 - 20) відповідь буде', '50', '1', '49', '20')
q2 = Question('У виразі 56 - (90 - 80) + 2 відповідь буде', '48', '10', '44', '84')
q3 = Question('У виразі 65 + (34 - 30) - 60 третьою дією має бути', '69 - 60', '65 + 4', '34 - 30', '65 - 60')
q4 = Question()
q5 = Question()
q6 = Question()
q7 = Question()
q8 = Question()
q9 = Question()
q10 = Question()

radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

def menu_generation():
    menu_win.show()
    window.hide()
btn_menu.clicked.connect(menu_generation)

def back_menu():
    menu_win.hide()
    window.show()
btn_back.clicked.connect(back_menu)

window.show()
app.exec_()

