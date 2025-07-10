from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPlainTextEdit, QTextEdit
import sys

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()

plain_text = QPlainTextEdit()
# plain_text.setPlainText("これは QPlainTextEdit です")

rich_text = QTextEdit()
# rich_text.setHtml("<b>これは QTextEdit</b> です")

#=================================
#ここにコードを追加します
# plain_text.setPlainText("これは通常のテキストです")
# print(plain_text.toPlainText())
# rich_text.setPlainText("これは通常のテキストです")
# print(rich_text.toPlainText())

# rich_text.setHtml("<h3 style='color:red'>タイトル</h3>")
# print(rich_text.toHtml())

# plain_text.setReadOnly(True)
# rich_text.setReadOnly(True)

plain_text.setPlaceholderText("ここにメッセージを入力してください")
rich_text.setPlaceholderText("ここにメッセージを入力してください")

plain_text.setPlainText("これは通常のテキストです")
plain_text.appendPlainText("新しいログを追加しました")

rich_text.setHtml("<b>これは QTextEdit</b> です")
rich_text.append("<i>追加された情報</i>")

# plain_text.clear()
# rich_text.clear()

plain_text.textChanged.connect(lambda: print("テキストが変更されました"))
rich_text.textChanged.connect(lambda: print("テキストが変更されました"))

plain_text.setLineWrapMode(QPlainTextEdit.NoWrap)

# from PySide6.QtGui import QFont
# plain_text.setFont(QFont("Meiryo", 12, QFont.Bold))
# rich_text.setFont(QFont("Times", 12, QFont.Medium))

# from PySide6.QtGui import QTextCursor
# plain_text.moveCursor(QTextCursor.Start) # カーソルを先頭へ
# rich_text.moveCursor(QTextCursor.EndOfLine) # カーソルを行の末尾へ

plain_text.setPlainText("これは\tQPlainTextEdit です")
plain_text.setTabStopDistance(50.0) # 50ピクセル幅に設定

plain_text.setPlainText("Hello")  # 初期状態
plain_text.insertPlainText(" World")  # 「Hello World」となる
plain_text.undo()  # => 「Hello」に戻る（「 World」が消える）

rich_text.setPlainText("Hello")  # 初期状態
rich_text.insertPlainText(" World")  # 「Hello World」となる
rich_text.undo()  # => 「Hello」に戻る（「 World」が消える）
rich_text.redo()  # => 「Hello World」に戻る（消した「 World」を復元）
#=================================

layout.addWidget(plain_text)
layout.addWidget(rich_text)

window.setLayout(layout)
window.show()
app.exec()