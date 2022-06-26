# This is a sample Python script.
import random

import drawRect
import time
import pyautogui
from mw import Ui_MainWindow
import sys
from drawRect import RectDrawer
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem

listSubsistem = list()


class EveEchoBott:
    state = "none"
    Amplifaing = False

    def __init__(self):
        self.state = "none"


class ShipSubsistem:
    def __init__(self):
        self.ButonPosition = 0
        self.WidgetInList: QListWidgetItem = None
        self.status = "online"
        self.timer = 0

    def Update(self):
        self.WidgetInList.setText("Amplifer" + self.status + str(self.ButonPosition) + str(self.timer))

        if self.status == "online" and self.timer == 0:
            return

        self.timer += round(tickTime)

        if self.timer <= 22:
            self.status = "worck"

        if self.timer == 23:
            EveEchoBott.Amplifaing = False;
            self.status = "offline"

        if self.timer == 85:
            self.timer = 0
            self.status = "online"

    def Activate(self):
        pyautogui.click(self.ButonPosition[0]+random.randrange(3,50), self.ButonPosition[1]+random.randrange(3,50),interval=0.25)
        self.status = "worck"
        self.timer = 1
        EveEchoBott.Amplifaing=True;
        print("twst")


def getStatus():
    global TimeMeshureL
    global TimeMeshureF
    TimeMeshureL = time.time()
    global tickTime
    tickTime = TimeMeshureL - TimeMeshureF
    TimeMeshureF = TimeMeshureL

    print(EveEchoBott.Amplifaing)

    if not EveEchoBott.Amplifaing:
        for system in listSubsistem:
            if system.status == "online":
                system.Activate()
                break

    for system in listSubsistem:
        system.Update()
        RectDrawer.Draw(system.ButonPosition)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    TimeMeshureF = time.time()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    MainWindow.show()

    sabsys = list(pyautogui.locateAllOnScreen('Screenshot_4.png', confidence=0.99))
    for rec in sabsys:
        subsis: ShipSubsistem = ShipSubsistem()
        subsis.ButonPosition = rec
        subsis.WidgetInList = QListWidgetItem("Amplifer" + str(rec), ui.listWidget)
        listSubsistem.append(subsis)

    # Setup base ui

    timer = QTimer()

    timer.timeout.connect(getStatus)  # execute `display_time`
    timer.setInterval(1000)  # 1000ms = 1s
    timer.start()

    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
