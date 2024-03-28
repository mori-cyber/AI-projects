# This Python file uses the following encoding: utf-8
import sys
import os


from PySide6.QtWidgets import QApplication, QWidget
# from PySide2.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class Test23(QWidget):
    def __init__(self):
        super(Test23, self).__init__()
        loader = QUiLoader()
        self.m =1
        self.ui=loader.load("form.ui")
        self.ui.show()
        self.ui.btn_sum.clicked.connect(self.sum)
        self.ui.btn_sub.clicked.connect(self.sub)
        self.ui.btn_equal.clicked.connect(self.equal)
        self.ui.btn_1.clicked.connect(self.num1)
        self.ui.btn_2.clicked.connect(self.num2)
        self.ui.btn_3.clicked.connect(self.num3)
        self.ui.btn_4.clicked.connect(self.num4)
        self.ui.btn_5.clicked.connect(self.num5)
        self.ui.btn_6.clicked.connect(self.num6)
        self.ui.btn_7.clicked.connect(self.num7)
        self.ui.btn_8.clicked.connect(self.num8)
        self.ui.btn_9.clicked.connect(self.num9)
        self.ui.btn_0.clicked.connect(self.num0)
        self.ui.btn_point.clicked.connect(self.point)
        self.ui.btn_mul.clicked.connect(self.mul)
        self.ui.btn_DIV.clicked.connect(self.DIV)
        self.ui.btn_pow.clicked.connect(self.pow)
        self.ui.btn_per.clicked.connect(self.per)
        self.ui.btn_c.clicked.connect(self.c)
    def num1(self):
        t=self.ui.tb1.text()
        t=t+'1'
        self.ui.tb1.setText(t)
    def num2(self):
        t = self.ui.tb1.text()
        t = t + '2'
        self.ui.tb1.setText(t)

    def num3(self):
        t = self.ui.tb1.text()
        t = t + '3'
        self.ui.tb1.setText(t)


    def num4(self):
        t = self.ui.tb1.text()
        t = t + '4'
        self.ui.tb1.setText(t)

    def num5(self):
        t = self.ui.tb1.text()
        t = t + '5'
        self.ui.tb1.setText(t)


    def num6(self):
        t = self.ui.tb1.text()
        t = t + '6'
        self.ui.tb1.setText(t)

    def num7(self):
        t = self.ui.tb1.text()
        t = t + '7'
        self.ui.tb1.setText(t)

    def num8(self):
        t = self.ui.tb1.text()
        t = t + '8'
        self.ui.tb1.setText(t)

    def num9(self):
        t = self.ui.tb1.text()
        t = t + '9'
        self.ui.tb1.setText(t)

    def num0(self):
        t = self.ui.tb1.text()
        t = t + '0'
        self.ui.tb1.setText(t)

    def point(self):
        t = self.ui.tb1.text()
        t = t + '.'
        self.ui.tb1.setText(t)

    def mul(self):
        self.op = '*'
        self.a = int(self.ui.tb1.text())
        self.ui.tb1.clear()

    def DIV(self):
        self.op = '/'
        self.a = int(self.ui.tb1.text())
        self.ui.tb1.clear()

    def per(self):
        self.op = '%'
        self.a = int(self.ui.tb1.text())
        self.ui.tb1.clear()

    def c(self):
        self.op = 'C'
        # self.a = int(self.ui.tb1.text())
        self.ui.tb1.clear()



    def equal(self):

        self.b=int(self.ui.tb1.text())

        if self.op == '+':
            result =self.a + self.b
        elif self.op == '-':
            result=self.a - self.b
        elif self.op == '*':
            result = self.a * self.b
        elif self.op == '/':
            result = self.a / self.b
        elif self.op == '%':
            result = self.a*0.01
        # elif self.op =='C':
        #     result =self.ui.tb1.clear()
        elif self.op == 'pow':
            i=0
            for i in range(self.b):
                self.m = self.m * self.a
                i += 1
            result = self.m
        self.ui.tb1.setText(str(result))


    def sum(self):
        self.op ='+'
        self.a=int(self.ui.tb1.text())
        self.ui.tb1.clear()
    def sub(self):
            self.op = '-'
            self.a = int(self.ui.tb1.text())
            self.ui.tb1.clear()
    def pow(self):
        self.op = 'pow'
        self.a = int(self.ui.tb1.text())
        self.ui.tb1.clear()


if __name__ == "__main__":
    app = QApplication([])
    window = Test23()
    # widget.show()
    sys.exit(app.exec_())
