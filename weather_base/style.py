import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.insert(1, '/home/import/Documents/weather_base/weather_base')
import api

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 481)
        Form.setStyleSheet("*{\n" "    background-color : \"#2e3440\";\n" "}")
        self.root = api.Api()
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, -10, 501, 491))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.main_label = QtWidgets.QLabel(self.frame)
        self.main_label.setGeometry(QtCore.QRect(20, 20, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Mono")
        font.setPointSize(36)
        self.main_label.setFont(font)
        self.main_label.setStyleSheet("*{\n"
                                      "    color: #eceff4\n"
                                      "    \n"
                                      "}\n"
                                      "")
        self.main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_label.setObjectName("main_label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(200, 60, 91, 17))
        font = QtGui.QFont()
        font.setFamily("comic mono")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("*{\n"
                                   "    color: \"#d8dee9\";\n"
                                   "    font-family:\"comic mono\"\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.output = QtWidgets.QLabel(self.frame)
        self.output.setGeometry(QtCore.QRect(90, 250, 350, 201))
        self.output.setStyleSheet("*{\n"
                                  "    text-align: center;\n"
                                  "    font-size: 21px;\n"
                                  "    font-family:\"comic mono\"\n"
                                  "}")
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setObjectName("output")
        self.btn = QtWidgets.QPushButton(self.frame)
        self.btn.clicked.connect(self.set_text)
        self.btn.setGeometry(QtCore.QRect(150, 170, 191, 41))
        self.btn.setStyleSheet("*{\n"
                               "    background-color : \"#434c5e\"; \n"
                               "    color : white;\n"
                               "    text-align: center;\n"
                               "    font-size: 16px;\n"
                               "    border-radius: 8px;\n"
                               "\n"
                               "}\n"
                               "\n"
                               "*:hover {\n"
                               "    background-color: #000000;\n"
                               "}")
        self.btn.setObjectName("btn")
        self.line_input = QtWidgets.QLineEdit(self.frame)
        self.line_input.setGeometry(QtCore.QRect(60, 110, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Mono")
        font.setPointSize(24)
        self.line_input.setFont(font)
        self.line_input.setStyleSheet("*{\n"
                                      "    background-color: \"#3b4252\";\n"
                                      "    color:white;\n"
                                      "    border-radius: 8px;\n"
                                      "\n"
                                      "}")
        self.line_input.setObjectName("line_input")
        self.line_input.setAlignment(QtCore.Qt.AlignCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def set_text(self):
        self.output.setText(self.root.Get_weather(city=self.line_input.text()))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.main_label.setText(_translate("Form", "⛅Weather"))
        self.label_2.setText(_translate("Form", "Made by Nwn"))
        # self.output.setText(_translate("Form", "dasfdfsdfsdfsdfds"))
        self.btn.setText(_translate("Form", "Get Weather !!"))
