from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import denglu
import newmain

#连接数据库
conn = sqlite3.connect('teacher.db')
c = conn.cursor()

class Login_window(QtWidgets.QMainWindow,denglu.Ui_Form):
    def __init__(self):
        super(Login_window,self).__init__()
        self.setupUi(self)
        self.denglupushButton.clicked.connect(self.login)
        self.tuichupushButton.clicked.connect(self.exit)

#登陆
    def login(self):
        username = self.zhanghaolineEdit.text()
        password = self.passwordtext.text()
        if username =='' or password == '':
            reply = QMessageBox.warning(self,'错误！','用户名或密码不能为空')
            return
        isok = c.execute('select * from yonghu')
        a = isok.fetchall()
        print(a)
        for i in a:
            if i[0] == username and i[1] == password:
                reply = QMessageBox.information(self,'成功！','登陆成功！')
                Ui_Main.show()
                self.close()
            else :
                reply = QMessageBox.warning(self,'失败！','账号或密码错误')



#退出
    def exit(self):
        self.close()






#启动
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Login_window()
    Ui_Main = newmain.Ui_Main()
    window.show()
    app.exec()