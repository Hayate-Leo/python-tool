# runtime_load.py
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QLineEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

app = QApplication(sys.argv)
loader = QUiLoader()
ui_file = QFile("mainwindow.ui")
if not ui_file.open(QFile.ReadOnly):
    raise RuntimeError("Cannot open mainwindow.ui")

window = loader.load(ui_file)
ui_file.close()
if window is None:
    raise RuntimeError("Failed to load UI")

# Designerで設定した objectName を使ってウィジェットを取得
button = window.findChild(QPushButton, "pushButton")
line_edit = window.findChild(QLineEdit, "lineEdit")
label = window.findChild(QLabel, "label")

if button and line_edit and label:
    def on_click():
        label.setText(line_edit.text())
    button.clicked.connect(on_click)

window.show()
sys.exit(app.exec())
