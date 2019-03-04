import Recorder
from PyQt5 import QtWidgets, QtGui, uic


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = uic.loadUi("gui.ui")
        self.connectButtonsToFunctions()
        self.initializeDropDown()

    def initializeDropDown(self):
        self.ui.agendaDropDown.addItem("Meeting Type 1")
        self.ui.agendaDropDown.addItem("Meeting Type 2")
        self.ui.agendaDropDown.addItem("Meeting Type 3")
        self.ui.agendaDropDown.addItem("Meeting Type 4")
        self.ui.agendaDropDown.addItem("Meeting Type 5")

    def getAgendaType(self):
        return self.ui.agendaDropDown.currentText()

    def appendInStatusBox(self,message):
        currentMsg = self.ui.statusBox.toPlainText()
        self.printInStatusBox(currentMsg+message)

    def printInStatusBox(self,message):
        self.ui.statusBox.setText(message)

    def getPhoneNumber(self):
        return self.ui.phoneNumberEntry.text()

    def connectButtonsToFunctions(self):
        try:
            self.ui.callButton.clicked.connect(self.callButtonClicked)
            self.ui.selectFileButton.clicked.connect(self.selectFileButtonClicked)
        except AttributeError as e:
            print("Either the object does not exist or it's connection function does not exist")
        except Exception as e:
            print(e)

    def callButtonClicked(self):
        phoneNumber = self.getPhoneNumber()
        # jabber = Jabber()
        # jabber.call(phoneNumber)
        self.recordingThread = Recorder.Recording()
        self.recordingThread.start()
        # while jabber.isCalling()
        #  pass
        self.recordingThread.stop()


    def selectFileButtonClicked(self):
        fileLocation, fileType = QtWidgets.QFileDialog.getOpenFileName()
        return fileLocation
