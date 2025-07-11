# from PySide6.QtWidgets import QApplication, QTextBrowser
# import sys

# app = QApplication(sys.argv)
# browser = QTextBrowser()

# html = """
# <h1>ようこそ</h1>
# <p>これは <a href="https://www.python.org">Python公式サイト</a> へのリンクです。</p>
# """
# browser.setHtml(html)

# # ========================================
# # ここにコードを追加します
# # from PySide6.QtCore import QUrl
# # # ページを探すディレクトリを指定
# # browser.setSearchPaths(["PySide/pages"])
# # # 初期表示ページを設定
# # browser.setSource(QUrl("page1.html"))
# # print(browser.source().toString())

# # リンクを外部ブラウザで開く
# browser.setOpenExternalLinks(True)

# # 内部リンクを自動的に開く
# from PySide6.QtCore import QUrl
# # ページを探すディレクトリを指定
# browser.setSearchPaths(["PySide/pages"])
# # 初期表示ページを設定
# browser.setSource(QUrl("page1.html"))
# # 内部リンクを自動的に開く
# browser.setOpenLinks(True)

# # html = "<p><a href='https://example.com'>リンク</a></p>"
# # browser.setHtml(html)

# def on_link_clicked(url): 
#     print("リンクがクリックされました:", url.toString())
# browser.anchorClicked.connect(on_link_clicked)

# browser.backward()
# browser.forward()
# browser.reload()
# # ========================================

# browser.show()
# app.exec()

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextBrowser, QPushButton
from PySide6.QtCore import QUrl
import sys

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout()

browser = QTextBrowser()
browser.setSearchPaths(["PySide/pages"])
browser.setSource(QUrl("page1.html"))
browser.setOpenLinks(True)

# ボタンを追加
back_button = QPushButton("戻る")
forward_button = QPushButton("進む")
reload_button = QPushButton("再読み込み")

back_button.clicked.connect(browser.backward)
forward_button.clicked.connect(browser.forward)
reload_button.clicked.connect(browser.reload)

# レイアウトに追加
layout.addWidget(browser)
layout.addWidget(back_button)
layout.addWidget(forward_button)
layout.addWidget(reload_button)

window.setLayout(layout)
window.show()
app.exec()