# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_helper(object):
    def setupUi(self, helper):
        helper.setObjectName("helper")
        helper.resize(215, 203)
        self.centralwidget = QtWidgets.QWidget(parent=helper)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 161, 21))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 20, 191, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 50, 141, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 40, 141, 51))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 90, 101, 31))
        self.pushButton.setObjectName("pushButton")
        helper.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=helper)
        self.statusbar.setObjectName("statusbar")
        helper.setStatusBar(self.statusbar)

        self.retranslateUi(helper)
        QtCore.QMetaObject.connectSlotsByName(helper)

    def retranslateUi(self, helper):
        _translate = QtCore.QCoreApplication.translate
        helper.setWindowTitle(_translate("helper", "MainWindow"))
        self.label.setText(_translate("helper", "<html><head/><body><p><span style=\" font-size:11pt;\">Код подразделения</span></p></body></html>"))
        self.pushButton.setText(_translate("helper", "Сгенерировать"))
