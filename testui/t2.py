#-*-coding:utf-8-*-
#-*-coding:utf-8-*-
# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a bit
more complicated window layout using
the QGridLayout manager.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication,QPushButton)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        title = QLabel('question')
        author = QLabel('documentation')



        queEdit = QLineEdit()

        quefind = QPushButton('quefind',self)
        docEdit = QTextEdit()

        docfind=QPushButton('docfind',self)


        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title,1,0)
        grid.addWidget(queEdit,1,1)

        grid.addWidget(quefind,2,0)

        grid.addWidget(author, 3, 0)
        grid.addWidget(docEdit, 3, 1)

        grid.addWidget(docfind, 4, 0)

        quefind.clicked.connect(self.buttonClicked)
        docfind.clicked.connect(self.buttonClicked)

        self.setLayout(grid)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Review')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        textboxValue = self.textbox.text()
        if sender.setWindowIconText()=="quefind":
            print('sha')
    def findque(self):
        print(self.queEdit.text())

    def finddoc(self):
        print(self.docEdit.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())