from PyQt5 import QtWidgets
from gui import TopLevelWindow


if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = TopLevelWindow()
    window.show()

    app.exec_()
