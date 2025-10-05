# theme_toggle_demo.py
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QLabel, QTextEdit
)
from PySide6.QtCore import Qt


class ThemeDemoApp(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("ダーク/ライト テーマ切替デモ")
        self.resize(640, 360)

        # UI
        main = QVBoxLayout()
        control_row = QHBoxLayout()

        self.toggle_btn = QPushButton("ライトに切替")
        self.toggle_btn.setCheckable(True)  # 押すと ON (ライト)
        self.toggle_btn.toggled.connect(self.on_toggle)

        # Add some sample widgets
        self.title = QLabel("ダークテーマサンプル")
        self.title.setObjectName("title")
        info = QLabel("以下はテーマによる見た目の違いを示すサンプルウィジェットです。")
        button = QPushButton("サンプルボタン")
        input_line = QLineEdit()
        input_line.setPlaceholderText("テキスト入力欄")
        text = QTextEdit()
        text.setPlainText("QTextEdit のサンプルテキスト。テーマ切替で色や枠が変わります。")

        control_row.addWidget(self.toggle_btn)
        control_row.addStretch()

        main.addLayout(control_row)
        main.addWidget(self.title)
        main.addWidget(info)
        main.addWidget(button)
        main.addWidget(input_line)
        main.addWidget(text)

        self.setLayout(main)

        # 初期はダーク
        self.apply_dark()

    def on_toggle(self, checked: bool):
        # checked == True -> ライトに切替
        if checked:
            self.apply_light()
        else:
            self.apply_dark()

    def apply_dark(self):
        theme = 'dark'
        with open(fr"C:\Users\kamis\python-tool\PySide\{theme}.qss", "r", encoding="utf-8") as f:
            self.app.setStyleSheet(f.read())
            print(f.read())
        self.toggle_btn.setText("ライトに切替")
        self.toggle_btn.setChecked(False)
        self.title.setText("ダークテーマサンプル")

    def apply_light(self):
        theme = 'light'
        with open(fr"C:\Users\kamis\python-tool\PySide\{theme}.qss", "r", encoding="utf-8") as f:
            self.app.setStyleSheet(f.read())
        self.toggle_btn.setText("ダークに切替")
        self.toggle_btn.setChecked(True)
        self.title.setText("ライトテーマサンプル")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = ThemeDemoApp(app)
    demo.show()
    sys.exit(app.exec())
