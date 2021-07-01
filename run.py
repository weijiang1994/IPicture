"""
# coding:utf-8
@Time    : 2021/07/01
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : run.py
@Desc    : run
@Software: PyCharm
"""
from PyQt5.QtWidgets import QApplication
import sys
from controller.main_frame import MainFrame

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainFrame()
    win.setWindowTitle('iPicture Beta Version1.0.0')
    win.show()
    app.exec()
