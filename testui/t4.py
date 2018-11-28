#-*-coding:utf-8-*-
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QLineEdit, QAction, QMessageBox


def correct(word):
    print("shijie")


class Line(QDialog):

    def Ui(self):
        self.line = QLineEdit(self)
        self.line.move(20,20)
        action = QAction(self)
        action.setIcon(QIcon('check.ico'))
        action.triggered.connect(self.Check)
        self.line.addAction(action,QLineEdit.TrailingPosition)

    def Check(self):
        word = self.line.text()
        if correct(word) != word:
            QMessageBox.information(self,'提示信息','你或许想要表达的单词是：'+correct(word))
        else:
            QMessageBox.information(self,'提示信息','你填写的单词是：'+word)