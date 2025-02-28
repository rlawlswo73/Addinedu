import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic 
from PyQt5.QtCore import QDate
import mysql.connector

from_class = uic.loadUiType("Test8.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self. setupUi(self)

        self.remote = mysql.connector.connect(
            host = "database-1.c3mmsaki87vo.ap-northeast-2.rds.amazonaws.com",
            port = 3306,
            user = "admin",
            password = "rlawlswo1",
            database = "amrdb"
        )
        self.cursor = self.remote.cursor(buffered=True)
            
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.btnSearch.clicked.connect(self.Search)
        self.btnClear.clicked.connect(self.Clear)

        sql = "select distinct birthday from celeb order by birthday asc"
        self.cursor.execute(sql)
        self.date_result = list(self.cursor.fetchall())
        self.start = self.date_result[0][0]
        self.end = self.date_result[-1][0]
        # self.editBirthday_start.setMinimumDate(QDate(self.start))
        # self.editBirthday_end.setMaximumDate(QDate(self.end))
        self.editBirthday_start.setDate(QDate(self.start))
        self.editBirthday_end.setDate(QDate(self.end))
        self.editBirthday_start.dateChanged.connect(self.dateChanged)
        self.editBirthday_end.dateChanged.connect(self.dateChanged)
        # self.editBirthday_end.setCurrentText(str(20221231))

        self.cbSex.addItem("All")
        sql = "select distinct sex from celeb"
        self.cursor.execute(sql)
        result = list(self.cursor.fetchall())
        for idx, i in enumerate(result):
            self.cbSex.addItem(str(result[idx][0]))
        self.cbJobtitle.addItem("All")
        self.cbJobtitle.addItem("가수")
        self.cbJobtitle.addItem("개그맨")
        self.cbJobtitle.addItem("텔런트")
        self.cbJobtitle.addItem("영화배우")
        self.cbJobtitle.addItem("모델")
        self.cbJobtitle.addItem("MC")
        self.cbAgency.addItem("All")
        sql = "select distinct agency from celeb"
        self.cursor.execute(sql)
        result = list(self.cursor.fetchall())
        for idx, i in enumerate(result):
            self.cbAgency.addItem(str(result[idx][0]))

    def dateChanged(self, date):
        # 날짜 유효성 검사
        if (QDate(self.start) > date) or (QDate(self.end) < date) :
            if (QDate(self.start) > date) :
                self.editBirthday_start.setDate(QDate(self.start))
            elif (QDate(self.end) < date) :
                self.editBirthday_end.setDate(QDate(self.end))
            QMessageBox.warning(self, 'Wrong Enter', 'Please enter right date')
        else:
            pass
            
    def date_error(self, date):
        QMessageBox.warning(self, 'Wrong Enter', 'Please enter right date')

    def Clear(self):
        self.cbSex.setCurrentText("All")
        self.cbJobtitle.setCurrentText("All")
        self.cbAgency.setCurrentText("All")
        self.editBirthday_start.setDate(QDate(self.start))
        self.editBirthday_end.setDate(QDate(self.end))

    def Search(self):
        self.tableWidget.setRowCount(0) 
        sex = str(self.cbSex.currentText())
        job = str(self.cbJobtitle.currentText())
        agency = str(self.cbAgency.currentText())

        # selet * from celeb where 날짜, 성별, 직업, 소속
        sql = "select * from celeb"
        where = "where"

        date = " birthday between " + str(self.editBirthday_start.text()) + " and " + str(self.editBirthday_end.text())
        where += date

        if(sex != "All" or job != "All" or agency != "All") :
            where += " and"

            if sex != "All":
                where += " sex='" + sex + "'"
                if job != "All" or agency != "All":
                    where += " and"
            if job != "All":
                where += " job_title like '%" + job + "%'"
                if agency != "All":
                    where += " and"
            if agency != "All":
                where += " agency='" + agency + "'"

            sql += " " + where

        print(sql)
        self.cursor.execute(sql)
        result = list(self.cursor.fetchall())
        # print(len(result))
        for idx, i in enumerate(result):
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for j in range(7):
                self.tableWidget.setItem(row, j, QTableWidgetItem(str(result[idx][j])))

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())