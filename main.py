import sys
import copy
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import csv
import webbrowser
import tkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from PyQt5 import uic, QtGui
import hashlib


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file_name = ''
        uic.loadUi('des.ui', self)
        self.tableWidget.cellDoubleClicked.connect(self.f)
        self.tableWidget.currentCellChanged.connect(self.activ)
        self.tableWidget.cellChanged.connect(self.izm)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1)
        self.pushButton.clicked.connect(self.sort_by_name)
        self.pushButton_2.clicked.connect(self.rowup)
        self.pushButton_3.clicked.connect(self.rowdown)
        self.pushButton_4.clicked.connect(Opening.openf)
        self.pushButton_5.clicked.connect(Opening.savef)
        self.pushButton_6.clicked.connect(Opening.saveasf)
        self.pushButton_7.clicked.connect(self.new)
        self.pushButton_8.clicked.connect(self.delete)
        self.pushButton_9.clicked.connect(self.changepassword)
        self.pushButton_10.clicked.connect(self.newfile)
        self.pushButton_11.clicked.connect(self.exit)
        self.spisok_of_name = []
        self.db = []
        self.reader = ''
        self.parol = ''
        k = ["Название", "Ссылка", "Логин", "Пароль"]
        title = k
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.pushButton.setStyleSheet("""
            QPushButton:hover { background-color: #00cfff }
            QPushButton:!hover { background-color: #00cfff }

            QPushButton:pressed { background-color: #164483; }
        """)  # Дизайн кнопок
        self.pushButton_2.setStyleSheet("""
                    QPushButton:hover { background-color: #00cfff }
                    QPushButton:!hover { background-color: #00cfff }

                    QPushButton:pressed { background-color: #164483; }
                """)
        self.pushButton_3.setStyleSheet("""
                    QPushButton:hover { background-color: #00cfff }
                    QPushButton:!hover { background-color: #00cfff }

                    QPushButton:pressed { background-color: #164483; }
                """)
        self.pushButton_4.setStyleSheet("""
                    QPushButton:hover { background-color: #00cfff }
                    QPushButton:!hover { background-color: #00cfff }

                    QPushButton:pressed { background-color: #164483; }
                """)
        self.pushButton_5.setStyleSheet("""
                            QPushButton:hover { background-color: #00cfff }
                            QPushButton:!hover { background-color: #00cfff }

                            QPushButton:pressed { background-color: #164483; }
                        """)
        self.pushButton_6.setStyleSheet("""
                            QPushButton:hover { background-color: #00cfff }
                            QPushButton:!hover { background-color: #00cfff }

                            QPushButton:pressed { background-color: #164483; }
                        """)
        self.pushButton_7.setStyleSheet("""
                                    QPushButton:hover { background-color: #00cfff }
                                    QPushButton:!hover { background-color: #00cfff }

                                    QPushButton:pressed { background-color: #164483; }
                                """)
        self.pushButton_8.setStyleSheet("""
                                    QPushButton:hover { background-color: #00cfff }
                                    QPushButton:!hover { background-color: #00cfff }

                                    QPushButton:pressed { background-color: #164483; }
                                """)
        self.pushButton_9.setStyleSheet("""
                                            QPushButton:hover { background-color: #00cfff }
                                            QPushButton:!hover { background-color: #00cfff }

                                            QPushButton:pressed { background-color: #164483; }
                                        """)
        self.pushButton_10.setStyleSheet("""
                                            QPushButton:hover { background-color: #00cfff }
                                            QPushButton:!hover { background-color: #00cfff }

                                            QPushButton:pressed { background-color: #164483; }
                                        """)
        self.pushButton_11.setStyleSheet("""
                                            QPushButton:hover { background-color: #00cfff }
                                            QPushButton:!hover { background-color: #00cfff }

                                            QPushButton:pressed { background-color: #164483; }
                                        """)

    def rowup(self):  # Функция сдвига колонок вверх
        cur = self.tableWidget.currentRow()
        if cur > 0:
            for i in range(4):
                self.db[cur][i], self.db[cur - 1][i] = self.db[cur - 1][i], self.db[cur][i]
            self.refresh_table()
            self.tableWidget.setCurrentCell(cur - 1, 0)

    def rowdown(self):  # Фунцкия сдвига колонок вниз
        cur = self.tableWidget.currentRow()
        if cur < len(self.db) - 1:
            for i in range(4):
                self.db[cur][i], self.db[cur + 1][i] = self.db[cur + 1][i], self.db[cur][i]
            self.refresh_table()
            self.tableWidget.setCurrentCell(cur + 1, 0)

    def new(self):
        cur = self.tableWidget.currentRow()
        self.db.insert(cur, ['', '', '', ''])
        self.refresh_table()

    def newfile(self):
        self.db = []
        self.refresh_table()

    def delete(self):
        if len(self.db) != 0:
            cur = self.tableWidget.currentRow()
            del self.db[cur]
            self.refresh_table()

    def sort_by_name(self):  # Сортировка таблицы по имени сайта
        self.db = sorted(self.db, key=lambda x: x[0])
        self.refresh_table()

    def changepassword(self):  # Смена пароля
        root = Tk()
        root.withdraw()
        self.parol = askstring('Pass', 'Введите новый пароль')
        root.destroy()

    def izm(self, row, col):
        if self.tableWidget.item(row, col).text() != '*****':
            self.db[row][col] = self.tableWidget.item(row, col).text()
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setSectionResizeMode(1)

    def activ(self, currentrow, currentcolumn, previousrow, previouscolumn):  # Скрытие пароля
        if currentrow != previousrow:
            d = QTableWidgetItem('*****')
            d.setForeground(QtGui.QColor("#000"))
            d.setBackground(QtGui.QColor("#fff"))
            self.tableWidget.setItem(previousrow, 3, d)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1)

    def refresh_table(self):  # Основная функция заполнения таблицы
        self.tableWidget.setRowCount(len(self.db))
        for i in range(len(self.db)):  # Заполнение таблицы
            a = QTableWidgetItem(self.db[i][0])
            a.setForeground(QtGui.QColor("#000"))
            a.setBackground(QtGui.QColor("#fff"))
            b = QTableWidgetItem(self.db[i][1])
            b.setForeground(QtGui.QColor("#000"))
            b.setBackground(QtGui.QColor("#fff"))
            c = QTableWidgetItem(self.db[i][2])
            c.setForeground(QtGui.QColor("#000"))
            c.setBackground(QtGui.QColor("#fff"))
            d = QTableWidgetItem('*****')
            d.setForeground(QtGui.QColor("#000"))
            d.setBackground(QtGui.QColor("#fff"))
            self.tableWidget.setItem(i, 0, a)
            self.tableWidget.setItem(i, 1, b)
            self.tableWidget.setItem(i, 2, c)
            self.tableWidget.setItem(i, 3, d)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setSectionResizeMode(1)

    def f(self, row, col):  # Функция перехода на сайт и копирования пароля или логина
        if col == 1:  # ссылку на сайт в браузере
            webbrowser.open(self.tableWidget.item(row, col).text(), new=2)
        if col == 2 or col == 3:  # копируем логин или пароль в буфер обмена
            tk = tkinter.Tk()
            tk.withdraw()
            tk.clipboard_clear()
            tk.clipboard_append(self.db[row][col])
            tk.destroy()
        if col == 3:
            self.tableWidget.setItem(row, col, QTableWidgetItem(self.db[row][col]))

    def load_table(self, table_name):  # Загрузка таблицы
        with open(table_name) as csvfile:
            self.reader = csv.reader(csvfile, delimiter='|', quotechar='"')
            k = ["Название", "Ссылка", "Логин", "Пароль"]
            title = k
            self.spisok_of_name = []
            self.db = []
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            for i, row in enumerate(self.reader):
                m = []
                m.append(row[0])
                m.append(row[1])
                m.append(row[2])
                m.append(row[3])
                self.db.append(m)
            user_pass_hash = self.db[-1][0]  # записанный в файл хэш пароля
            del self.db[-1]
            if self.parol == '':
                parol_hash = ''
            else:
                parol_hash = hashlib.md5(self.parol.encode('utf-8')).hexdigest()  # хэш пароля
            if user_pass_hash == parol_hash:
                cr = Cryptit()
                self.db = cr.decrypt(self.db)
                self.refresh_table()  # Функция заполнения таблицы
                self.tableWidget.resizeColumnsToContents()
                self.tableWidget.horizontalHeader().setSectionResizeMode(1)
                self.tableWidget.setCurrentCell(0, 0)
            else:
                root = Tk()
                root.withdraw()
                messagebox.showerror("Ошибка", "Неверный пароль")
                root.destroy()

    def exit(self):
        sys.exit(app.exec_())


class Cryptit:  # Класс шифрования паролей
    def crypt(self, d):
        chars_from = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        chars_from += 'abcdefghijklmnopqrstuvwxyz_-+'
        chars_from += 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        chars_from += 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890'
        chars_to = 'YJ+MISKPNAC-Rsfu0qelnvhd_k'
        chars_to += 'GXOEH1VZUL7WDQTFBzarpbjytcwogxmi'
        chars_to += 'ШОБТЙЩДюъохвжьк5гияЁАЬ9ЦЛМГ26РЯКНЕХПУЮИ'
        chars_to += 'ФСЖ8ЪЭ3ЗВЫЧлцщшзычмедйтруэ4снфабёп'
        crypt = str.maketrans(chars_from, chars_to)
        for i in range(len(d)):
            d[i][2] = d[i][2].translate(crypt)
            d[i][3] = d[i][3].translate(crypt)
        return d

    def decrypt(self, d):
        chars_from = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        chars_from += 'abcdefghijklmnopqrstuvwxyz_-+'
        chars_from += 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        chars_from += 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890'
        chars_to = 'YJ+MISKPNAC-Rsfu0qelnvhd_k'
        chars_to += 'GXOEH1VZUL7WDQTFBzarpbjytcwogxmi'
        chars_to += 'ШОБТЙЩДюъохвжьк5гияЁАЬ9ЦЛМГ26РЯКНЕХПУЮИ'
        chars_to += 'ФСЖ8ЪЭ3ЗВЫЧлцщшзычмедйтруэ4снфабёп'
        decrypt = str.maketrans(chars_to, chars_from)
        for i in range(len(d)):
            d[i][2] = d[i][2].translate(decrypt)
            d[i][3] = d[i][3].translate(decrypt)
        return d


class Opening(MyWidget):  # Класс открытия файла
    def openf(self):
        ftypes = [('dpe files', '*.dpe')]
        root = Tk()
        root.withdraw()
        ex.file_name = askopenfilename(filetypes=ftypes)
        ex.parol = askstring('Pass', 'Введите пароль')
        root.destroy()
        if ex.file_name and ex.parol:
            ex.load_table(ex.file_name)

    def savef(self):
        if len(ex.db) != 0:
            cr = Cryptit()
            dbcrypt = copy.deepcopy(ex.db)
            dbcrypt = cr.crypt(dbcrypt)
            if ex.parol == '':
                parol_hash = ''
            else:
                parol_hash = hashlib.md5(ex.parol.encode('utf-8')).hexdigest()  # хэш пароля
            dbcrypt.append([parol_hash, '', '', ''])
            with open(ex.file_name, "w", newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter='|')
                for line in dbcrypt:
                    writer.writerow(line)

    def saveasf(self):  # Функция сох
        if len(ex.db) != 0:
            ftypes = [('dpe files', '*.dpe')]
            root = Tk()
            root.withdraw()
            ex.file_name = asksaveasfilename(filetypes=ftypes, defaultextension="dpe")
            root.destroy()
            if ex.file_name:
                cr = Cryptit()
                dbcrypt = copy.deepcopy(ex.db)
                dbcrypt = cr.crypt(dbcrypt)
                if ex.parol == '':
                    parol_hash = ''
                else:
                    parol_hash = hashlib.md5(ex.parol.encode('utf-8')).hexdigest()  # хэш пароля
                dbcrypt.append([parol_hash, '', '', ''])
                with open(ex.file_name, "w", newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter='|')
                    for line in dbcrypt:
                        writer.writerow(line)


app = QApplication(sys.argv)
app.setStyle('Fusion')
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
