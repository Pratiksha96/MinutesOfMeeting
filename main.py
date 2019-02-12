from PyQt5 import QtWidgets, QtGui, uic

import Recorder

app = QtWidgets.QApplication([])
application = Recorder.mywindow()
application.ui.show()
app.exec()
