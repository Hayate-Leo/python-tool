from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox, QFrame, QLabel
import sys

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout()

# QGroupBox の例
group = QGroupBox("設定")
group_layout = QVBoxLayout()
group_layout.addWidget(QLabel("オプション1"))
group_layout.addWidget(QLabel("オプション2"))
group.setLayout(group_layout)
#=========================================
#ここにQGroupBoxのコードを追加します
group.setTitle("グループボックスのラベル設定")

label = group.title()
print(label)

group.setCheckable(True)
group.setChecked(False)

state = group.isChecked()
print(state)
# False
#=========================================

# QFrame の例
frame = QFrame()
frame.setFrameShape(QFrame.Box)
frame.setFrameShadow(QFrame.Sunken)
frame_layout = QVBoxLayout()
frame_layout.addWidget(QLabel("情報エリア"))
frame.setLayout(frame_layout)
#=========================================
#ここにQFrameのコードを追加します
frame.setFrameShape(QFrame.Panel)

frame.setFrameShadow(QFrame.Raised)
# frame.setFrameShadow(QFrame.Sunken)

frame.setLineWidth(2)

frame.setMidLineWidth(3)

shape = frame.frameShape()
print(shape)
# 2
#=========================================

layout.addWidget(group)
layout.addWidget(frame)
window.setLayout(layout)
window.setWindowTitle("QGroupBoxとQFrame")
window.show()

sys.exit(app.exec())