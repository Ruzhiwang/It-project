# coding=utf-8
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox,QFileDialog
import sqlite3
import xlrd
import xlwt
from zhujiemian import Ui_MainWindow

#连接数据库
conn = sqlite3.connect('teacher.db')
c = conn.cursor()

class Ui_Main(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        super(Ui_Main,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.chaxunall)
        self.pushButton_2.clicked.connect(self.chaxunid)
        self.pushButton_3.clicked.connect(self.chaxunname)
        self.pushButton_4.clicked.connect(self.add_newtc)
        self.pushButton_5.clicked.connect(self.change)
        self.pushButton_6.clicked.connect(self.shanchu)
        self.pushButton_9.clicked.connect(self.beifen)
        self.pushButton_7.clicked.connect(self.openfile)
        self.pushButton_8.clicked.connect(self.savefile)
#导入
    #def daoru(self):

#导出

#查询.所有教师
    def chaxunall(self):
        n = c.execute('select * from t')
        a = n.fetchall()
        d = '教师ID\t姓名\t任课数\t所授课程\n'
        for i in a:
            d += i[0]+"\t"+i[1]+"\t"+i[2]+'\t'+i[3]+'\n'
        self.textBrowser.setText(d)
#查询.根据教师id查询
    def chaxunid(self):
        a = self.lineEdit.text()
        if a == '':
           reply = QMessageBox.warning(self,'警告','教工号输入为空！')
        else:
            isok = c.execute("select * from t where id ='"+str(a)+"'")
            tempstr = isok.fetchall()
            if tempstr:
                d ='教师ID\t姓名\t任课数\t所授课程\n'
                d += tempstr[0][0] + "\t" + tempstr[0][1] + "\t" + tempstr[0][2] + '\t' + tempstr[0][3] + '\n'
                self.textBrowser.setText(d)
            else:
                reply = QMessageBox.warning(self,'警告','未找到该教师信息！')

#查询.根据教师姓名查询
    def chaxunname(self):
           a = self.lineEdit_2.text()
           if a == '':
              reply = QMessageBox.warning(self,'警告','教工姓名输入为空！')
           else:
               isok = c.execute("select * from t where name ='"+str(a)+"'")
               tempstr = isok.fetchall()
               d = '教师ID\t姓名\t任课数\t所授课程\n'
               if tempstr:
                  for i in tempstr:
                   d += i[0] + "\t" + i[1] + "\t" + i[2] + '\t' + i[3] + '\n'
                   self.textBrowser.setText(d)
               else:
                   reply = QMessageBox.warning(self,'警告','未找到该教师信息！')

#修改.添加新教工信息
    def add_newtc(self):
        a = self.lineEdit_3.text()
        if a == '':
           reply = QMessageBox.warning(self,'警告','教工号输入为空！')
        else:
            isok = c.execute("select * from t where id ='"+str(a)+"'")
            tempstr = isok.fetchall()
            if tempstr:
                reply = QMessageBox.warning(self, '警告', '教工号已存在！')
            else:
                tempstr = list()
                tempstr.append(self.lineEdit_3.text())
                tempstr.append(self.lineEdit_4.text())
                tempstr.append(self.lineEdit_5.text())
                tempstr.append(self.lineEdit_6.text())
                n = c.execute("insert into t values (?,?,?,?)", tempstr)
                conn.commit()
                reply = QMessageBox.information(self, '成功！', '添加成功！')
                n = c.execute('select * from t')
                a = n.fetchall()
                d = '教师ID\t姓名\t任课数\t所授课程\n'
                for i in a:
                    d += i[0] + "\t" + i[1] + "\t" + i[2] + '\t' + i[3] + '\n'
                self.textBrowser_3.setText(d)
#修改.根据教工号修改信息
    def change(self):
        a = self.lineEdit_7.text()
        if a == '':
            reply = QMessageBox.warning(self, '警告', '教工号输入为空！')
        else:
            isok = c.execute("select * from t where id ='" + str(a) + "'")
            tempstr = isok.fetchall()
            if tempstr:
                b = self.lineEdit_8.text()
                cc = self.lineEdit_9.text()
                dd = self.lineEdit_10.text()
                if b != '':
                    c.execute("update t set name = '" + b + "' where id = '"+str(a)+"'")
                    conn.commit()
                if cc != '':
                    c.execute("update t set courses = '" + cc + "' where id = '"+str(a)+"'")
                    conn.commit()
                if dd != '':
                    c.execute("update t set ke = '" + dd + "' where id = '"+str(a)+"'")
                    conn.commit()
                reply = QMessageBox.information(self, '成功！', '修改成功！')
                n = c.execute('select * from t')
                a = n.fetchall()
                d = '教师ID\t姓名\t任课数\t所授课程\n'
                for i in a:
                    d += i[0] + "\t" + i[1] + "\t" + i[2] + '\t' + i[3] + '\n'
                self.textBrowser_3.setText(d)
            else:
                reply = QMessageBox.warning(self, '修改失败', '未找到该教师信息！')

#修改.根据教工号删除
    def shanchu(self):
        a = self.lineEdit_11.text()
        if a == '':
            reply = QMessageBox.warning(self, '警告', '教工号输入为空！')
        else:
            isok = c.execute("select * from t where id ='" + str(a) + "'")
            tempstr = isok.fetchall()
            if tempstr:
                c.execute("delete  from t where id ='"+str(a)+"'")
                conn.commit()
                reply = QMessageBox.information(self, '成功！', '删除成功！')
                n = c.execute('select * from t')
                a = n.fetchall()
                d = '教师ID\t姓名\t任课数\t所授课程\n'
                for i in a:
                    d += i[0] + "\t" + i[1] + "\t" + i[2] + '\t' + i[3] + '\n'
                self.textBrowser_3.setText(d)
            else:
                reply = QMessageBox.warning(self, '删除失败', '未找到该教师信息！')

# 数据库备份
    def beifen(self):
        with open('teacher.db.bak', 'wb+')as f:
            for line in conn.iterdump():
                data = line + '\n'
                data = data.encode("utf-8")
                f.write(data)
            reply = QMessageBox.information(self, '备份成功！', '备份文件为teacher.db.bak')

#导入 (excel)
    def openfile(self):
        #只获取前面的路径
        openfile_name,_ = QFileDialog.getOpenFileName(self,'选择文件','','Excel files(*.xls , *.xlsx)')
        print(openfile_name)
        if openfile_name == '':
            return

        xls = xlrd.open_workbook(str(openfile_name))
        table = xls.sheets()[0]
        data = list()
        n = table.nrows
        for i in range(1,n):
            data = table.row_values(i)
           # print("updata t set name = '"+str(data[1])+"',courses = '"+str(data[2])+"',ke = '"+str(data[3])+"' where id = '"+str(data[0])+"'")
            if c.execute("select * from t where id = '"+str(data[0])+"'").fetchall():
                c.execute("update t set name = '"+str(data[1])+"',courses = '"+str(data[2])+"',ke = '"+str(data[3])+"' where id = '"+str(data[0])+"'")
                conn.commit()
            else:
                c.execute("insert into t values(?,?,?,?) ",data)
                conn.commit()
        QMessageBox.information(self,"导入成功","导入完毕。")

#导出
    def savefile(self):
        n = c.execute("select * from t")
        all = n.fetchall()
        workbook = xlwt.Workbook()#创建一个空的工作簿

        sheet = workbook.add_sheet("TeacherSheet") #创建一个新表格

        index  = len(all)
        sheet.write(0,0,"id")
        sheet.write(0, 1, "name")
        sheet.write(0, 2, "courses")
        sheet.write(0, 3, "ke")

        for i in range(0,index):
            for j in range(0,len(all[i])):
                sheet.write(i+1,j,all[i][j])

        workbook.save("导出.xls")

        QMessageBox.information(self,"导出成功","文件为 导出.xls ")











# 启动
if __name__ == '__main__':
        app = QtWidgets.QApplication([])
        window = Ui_MainWindow()
        window.show()
        app.exec()