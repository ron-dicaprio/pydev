# -*- endoding=utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import time
import py_translate
print('time1:', time.time())
class youdaofanyi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.buttonClicked()

    def initUI(self):
        self.setWindowTitle('有道翻译器V1.0')
        self.setWindowIcon(QIcon('logo.png'))
        # 自定义窗口大小
        self.resize(600, 700)
        # windows窗口的位置
        self.move(700, 200)
        # 文本框位置
        self.text_area1 = QTextEdit(self)
        # 窗口位置
        self.text_area1.move(20, 20)
        self.text_area1.resize(440,280)
        #文本框位置
        self.text_area2 = QTextBrowser(self)
        #窗口位置
        self.text_area2.move(20, 350)
        #窗口区域大小
        self.text_area2.resize(440, 288)

        btn1 = QPushButton('操作', self)
        btn1.move(480, 80)

        self.show()
        self.statusBar().showMessage('兴趣永远是最好的老师！')
        btn1.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        textcontenct = self.text_area1.toPlainText()
        if textcontenct == '':
            pass
        else:
            self.text_area2.clear()
            result = py_translate.youdao_translate(textcontenct)
            self.text_area2.append(result)
            self.statusBar().showMessage("[%s]翻译成功！" % (result))
        print('time2:',time.time())

    #自定义退出事件
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', "你确定要退出么?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = youdaofanyi()
    sys.exit(app.exec_())

'''
# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import py_translate
import sys

class tanslate(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.buttonClicked()

    def initUI(self):
        self.setWindowTitle('有道翻译器V1.0')

        self.setWindowIcon(QIcon('logo.png'))
        # 自定义窗口大小
        self.resize(600, 700)
        # windows窗口的位置
        self.move(700, 200)
        #增加按钮
        btn1 = QPushButton("确认翻译", self)
        #按钮位置
        btn1.move(0, 100)
        #文本框位置
        self.text_area1 = QTextEdit(self)
        #窗口位置
        self.text_area1.move(100, 40)
        #窗口区域大小
        self.text_area1.resize(450, 300)

        #增加按钮
        btn2 = QLabel("翻译结果", self)
        #按钮位置
        btn2.move(20, 400)
        #文本框位置
        self.text_area2 = QTextBrowser(self)
        #窗口位置
        self.text_area2.move(100, 380)
        #窗口区域大小
        self.text_area2.resize(450, 300)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('菜单')
        #fileMenu2 = menubar.addMenu('工具')
        #fileMenu3 = menubar.addMenu('帮助')
        impMenu = QMenu('翻译器', self)
        #impMenu2 = QMenu('开发者', self)
        impAction = QAction('确认翻译', self)
        #impAction2 = QAction('关于软件', self)
        impMenu.addAction(impAction)
        #impMenu2.addAction(impAction2)
        fileMenu.addMenu(impMenu)
        #fileMenu2.addMenu(impMenu2)
        self.show()
        btn1.clicked.connect(self.buttonClicked)
        self.statusBar().showMessage("有道词典V1.0")
        #impAction.clicked.connect(self.buttonClicked2)


    def buttonClicked(self):
        #判断要翻译的内容是否为空
        textcontenct = self.text_area1.toPlainText()
        #内容为空就不调用接口
        if textcontenct == '':
            pass
        else:
            try:
                result = py_translate.youdao_translate(textcontenct)
                self.text_area2.clear()
                self.text_area2.append(result)
                self.statusBar().showMessage("%s 翻译完毕！" % (textcontenct))

            except Exception as e:
                print(self.text_area2.append(e))


    #自定义退出事件
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', "你确定要退出么?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    #键盘退出事件
    #def keyPressEvent(self, esc):
    #    if esc.key() == Qt.Key_Escape:
    #       self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = tanslate()
    sys.exit(app.exec_())
  
'''
