from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

def on_button_clicked():
    print("Button clicked!")

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()

button = QPushButton("Click Me")        # ボタンのテキストを設定
button.clicked.connect(on_button_clicked) # ボタンクリック時の処理を接続

# ======================
# ここにプロパティやメソッドを記入します
button.setText("開始")
text = button.text()
print(text)

from PySide6.QtGui import QIcon
button.setIcon(QIcon("Pyside/useful-python-logo.png"))
icon = button.icon()
print(icon)

button.setCheckable(True)
checkable = button.isCheckable()
print(checkable)

# button.setChecked(True)
# checked = button.isChecked()
# print(checked)

# button.toggle()

from PySide6.QtGui import QKeySequence
button.setShortcut(QKeySequence("Ctrl+S"))
sc = button.shortcut()
print(sc)

# button.setEnabled(False)
# enabled = button.isEnabled()
# print(enabled)

button.setToolTip("クリックして実行")
tip = button.toolTip()
print(tip)

# button.setStyleSheet("background-color: yellow; font-weight: bold;")
# css = button.styleSheet()
# print(css)

# チェック可能の切り替え
button.setCheckable(True)

def on_toggle():
    """チェックONOFFごとに設定"""
    if button.isChecked():
        statustext = "ON状態"
        button.setText(statustext)
        print(statustext)
    else:
        statustext = "OFF状態"
        button.setText(statustext)
        print(statustext)
# クリック時に発行されるシグナル
button.clicked.connect(on_toggle)
# ======================

layout.addWidget(button)
window.setLayout(layout)

window.show()
app.exec()