from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QGridLayout
)

app = QApplication([])

# HBoxLayout例
hbox = QHBoxLayout()
hbox_button1 = QPushButton("Button 1")
hbox_button2 = QPushButton("Button 2")
hbox.addWidget(hbox_button1)
hbox.addWidget(hbox_button2)

# VBoxLayout例
vbox = QVBoxLayout()
vbox.addWidget(QPushButton("Button A"))
vbox.addWidget(QPushButton("Button B"))

# GridLayout例
grid = QGridLayout()
grid.addWidget(QPushButton("Top-Left"), 0, 0)
grid.addWidget(QPushButton("Top-Right"), 0, 1)
grid.addWidget(QPushButton("Bottom"), 1, 0, 1, 2)

#==========================
# ここにコードを追加します
# hbox.addWidget(QPushButton("追加ボタン"))
# vbox.addWidget(QPushButton("追加ボタン"))
# grid.addWidget(QPushButton("追加ボタン"), 2, 0)

# grid.addLayout(hbox, 2, 0)
# grid.addLayout(vbox, 2, 1)

# hbox.addSpacing(30)
# hbox.addStretch()
# hbox.setSpacing(30)

# hbox.setContentsMargins(0, 0, 0, 0)

# 配置位置の調整
from PySide6.QtCore import Qt
hbox.setAlignment(hbox_button1, Qt.AlignLeft)
hbox.setAlignment(hbox_button2, Qt.AlignRight)

item1 = hbox.itemAt(0).widget()
item2 = hbox.itemAt(1).widget()
print(f'Button 1: {item1}')
print(f'Button 2: {item2}')
# Button 1: <PySide6.QtWidgets.QPushButton(0x194411dba30) at 0x000001944182CBC0>
# Button 2: <PySide6.QtWidgets.QPushButton(0x194411dbbf0) at 0x000001944182CC40>

n = hbox.count()
print(n)
# 2

# hbox.takeAt(0)
hbox.insertWidget(1, QPushButton("中間ボタン"))
#==========================

# メインウィンドウにレイアウトを適用
window = QWidget()
window.setLayout(hbox)  # ←他のレイアウトに差し替えてもOK
# window.setLayout(vbox)  # ←他のレイアウトに差し替えてもOK
# window.setLayout(grid)  # ←他のレイアウトに差し替えてもOK
window.show()
app.exec()