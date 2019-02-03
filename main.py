from PyQt5 import QtWidgets, QtGui, uic

from Recorder import mywindow

app = QtWidgets.QApplication([])
application = mywindow()
application.ui.show()
app.exec()
