# Form implementation generated from reading ui file 'addworker.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_helper2(object):
    def setupUi(self, helper):
        helper.setObjectName("helper")
        helper.resize(340, 203)
        self.centralwidget = QtWidgets.QWidget(parent=helper)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 71, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 60, 121, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 60, 121, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 20, 81, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(125, 120, 93, 28))
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
        self.label.setText(_translate("helper", "<html><head/><body><p><span style=\" font-size:11pt;\">Марка</span></p></body></html>"))
        self.label_2.setText(_translate("helper", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">ФИО</span></p></body></html>"))
        self.pushButton.setText(_translate("helper", "Подтвердить"))
