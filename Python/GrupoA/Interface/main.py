import sys
from PyQt5.QtWidgets import QApplication
from recorder import RecorderWindow

app = QApplication(sys.argv)

recorder = RecorderWindow()

sys.exit(app.exec_())
