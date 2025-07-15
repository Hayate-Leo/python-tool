from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QLabel, QVBoxLayout
import sys

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout()

# QTabWidgetの作成
tabs = QTabWidget()

# タブの中身となるウィジェット
tab1 = QLabel("タブ1の内容")
tab2 = QLabel("タブ2の内容")

# タブにウィジェットを追加
tabs.addTab(tab1, "タブ1")
tabs.addTab(tab2, "タブ2")

#================================================
#ここにコードを追加します
tabs.addTab(QWidget(), "詳細")

tabs.insertTab(1, QWidget(), "新規")

tabs.removeTab(0)
index = tabs.currentIndex()
print(index)
# 0

tabs.setCurrentIndex(1)

n = tabs.count()
print(n)
# 3

tabs.setTabText(0, "設定")

text = tabs.tabText(1)
print(text)
# タブ2

tabs.setTabToolTip(0, "設定画面")

tabs.setTabEnabled(1, False)
tabs.setTabsClosable(True)

def close_tab(index):
    tabs.removeTab(index)

tabs.tabCloseRequested.connect(close_tab)

from PySide6.QtWidgets import QTabWidget
tabs.setTabPosition(QTabWidget.West)

tabs.setMovable(True)
#================================================

layout.addWidget(tabs)
window.setLayout(layout)
window.setWindowTitle("QTabWidgetの基本")
window.show()

sys.exit(app.exec())