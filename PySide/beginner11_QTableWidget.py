from PySide6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()

table = QTableWidget()
table.setRowCount(3)
table.setColumnCount(2)
table.setHorizontalHeaderLabels(["名前", "年齢"])

table.setItem(0, 0, QTableWidgetItem("田中"))
table.setItem(0, 1, QTableWidgetItem("25"))

#==============================================
# ここにコードを追加します
table.setRowCount(5)       # 5行に設定
table.setColumnCount(6)    # 6列に設定

item1 = QTableWidgetItem("佐藤")
item2 = QTableWidgetItem("28")
table.setItem(1, 0, item1)  # (1, 0) のセルに「佐藤」を挿入
table.setItem(1, 1, item2)  # (1, 1) のセルに「28」を挿入

table.setHorizontalHeaderLabels(["名前", "年齢", "住所", "職業"])

value = table.item(0, 1).text()  # (0, 1) のセルのテキストを取得
print(value)

table.insertRow(1)   # 2行目の前に新しい行を挿入
table.removeRow(2)   # 3行目を削除

from PySide6.QtWidgets import QAbstractItemView
# table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 編集禁止

table.setSelectionBehavior(QAbstractItemView.SelectRows)    # 行単位で選択
# または
table.setSelectionBehavior(QAbstractItemView.SelectItems)   # セル単位で選択

# コンテンツを削除
# table.clearContents()

table.setAlternatingRowColors(True)  # TrueでON、FalseでOFF

# table.resizeColumnsToContents()

# 3x2の成績表のようなテーブルを作成
table.setRowCount(3)
table.setColumnCount(2)
table.setHorizontalHeaderLabels(["名前", "点数"])

students = [("山田", "85"), ("佐藤", "90"), ("鈴木", "78")]

for row, (name, score) in enumerate(students):
    table.setItem(row, 0, QTableWidgetItem(name))
    table.setItem(row, 1, QTableWidgetItem(score))
#==============================================
layout.addWidget(table)
window.setLayout(layout)
window.show()
app.exec()