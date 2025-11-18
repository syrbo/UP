import sys
import mysql.connector
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from ui_form import Ui_Widget

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234567890",
    database="sys"
)
cursor = conn.cursor()

class Enter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.auth.clicked.connect(self.save_value)

    def save_value(self):        
        a = self.ui.login.text()
        b = self.ui.password.text()
        cursor.execute("SELECT password from sys.Autorization WHERE login = %s",(a,))
        str = cursor.fetchone()
        if b in str:
            print("ЛОГИН И ПАРОЛЬ СОВПАДАЕТ")
        else:
            msgBox = QMessageBox()
            msgBox.setText("Недачная попытка авторизации.")
            msgBox.exec()
        if self.w is None:
            self.w = Main()
            self.w.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Enter()
    widget.show()
    sys.exit(app.exec())
