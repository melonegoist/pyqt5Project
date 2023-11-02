# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 379)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 0, 400, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)

        self.parametrs = ("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid #000;\n"
"border-radius: 2px;\n"
"font-family: Verdana;\n"
"font-size: 25px}"
"QPushButton::hover{background-color: #be94d4}")

        self.label_result.setFont(font)
        self.label_result.setStyleSheet("background-color: #121212;\n"
"color: #fff;\n"
"padding-left: 1px")
        self.label_result.setObjectName("label_result")
        self.btn_d_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_d_1.setGeometry(QtCore.QRect(0, 313, 100, 66))
        self.btn_d_1.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"border: 1px solid #000;\n"
"border-radius: 2px;\n"
"font-family: Verdana;\n"
"font-size: 25px")
        self.btn_d_1.setObjectName("btn_d_1")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(100, 313, 100, 66))
        self.btn_0.setStyleSheet(f"{self.parametrs}")
        self.btn_0.setObjectName("btn_0")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(200, 313, 100, 66))
        self.btn_equal.setStyleSheet("background-color: #9e7bb5;\n"
"border: 1px solid #000;\n"
"border-radius: 2px;\n"
"font-family: Verdana;\n"
"font-size: 25px")
        self.btn_equal.setObjectName("btn_equal")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(300, 313, 100, 66))
        self.btn_plus.setStyleSheet("background-color: rgb(170, 85, 255);\n"
"border: 1px solid #000;\n"
"border-radius: 2px;\n"
"font-family: Verdana;\n"
"font-size: 25px")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(300, 247, 100, 66))
        self.btn_minus.setStyleSheet("border: 1px solid #000;\n"
"background-color: rgb(170, 85, 255);\n"
"border-radius: 2px;\n"
"font-family: Verdana;\n"
"font-size: 25px")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(200, 247, 100, 66))
        self.btn_3.setStyleSheet(f"{self.parametrs}")
        self.btn_3.setObjectName("btn_3")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(100, 247, 100, 66))
        self.btn_2.setStyleSheet(f"{self.parametrs}")
        self.btn_2.setObjectName("btn_2")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 247, 100, 66))
        self.btn_1.setStyleSheet(f"{self.parametrs}")
        self.btn_1.setObjectName("btn_1")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(100, 181, 100, 66))
        self.btn_5.setStyleSheet(f"{self.parametrs}")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(200, 181, 100, 66))
        self.btn_6.setStyleSheet(f"{self.parametrs}")
        self.btn_6.setObjectName("btn_6")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 181, 100, 66))
        self.btn_4.setStyleSheet(f"{self.parametrs}")
        self.btn_4.setObjectName("btn_4")
        self.btn_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multiply.setGeometry(QtCore.QRect(300, 181, 100, 66))
        self.btn_multiply.setStyleSheet("background-color: rgb(170, 85, 255);\n"
"border: 1px solid #000;\n"
"border-radius: 2px;\n"
"font-family: Verdana;\n"
"font-size: 25px")
        self.btn_multiply.setObjectName("btn_multiply")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 115, 100, 66))
        self.btn_7.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid #000;\n"
"border-radius: 2px;\n"
"font-family: Verdana;\n"
"font-size: 25px}"
"QPushButton::hover{background-color: #be94d4}")
        self.btn_7.setObjectName("btn_7")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(200, 115, 100, 66))
        self.btn_9.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"border: 1px solid #000;\n"
"border-radius: 2px;\n"
"font-family: Verdana;\n"
"font-size: 25px}"
"QPushButton::hover{background-color: #be94d4}")
 


        self.btn_9.setObjectName("btn_9")
        self.btn_divide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_divide.setGeometry(QtCore.QRect(300, 115, 100, 66))
        self.btn_divide.setStyleSheet("background-color: rgb(170, 85, 255);\n"
"border: 1px solid #000;\n"
"border-radius: 2px;\n"
"font-family: Verdana;\n"
"font-size: 25px")
        self.btn_divide.setObjectName("btn_divide")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(100, 115, 100, 66))
        self.btn_8.setStyleSheet(f"{self.parametrs}")
        self.btn_8.setObjectName("btn_8")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(0, 49, 100, 66))
        self.btn_clear.setStyleSheet("background-color: #4d0f28;\n"
"border: 1px solid #000;\n"
"border-radius: 2px;\n"
"font-family: Verdana;\n"
"font-size: 25px")
        self.btn_clear.setObjectName("btn_clear")
        self.btn_stngs = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stngs.setGeometry(QtCore.QRect(100, 49, 100, 66))
        self.btn_stngs.setStyleSheet("background-color: #4d0f28;\n"
"border: 1px solid #000;\n"
"border-radius: 2px;\n"
"font-family: Verdana;\n"
"font-size: 25px")
        self.btn_stngs.setObjectName("btn_stngs")
        self.btn_more = QtWidgets.QPushButton(self.centralwidget)
        self.btn_more.setGeometry(QtCore.QRect(200, 49, 100, 66))
        self.btn_more.setStyleSheet("background-color: #4d0f28;\n"
"border: 1px solid #000;\n"
"border-radius: 2px;\n"
"font-family: Verdana;\n"
"font-size: 25px")
        self.btn_more.setObjectName("btn_more")
        self.btn_del = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del.setGeometry(QtCore.QRect(300, 49, 100, 66))
        self.btn_del.setStyleSheet("background-color: rgb(170, 85, 255);\n"
"border: 1px solid #000;\n"
"border-radius: 2px;\n"
"font-family: Verdana;\n"
"font-size: 25px")
        self.btn_del.setObjectName("btn_del")


        self.display = QtWidgets.QLabel(self.centralwidget)
        self.display.setStyleSheet("color: orange;\n"
"font-family: Verdana;\n"
"font-size: 25px")
        self.display.setGeometry(QtCore.QRect(325, 11, 100, 25))
        self.display.setObjectName("display")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "App"))
        self.label_result.setText(_translate("MainWindow", "TextLabel"))
        self.btn_d_1.setText(_translate("MainWindow", "9"))
        self.btn_0.setText(_translate("MainWindow", "9"))
        self.btn_equal.setText(_translate("MainWindow", "9"))
        self.btn_plus.setText(_translate("MainWindow", "9"))
        self.btn_minus.setText(_translate("MainWindow", "9"))
        self.btn_3.setText(_translate("MainWindow", "9"))
        self.btn_2.setText(_translate("MainWindow", "9"))
        self.btn_1.setText(_translate("MainWindow", "9"))
        self.btn_5.setText(_translate("MainWindow", "9"))
        self.btn_6.setText(_translate("MainWindow", "9"))
        self.btn_4.setText(_translate("MainWindow", "9"))
        self.btn_multiply.setText(_translate("MainWindow", "9"))
        self.btn_7.setText(_translate("MainWindow", "9"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_divide.setText(_translate("MainWindow", "9"))
        self.btn_8.setText(_translate("MainWindow", "9"))
        self.btn_clear.setText(_translate("MainWindow", "clear"))
        self.btn_stngs.setText(_translate("MainWindow", "stngs"))
        self.btn_more.setText(_translate("MainWindow", "more"))
        self.btn_del.setText(_translate("MainWindow", "<-"))
        self.display.setText(_translate("MainWindow", ""))

        self.btn_1.setText('1')
        self.btn_2.setText('2')
        self.btn_3.setText('3')
        self.btn_4.setText('4')
        self.btn_5.setText('5')
        self.btn_6.setText('6')
        self.btn_7.setText('7')
        self.btn_8.setText('8')
        self.btn_9.setText('9')
        self.btn_0.setText('0')
        
        self.btn_d_1.setText('')

        self.btn_equal.setText('=')
        self.btn_divide.setText('/')
        self.btn_multiply.setText('x')
        self.btn_minus.setText('-')
        self.btn_plus.setText('+')

        self.btn_clear.setText('C')
        self.btn_stngs.setText('Stngs')
        self.btn_more.setText('More')
        self.btn_del.setText('<-')

        
    def add_functions(self):
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))

        self.btn_divide.clicked.connect(lambda: self.write_number(self.btn_divide.text()))
        self.btn_multiply.clicked.connect(lambda: self.write_number(self.btn_multiply.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_equal.clicked.connect(self.result)

        self.btn_clear.clicked.connect(self.clear)

        self.label_result.setText('0')

    def write_number(self, number):
        if self.label_result.text() == '0':
            self.label_result.setText('')
        self.label_result.setText(self.label_result.text() + number)


    def result(self):
        self.list = []
        self.list_1 = []
        self.list_2 = []

        self.expression = self.label_result.text()
        for self.symbol in self.expression:
            self.list.insert(len(self.list), self.symbol)
        print(self.list)

        for self.element in self.list:
            self.list_1.insert(len(self.list_1), self.element)
            if self.element == '/':
                break
            elif self.element == 'x':
                break
            elif self.element == '-':
                break
            elif self.element == '+':
                break
        
        self.list_1.pop()
        self.length_1 = len(self.list_1)
        self.length = len(self.list)

        for self.i in range(self.length_1, self.length):
            self.list_2.insert(len(self.list_2), self.list[self.i])
        

        self.sign = self.list_2[0]
        self.list_2.reverse()
        self.list_2.pop()
        self.list_2.reverse()


        self.number_1 = int(''.join(self.list_1))
        self.number_2 = int(''.join(self.list_2))
        print(self.number_1)
        print(self.sign)
        print(self.number_2)

        if self.sign == '/':
            self.answer = self.number_1 / self.number_2

        elif self.sign == 'x':
            self.answer = self.number_1 * self.number_2

        elif self.sign == '-':
            self.answer = self.number_1 - self.number_2

        elif self.sign == '+':
            self.answer = self.number_1 + self.number_2


        print(self.answer)

        self.display.setText(f"{self.answer}")



    def clear(self):
        self.list_1 = []
        self.list_2 = []
        self.list = []
        self.label_result.setText('0')
   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

