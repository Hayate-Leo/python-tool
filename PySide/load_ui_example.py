# load_ui_example.py
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys

app = QApplication(sys.argv)
loader = QUiLoader()
file = QFile(fr"C:\Users\kamis\python-tool\PySide\mainwindow.ui")
file.open(QFile.ReadOnly)
window = loader.load(file)
file.close()

window.show()
sys.exit(app.exec())