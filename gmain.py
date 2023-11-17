import sys

from PyQt5 import QtWidgets

from ui import Ui_MainWindow


def F5(x, k, m):
    return k * x + m


class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.calcBtn.clicked.connect(self.calc)

    def calc(self):
        self.resultBox.setPlainText("")
        a = self.aBox.value()
        b = self.bBox.value()
        h = self.hBox.value()
        k = self.kBox.value()
        m = self.mBox.value()
        x = a
        i = 1
        out = "№          x       f(x)\n"
        while (x <= b):
            out += str(i) + " " + "{:10.4f}".format(x) + " " + "{:10.4f}".format(F5(x, k, m)) + "\n"
            x += h
            i += 1
        self.resultBox.setPlainText(out)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()
