from PySide6.QtWidgets import QApplication, QLabel
import sys

app = QApplication(sys.argv)
label = QLabel('Hello QLabel!')

# ======================
# ここにプロパティやメソッドを記入します
label.setText("Hello World!") # テキストの設定
current_text = label.text()    # テキスト取得
print(current_text)

# from PySide6.QtGui import QPixmap
# label.setPixmap(QPixmap("PySide/useful-python-logo.png"))  # 画像表示
# pix = label.pixmap()                 # 画像取得
# print(pix)

from PySide6.QtCore import Qt #ライブラリの読み込み
label.setAlignment(Qt.AlignCenter)   # 中央配置
align = label.alignment()            # 現在のアライメント取得
print(align)

label.setText("How to use PySide6.QtWidgets.QLabel") # テキストの設定
label.setWordWrap(True)   # 自動改行ON
wrap = label.wordWrap()   # 自動改行状態取得
print(wrap)

# label.setTextFormat(Qt.RichText)    # リッチテキストに変更
# fmt = label.textFormat()            # 現在の形式取得
# print(fmt)

# label.setText("<a href='https://www.useful-python.com/'>Useful-Python.com</a>")
# label.setOpenExternalLinks(True)
link = label.openExternalLinks()
fmt = label.textFormat() 
print(f'fmt: {fmt}, link: {link}')

# from PySide6.QtGui import QPixmap
# label.setPixmap(QPixmap("PySide/useful-python-logo.png"))  # 画像表示
# label.setScaledContents(True)
# scaled = label.hasScaledContents()
# print(scaled)

# label.setIndent(20)
# indent = label.indent()
# print(indent)

# label.setMargin(30)
# m = label.margin()
# print(m)

from PySide6.QtWidgets import QLineEdit # ライブラリの読み込み
label1 = QLabel("&Firstname:")                # Alt+F でショートカット指定（&が目印）
label2 = QLabel("&Lastname:")                # Alt+L でショートカット指定（&が目印）
line_edit1 = QLineEdit()                 # 入力フォーム
line_edit2 = QLineEdit()                 # 入力フォーム
label1.setBuddy(line_edit1)               # QLabelとQLineEditを関連付け（Buddy設定）
label2.setBuddy(line_edit2)               # QLabelとQLineEditを関連付け（Buddy設定）

b1 = label1.buddy()
b2 = label2.buddy()
print(b1)
print(b2)

# label.setStyleSheet("color: cyan;")
# css = label.styleSheet()
# print(css)         

from PySide6.QtGui import QFont
label.setFont(QFont("Arial", 14))
# ======================

label.show()
sys.exit(app.exec())