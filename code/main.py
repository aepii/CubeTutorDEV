from PyQt5 import QtWidgets
from gui import TopLevelWindow
from web_scraper import SpeedCubeDB
import sys

if __name__ == "__main__":

    speedCubeDB = SpeedCubeDB()
    speedCubeDB = speedCubeDB.write_data(["PLL", "OLL", "F2L"])

    app = QtWidgets.QApplication(sys.argv)
    window = TopLevelWindow()
    window.show()

    app.exec_()
