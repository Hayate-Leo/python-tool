from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QDoubleSpinBox
import sys

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()

# QSpinBox
spinbox = QSpinBox()
spinbox.setMinimum(0) #最小値
spinbox.setMaximum(100) #最大値
spinbox.setValue(10) #現在値

# QDoubleSpinBox
doublespinbox = QDoubleSpinBox()
doublespinbox.setMinimum(0.0) #最小値
doublespinbox.setMaximum(100.0) #最大値
doublespinbox.setDecimals(2) #桁数設定
doublespinbox.setValue(10.5) #現在値

#============================
#ここにコードを追加してください
print(spinbox.minimum())
print(doublespinbox.minimum())

print(spinbox.maximum())
print(doublespinbox.maximum())

spinbox.setSingleStep(2)
print(spinbox.singleStep())

doublespinbox.setSingleStep(0.2)
print(doublespinbox.singleStep())

# spinbox.setPrefix("¥")
# print(spinbox.prefix())

# doublespinbox.setPrefix("$")
# print(doublespinbox.prefix())

spinbox.setSuffix(" kg")
print(spinbox.suffix())

doublespinbox.setSuffix(" m")
print(doublespinbox.suffix())

spinbox.setWrapping(True)
print(spinbox.wrapping())

doublespinbox.setWrapping(True)
print(doublespinbox.wrapping())

spinbox.valueChanged.connect(lambda v: print(f"SpinBox 値: {v}"))
doublespinbox.valueChanged.connect(lambda v: print(f"DoubleSpinBox 値: {v}"))

spinbox.setDisplayIntegerBase(16)  # 16進数表示
print(spinbox.displayIntegerBase())

doublespinbox.setDecimals(3)
print(doublespinbox.decimals())
#============================

layout.addWidget(spinbox)
layout.addWidget(doublespinbox)
window.setLayout(layout)
window.show()
app.exec()