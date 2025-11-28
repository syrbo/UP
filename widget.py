import sys
import mysql.connector
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QTableWidgetItem, QAbstractItemView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt

version = 'beta 0.0.1'

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234567890",
    database="sys"
)
cursor = conn.cursor()


def load_ui(path):
    loader = QUiLoader()
    ui_file = QFile(path)
    ui_file.open(QFile.ReadOnly)
    ui = loader.load(ui_file)
    ui_file.close()
    return ui

def addToCheckBox(self,fetched,comboBoxName):
    for i in range(len(fetched)):
        item = fetched[i]
        res = ' '.join(item)
        print(comboBoxName)
        comboBoxName.insertItem(i,res)

def sos(self, rows=[]):
    if rows == []:
        exit
    self.ui.tableWidget.setRowCount(len(rows))
    self.ui.tableWidget.setColumnCount(5)
    self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows);
    for i in range(len(rows)):
        item = QTableWidgetItem(str(rows[i][0]))
        self.ui.tableWidget.setItem(i,0,item)
        item = QTableWidgetItem(str(rows[i][1]))
        self.ui.tableWidget.setItem(i,1,item)
        item = QTableWidgetItem(str(rows[i][2]))
        self.ui.tableWidget.setItem(i,2,item)
        item = QTableWidgetItem(str(rows[i][3]))
        self.ui.tableWidget.setItem(i,3,item)
        item = QTableWidgetItem(str(rows[i][4]))
        self.ui.tableWidget.setItem(i,4,item)


class NewName(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("newname.ui")
        self.setCentralWidget(self.ui)
        width = 700
        height = 665
        self.setFixedSize(width, height)
        self.ui.groupBox_2.setVisible(False)
        self.ui.pushButton_2.clicked.connect(self.showGroupBox_2)
        self.ui.pushButton_14.clicked.connect(self.hideGroupBox_2)
        self.ui.pushButton_13.clicked.connect(self.makeAction)
        self.ui.pushButton_12.clicked.connect(self.addChar)
        self.ui.label_4.setEnabled(False)
        self.ui.spinBox_2.setEnabled(False)
        self.ui.comboBox_2.setEnabled(False)
        self.ui.label_5.setEnabled(False)
        self.ui.spinBox_3.setEnabled(False)
        self.ui.checkBox.checkStateChanged.connect(self.garantyTurnOnOff)
        self.ui.comboBox_3.currentIndexChanged.connect(self.typeChange)

        cursor.execute("SELECT Value FROM sys.Manufacturer;")
        manufacturer = cursor.fetchall()
        addToCheckBox(self,manufacturer,self.ui.comboBox)
        cursor.execute("SELECT Value FROM sys.TypeTovar;")
        typesTovar = cursor.fetchall()
        addToCheckBox(self,typesTovar,self.ui.comboBox_3)

        cursor.execute("SELECT Value FROM sys.Characters;")
        rows = cursor.fetchall()
        self.ui.tableWidget_5.setRowCount(len(rows))
        self.ui.tableWidget_5.setColumnCount(2)
        for i in range(len(rows)):
            text_item = QTableWidgetItem(str(rows[i][0]))
            self.ui.tableWidget_5.setItem(i, 1, text_item)
            check_item = QTableWidgetItem()
            check_item.setFlags(check_item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            check_item.setCheckState(Qt.Unchecked)
            self.ui.tableWidget_5.setItem(i, 0, check_item)

    def garantyTurnOnOff(self):
        if self.ui.checkBox.isChecked() == False:
            self.ui.label_4.setEnabled(False)
            self.ui.spinBox_2.setEnabled(False)
            self.ui.comboBox_2.setEnabled(False)
            self.ui.label_5.setEnabled(False)
            self.ui.spinBox_3.setEnabled(False)
        elif self.ui.checkBox.isChecked() == True:
            self.ui.label_4.setEnabled(True)
            self.ui.spinBox_2.setEnabled(True)
            self.ui.comboBox_2.setEnabled(True)
            self.ui.label_5.setEnabled(True)
            self.ui.spinBox_3.setEnabled(True)
        else:
            return('отрава')

    def typeChange(self):
        typeTovarID = int(self.ui.comboBox_3.currentIndex()) + 1
        print(typeTovarID)
        cursor.execute("""SELECT *
        FROM TypeTovar
        JOIN TypeCharList       ON TypeTovar.ID = TypeCharList.TypeID
        LEFT JOIN CharValues    ON CharValues.CharID = TypeCharList.CharID
        LEFT JOIN Characters    ON Characters.ID = TypeCharList.CharID
        WHERE TypeTovar.ID = %s;""",(typeTovarID,))
        rows = cursor.fetchall()
        print(rows)
        self.ui.tableWidget_3.setRowCount(len(rows))
        self.ui.tableWidget_3.setColumnCount(2)
        for i in range(len(rows)):
            item = QTableWidgetItem(str(rows[i][8]))
            self.ui.tableWidget_3.setItem(i,0,item)
        print('поменял', 'индекс ', typeTovarID)

    def addChar(self):
        charName = self.ui.lineEdit_3.text()
        cursor.execute("INSERT INTO sys.Characters (Value) VALUES (%s);",(charName,))
        conn.commit()
        print(charName)

    def makeAction(self):
        checked = []
        row_count = self.ui.tableWidget_3.rowCount()

        for row in range(row_count):
            item = self.ui.tableWidget_3.item(row, 0)
            if item and item.checkState() == Qt.Checked:
                checked.append(row + 1)

        typeName = self.ui.lineEdit_8.text()

        cursor.execute(
            "INSERT INTO TypeTovar (Value) VALUES (%s);",
            (typeName,)
        )
        conn.commit()

        cursor.execute("SELECT LAST_INSERT_ID();")
        new_type_id = cursor.fetchone()[0]

        print("Новый TypeID:", new_type_id)

        for char_id in checked:
            cursor.execute(
                "INSERT INTO TypeCharList (TypeID, CharID) VALUES (%s, %s);",
                (new_type_id, char_id)
            )

        conn.commit()


    def showGroupBox_2(self):
        self.ui.groupBox_2.setVisible(True)
        self.ui.scrollArea.setVisible(False)

    def hideGroupBox_2(self):
        self.ui.groupBox_2.setVisible(False)
        self.ui.scrollArea.setVisible(True)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("main.ui")
        self.setCentralWidget(self.ui)
        self.setCentralWidget(self.ui)
        width = 1100
        height = 450
        self.setFixedSize(width, height)

        self.ui.action_3.triggered.connect(self.toNewName)

        self.ui.tableWidget.cellClicked.connect(self.on_cell_clicked)
        self.ui.lineEdit.textEdited.connect(self.text_edited)
        self.ui.version.setText(f'версия {version}')
        cursor.execute("""
            SELECT u.Surname, u.Name, u.Patronymic
            FROM sys.Autorization a
            JOIN sys.Users u ON u.ID = a.UserID
            WHERE a.Login = %s
        """, (user,))
        user_SNP = cursor.fetchone()
        self.ui.label_user.setText(f'Пользователь: {user_SNP[0]} {user_SNP[1]} {user_SNP[2]}')
        cursor.execute("""
            SELECT u.RoleID
            FROM sys.Autorization a
            JOIN sys.Users u ON u.ID = a.UserID
            WHERE a.Login = %s
        """, (user,))
        acc_Role = cursor.fetchone()
        cursor.execute("SELECT Value FROM sys.Roles WHERE ID= %s", (acc_Role[0],))
        acc_Role = cursor.fetchone()
        self.ui.label_role.setText(f'Текущая роль: {acc_Role[0]}')
        cursor.execute("SELECT Tovar.ID, CONCAT(TypeTovar.Value,' ',Manufacturer.Value,' ', Tovar.Name) as TovarName, Tovar.CostValue,  Tovar.Count, Tovar.GarantyValue FROM Tovar INNER JOIN Manufacturer ON Tovar.ManufacturerID = Manufacturer.ID INNER JOIN TypeTovar ON Tovar.TypeID = TypeTovar.ID")
        rows = cursor.fetchall()
        print(rows)
        sos(self, rows)

    def toNewName(self):
        self.new_window = NewName()
        self.new_window.show()

    def text_edited(self):
        a = self.ui.lineEdit.text()
        if self.ui.comboBox.currentIndex() == 0:
            cursor.execute("SELECT Tovar.ID, CONCAT(TypeTovar.Value,' ',Manufacturer.Value,' ', Tovar.Name) as TovarName, Tovar.CostValue,  Tovar.Count, Tovar.GarantyValue FROM Tovar INNER JOIN Manufacturer ON Tovar.ManufacturerID = Manufacturer.ID INNER JOIN TypeTovar ON Tovar.TypeID = TypeTovar.ID WHERE Tovar.ID LIKE '%"+a+"%'")
            rows = cursor.fetchall()
            sos(self, rows)
        elif self.ui.comboBox.currentIndex() == 1:
            cursor.execute("SELECT Tovar.ID, CONCAT(TypeTovar.Value,' ',Manufacturer.Value,' ', Tovar.Name) as TovarName, Tovar.CostValue,  Tovar.Count, Tovar.GarantyValue FROM Tovar INNER JOIN Manufacturer ON Tovar.ManufacturerID = Manufacturer.ID INNER JOIN TypeTovar ON Tovar.TypeID = TypeTovar.ID WHERE CONCAT(TypeTovar.Value,' ',Manufacturer.Value, ' ', Tovar.Name) LIKE '%"+a+"%'")
            rows = cursor.fetchall()
            sos(self, rows)
        else:
            return("отрава")


    def on_cell_clicked(self, row, column):
        item = self.ui.tableWidget.item(row, 0)
        a = item.text()
        cursor.execute("""
        SELECT * FROM Tovar
        INNER JOIN TypeCharList ON Tovar.TypeID = TypeCharList.TypeID
        INNER JOIN CharValues ON TypeCharList.CharID = CharValues.CharID
        INNER JOIN Characters ON Characters.ID = CharValues.CharID
        WHERE Tovar.ID= %s
        """, (a,))
        rows = cursor.fetchall()
        self.ui.tableWidget_2.setRowCount(len(rows))
        self.ui.tableWidget_2.setColumnCount(2)
        self.ui.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows);
        for i in range(len(rows)):
            item = QTableWidgetItem(str(rows[i][12]))
            self.ui.tableWidget_2.setItem(i,1,item)
            item = QTableWidgetItem(str(rows[i][14]))
            self.ui.tableWidget_2.setItem(i,0,item)

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = load_ui("login.ui")
        self.setCentralWidget(self.ui)
        self.ui.auth.clicked.connect(self.login)
        self.ui.pass_show.toggled.connect(self.toggle_password)
        self.ui.password.setEchoMode(QLineEdit.Password)
        self.setCentralWidget(self.ui)
        width = 500
        height = 250
        self.setFixedSize(width, height)

    def toggle_password(self, checked):
        if checked:
            self.ui.password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.password.setEchoMode(QLineEdit.Password)

    def login(self):
        global user
        user = self.ui.login.text()
        password = self.ui.password.text()

        cursor.execute(
            "SELECT password FROM sys.Autorization WHERE login=%s",(user,)
        )
        result = cursor.fetchone()

        if not result or result[0] != password:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль.")
            return

        self.main_window = MainWindow()
        self.main_window.show()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
