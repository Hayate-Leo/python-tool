from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

def on_button_clicked():
    print("Button clicked!")

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()

button = QPushButton("Click Me")        # ボタンのテキストを設定
button.clicked.connect(on_button_clicked) # ボタンクリック時の処理を接続

layout.addWidget(button)
window.setLayout(layout)

window.show()
app.exec()