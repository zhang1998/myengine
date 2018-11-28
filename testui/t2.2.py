#-*-coding:utf-8-*-

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication,QPushButton)


class Example():
    list1 = ['physic', 'chemistry']
    def __init__(self,list1):
        print(list1)
        self.p2(list1)

    def p2(self,list1):
        print('p2:'+list1[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    list1=['1','2']
    ex = Example(list1)
    print(ex.list1[0])