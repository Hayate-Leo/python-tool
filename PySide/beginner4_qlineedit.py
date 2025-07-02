from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
import sys

def on_text_changed(text):
    print("入力された内容:", text)

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()

line_edit = QLineEdit()
line_edit.setPlaceholderText("ここに入力")  # 入力欄に薄く表示されるヒントテキスト
line_edit.textChanged.connect(on_text_changed)  # 入力変更時に呼ばれる関数を接続

# ==================================
# ここにプロパティやメソッドを記入します
# line_edit.setText("山田太郎")
# text = line_edit.text()
# print(text)

line_edit.setPlaceholderText("名前を入力してください")
holder = line_edit.placeholderText()
print(holder)

from PySide6.QtWidgets import QLineEdit
# line_edit.setEchoMode(QLineEdit.Password)
# line_edit.setEchoMode(QLineEdit.NoEcho)
mode = line_edit.echoMode()
print(mode)
# QLineEdit.EchoMode.Password が返る

line_edit.setMaxLength(10)
print(line_edit.maxLength())
# 10

line_edit.setText("テスト")
line_edit.clear()
print(line_edit.text())
# 空文字列

# line_edit.setReadOnly(True)
# print(line_edit.isReadOnly())
# True

# from PySide6.QtGui import QIntValidator
# validator = QIntValidator()
# line_edit.setValidator(validator)
# バリデータの動作はGUI上で確認

# from PySide6.QtCore import Qt
# line_edit.setAlignment(Qt.AlignRight)
# line_edit.setAlignment(Qt.AlignLeft)
# line_edit.setAlignment(Qt.AlignCenter)
# print(line_edit.alignment())
# Qt.AlignmentFlag.AlignRight

# line_edit.setText("テスト")
# line_edit.setCursorPosition(0)  # 先頭に移動
# print(line_edit.cursorPosition())
# 0

line_edit.editingFinished.connect(lambda: print("入力完了"))
# フォーカスアウトか Enter キーで "入力完了" が表示される

# line_edit.setInputMask("0000-00-00")  # 年月日形式
# print(line_edit.inputMask())
# 0000-00-00

from PySide6.QtWidgets import QCompleter
completer = QCompleter(["apple", "banana", "cherry"])
line_edit.setCompleter(completer)

line_edit.setDragEnabled(True)
print(line_edit.dragEnabled())
# True

# line_edit.setText("PySide6")
# line_edit.setSelection(0, 6)  # "PySide" を選択
# print(line_edit.selectedText())
# # PySide

line_edit.setStyleSheet("color: red; background-color: yellow;")
# ==================================

layout.addWidget(line_edit)
window.setLayout(layout)

window.show()
app.exec()