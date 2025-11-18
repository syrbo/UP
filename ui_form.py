# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(491, 251)
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(7, 39, 471, 21))
        font = QFont()
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(7, 9, 471, 31))
        font1 = QFont()
        font1.setPointSize(18)
        self.label.setFont(font1)
        self.login = QLineEdit(Widget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(100, 100, 349, 21))
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 100, 50, 21))
        self.password = QLineEdit(Widget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(100, 130, 349, 21))
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 130, 50, 21))
        self.auth = QPushButton(Widget)
        self.auth.setObjectName(u"auth")
        self.auth.setGeometry(QRect(179, 190, 131, 32))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0443\u0439\u0442\u0435\u0441\u044c \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0435!", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u041f\u0430\u043d\u0435\u043b\u044c \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.auth.setText(QCoreApplication.translate("Widget", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
    # retranslateUi

