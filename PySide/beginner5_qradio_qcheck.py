from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QRadioButton, QButtonGroup
import sys

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()
# チェックボタン
checkbox = QCheckBox("同意する")
# ラジオボタン
radio1 = QRadioButton("選択肢 1")
radio2 = QRadioButton("選択肢 2")
# グループ化
group = QButtonGroup()
group.addButton(radio1)
group.addButton(radio2)
# ======================================
# ここにコードを入力してカスタムします
def on_state_changed(state):
    print(f"チェック状態が変わりました: {state}")

checkbox.stateChanged.connect(on_state_changed)

# checkbox.setChecked(True)
# print(checkbox.isChecked())
# True

checkbox.setTristate(True)
print(checkbox.isTristate())

from PySide6.QtCore import Qt
checkbox.setCheckState(Qt.PartiallyChecked)
print(checkbox.checkState())  # Qt.Unchecked / Qt.Checked / Qt.PartiallyChecked

from PySide6.QtWidgets import QStyleOptionButton
option = QStyleOptionButton()
checkbox.initStyleOption(option)

radio1.setChecked(True)
print(radio1.isChecked())  # True or False
print(radio2.isChecked())  # True or False

radio1.toggled.connect(lambda checked: print(f"選択状態: {checked}"))

checkbox.setText("同意します")
radio1.setText("Pure Python派")
radio2.setText("Anaconda派")
text = checkbox.text()
print(text)
# ======================================
layout.addWidget(checkbox)
layout.addWidget(radio1)
layout.addWidget(radio2)

window.setLayout(layout)
window.show()
app.exec()