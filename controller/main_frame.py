"""
# coding:utf-8
@Time    : 2021/07/01
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : main_frame.py
@Desc    : main_frame
@Software: PyCharm
"""
from views.mainframe import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow


class MainFrame(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(MainFrame, self).__init__()
        self.setupUi(self)
