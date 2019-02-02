from PyQt5 import QtWidgets, QtGui, uic
import sys
import threading


class Recording(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.shutdownFlag = threading.Event()

    def run(self):
        while not self.stopped():
            print("hello")

    def stop(self):
        self.shutdownFlag.set()

    def stopped(self):
        return self.shutdownFlag.is_set()

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = uic.loadUi("gui.ui")
        self.connectButtonsToFunctions()

    def printInTextBox(self,message):
        self.ui.displayText.setText(message)

    def connectButtonsToFunctions(self):
        try:
            self.ui.startButton.clicked.connect(self.startButtonClicked)
            self.ui.stopButton.clicked.connect(self.stopButtonClicked)
        except AttributeError as e:
            print("Either the object does not exist or it's connection function does not exist")
        except Exception as e:
            print(e)

    def startButtonClicked(self):
        print("startButtonClicked")
        self.recordingThread = Recording()
        self.recordingThread.start()

    def stopButtonClicked(self):
        print("stopButtonClicked")
        self.recordingThread.stop()

app = QtWidgets.QApplication([])
application = mywindow()
application.ui.show()
app.exec()
