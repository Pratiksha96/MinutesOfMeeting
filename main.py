from PyQt5 import QtWidgets, QtGui, uic

import UI

app = QtWidgets.QApplication([])
application = UI.mywindow()
application.ui.show()
app.exec()
