import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox)
from PyQt5.QtGui import QFont
import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Database')

        self.name_label = QLabel('Name:')
        self.name_edit = QLineEdit()
        self.email_label = QLabel('Email:')
        self.email_edit = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_edit = QLineEdit()

        self.add_button = QPushButton('Add User')
        self.add_button.clicked.connect(self.add_user)

        self.delete_button = QPushButton('Delete User')
        self.delete_button.clicked.connect(self.delete_user)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['ID', 'Name', 'Email'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.update_table()

        vbox = QVBoxLayout()
        vbox.addWidget(self.name_label)
        vbox.addWidget(self.name_edit)
        vbox.addWidget(self.email_label)
        vbox.addWidget(self.email_edit)
        vbox.addWidget(self.password_label)
        vbox.addWidget(self.password_edit)
        vbox.addWidget(self.add_button)
        vbox.addWidget(self.delete_button)
        vbox.addWidget(self.table)
        self.setLayout(vbox)

    def add_user(self):
        name = self.name_edit.text().strip()
        email = self.email_edit.text().strip()
        password = self.password_edit.text().strip()

        if not name or not email or not password:
            QMessageBox.warning(self, 'Input Error', 'All fields are required!')
            return

        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
            conn.commit()
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, 'Database Error', 'User with this email already exists!')
        finally:
            conn.close()

        self.name_edit.clear()
        self.email_edit.clear()
        self.password_edit.clear()
        self.update_table()

    def delete_user(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, 'Selection Error', 'Please select a user to delete!')
            return

        user_id = self.table.item(selected_row, 0).text()

        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()

        self.update_table()

    def update_table(self):
        self.table.setRowCount(0)
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            row_count = self.table.rowCount()
            self.table.insertRow(row_count)
            for i, item in enumerate(row):
                self.table.setItem(row_count, i, QTableWidgetItem(str(item)))
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())

