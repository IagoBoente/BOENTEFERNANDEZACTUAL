# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vensalir.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_venSalir(object):
    def setupUi(self, venSalir):
        venSalir.setObjectName("venSalir")
        venSalir.resize(376, 150)
        venSalir.setModal(True)
        self.btnBoxSalir = QtWidgets.QDialogButtonBox(venSalir)
        self.btnBoxSalir.setGeometry(QtCore.QRect(120, 90, 161, 32))
        self.btnBoxSalir.setOrientation(QtCore.Qt.Horizontal)
        self.btnBoxSalir.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.btnBoxSalir.setCenterButtons(True)
        self.btnBoxSalir.setObjectName("btnBoxSalir")
        self.lblMensalir = QtWidgets.QLabel(venSalir)
        self.lblMensalir.setGeometry(QtCore.QRect(90, 40, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lblMensalir.setFont(font)
        self.lblMensalir.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblMensalir.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblMensalir.setObjectName("lblMensalir")
        self.lblImgaviso = QtWidgets.QLabel(venSalir)
        self.lblImgaviso.setGeometry(QtCore.QRect(30, 30, 51, 41))
        self.lblImgaviso.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblImgaviso.setText("")
        self.lblImgaviso.setPixmap(QtGui.QPixmap(":/avisosalir/iconoaviso.png"))
        self.lblImgaviso.setScaledContents(True)
        self.lblImgaviso.setObjectName("lblImgaviso")
        self.label = QtWidgets.QLabel(venSalir)
        self.label.setGeometry(QtCore.QRect(50, 70, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/iconoaviso.png"))
        self.label.setObjectName("label")

        self.retranslateUi(venSalir)
        self.btnBoxSalir.accepted.connect(venSalir.accept)
        self.btnBoxSalir.rejected.connect(venSalir.reject)
        QtCore.QMetaObject.connectSlotsByName(venSalir)

    def retranslateUi(self, venSalir):
        _translate = QtCore.QCoreApplication.translate
        venSalir.setWindowTitle(_translate("venSalir", "Desea Salir?"))
        self.lblMensalir.setText(_translate("venSalir", "¿Está seguro que desea salir de la aplicación?"))

