from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox
import sys

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()

combo = QComboBox()
combo.addItems(["選択肢1", "選択肢2", "選択肢3"])

# ========================================
# ここにコードを追加します
combo.setCurrentIndex(1)
index = combo.currentIndex()
print(f"現在の選択インデックス: {index}")

combo.setCurrentText("選択肢3")
text = combo.currentText()
print(f"現在の選択テキスト: {text}")

# アイテムの追加
# combo.addItem("新しい選択肢")
# combo.addItems(["A", "B", "C"])
combo.insertItem(1, "挿入された選択肢")
# アイテムの削除
combo.removeItem(0)
# combo.clear()
numbers = combo.count()
print(f"選択肢の数: {numbers}")

combo.setEditable(True)
print(f"編集可能か？: {combo.isEditable()}")

# アイテムの追加
combo.addItems(["A", "B", "C"])
# 表示されるアイテム数の最大値を設定
combo.setMaxVisibleItems(5)

combo.setEditable(True)
combo.setInsertPolicy(QComboBox.InsertAtTop)

from PySide6.QtWidgets import QCompleter
combo.setEditable(True)
completer = QCompleter(["候補1", "候補2", "候補3"])
combo.setCompleter(completer)

combo.activated.connect(lambda i: print(f"選ばれたインデックス: {i}"))

combo.currentIndexChanged.connect(lambda i: print(f"新しいインデックス: {i}"))

combo.addItem("追加されたデータ", userData=123)
data = combo.itemData(6)
print(f"追加されたデータ: {data}")

combo.setItemText(0, "新しいテキスト")
print(combo.itemText(0))
# ========================================

layout.addWidget(combo)

window.setLayout(layout)
window.show()
app.exec()