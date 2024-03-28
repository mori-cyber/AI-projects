# This Python file uses the following encoding: utf-8
import sys
import os

from Database import Database
from Webcam import Camera
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtGui
from functools import partial


class Face_Detection(QWidget):
    def __init__(self):
        super(Face_Detection, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("basic_form.ui")
        self.ui.btn_add.clicked.connect(self.addNewUser)
        self.users = self.readMessages()
        self.length = len(self.users)
        self.ui.show()

    def readMessages(self):
        users = Database.select()
        print(users)
        for i, user in enumerate(users):
            label = QLabel()
            label.setText(user[1])

            btn = QPushButton()
            btn.setText('×')
            btn.setStyleSheet('max-width: 18px; min-height: 18px; background-color: #F05454;'
                              ' color: white; border: 0px; border-radius: 9px;')

            avatar = QPushButton()
            avatar.setStyleSheet('max-width: 70px; min-height: 70px; border: 0px; border-radius: 35px;')
            avatar.setIcon(QtGui.QIcon(f"assets/img/users/{user[4]}"))
            avatar.setIconSize(QSize(70, 70))

            self.ui.gl_personel.addWidget(avatar, i, 0, alignment=Qt.Alignment())
            self.ui.gl_personel.addWidget(label, i, 1, alignment=Qt.Alignment())
            self.ui.gl_personel.addWidget(btn, i, 2, alignment=Qt.Alignment())
            btn.clicked.connect(partial(self.deleteUser, user[0], btn, label, avatar))
        return users

    def addNewUser(self):
        self.add_new_user = AddUser(self.length)

    def deleteUser(self, id,btn, label, avatar):
        response = Database.delete(id)
        if response:
            btn.hide()
            label.hide()
            avatar.hide()
            self.msgBox("message deleted!")
        else:
            self.msgBox("Database error!")

    def msgBox(self, msg):
        msg_box = QMessageBox()
        msg_box.setText(msg)
        msg_box.exec_()
class AddUser(QWidget):
    def __init__(self, len):
        super(AddUser, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui')
        self.ui.show()
        self.ui.Cam_b.setIcon(QtGui.QIcon('camera.png'))
        self.ui.pb_add.clicked.connect(self.add)
        self.ui.Cam_b.clicked.connect(self.takePhoto)
        self.length = len
        print('self.length: ',self.length)

    def add(self):
        name = self.ui.le_name.text()
        family = self.ui.le_family.text()
        nationalcode = self.ui.le_natinalcode.text()
        birthday = self.ui.le_brith.text()

        if name != "" and nationalcode != "":
            response = Database.insert(name,family,nationalcode, birthday, self.length+1)
            if response:
                self.length += 1
                label = QLabel()
                label.setText(name)

                btn = QPushButton()
                btn.setText('×')
                btn.setStyleSheet('max-width: 18px; min-height: 18px; background-color: #F05454;'
                                  ' color: white; border: 0px; border-radius: 9px;')

                avatar = QPushButton()
                avatar.setStyleSheet('max-width: 70px; min-height: 70px; border: 0px; border-radius: 35px;')
                avatar.setIcon(QtGui.QIcon(f"imageg/{self.length-1}.jpg"))
                avatar.setIconSize(QSize(70, 70))

                widget.ui.gl_personel.addWidget(avatar, self.length, 0, alignment=Qt.Alignment())
                widget.ui.gl_personel.addWidget(label, self.length, 1, alignment=Qt.Alignment())
                widget.ui.gl_personel.addWidget(btn, self.length, 2, alignment=Qt.Alignment())
                btn.clicked.connect(partial(widget.deleteUser, self.length, btn, label, avatar))
                self.ui.close()
                self.msgBox("User added successfully!")
            else:
                self.msgBox("Database error!")
        else:
            self.msgBox("Error: feilds are empty!")

    def takePhoto(self):
        camera = Camera(self.length, self.ui.img_label)

    def msgBox(self, msg):
        msg_box = QMessageBox()
        msg_box.setText(msg)
        msg_box.exec_()
if __name__ == "__main__":
    app = QApplication([])
    widget = Face_Detection()
    sys.exit(app.exec_())
