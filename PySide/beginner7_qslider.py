from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider
from PySide6.QtCore import Qt
import sys

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()

slider = QSlider()
slider.setOrientation(Qt.Horizontal)
slider.setMinimum(0)
slider.setMaximum(100)
slider.setValue(50)

#========================================
#ここにコードを追加します
print(slider.minimum())
print(slider.maximum())

slider.setValue(10)
print(slider.value())

# slider.setOrientation(Qt.Vertical)
print(slider.orientation())

slider.setTickPosition(QSlider.TicksBelow)
print(slider.tickPosition())

slider.setTickInterval(20)
print(slider.tickInterval())

slider.setSingleStep(20)
print(slider.singleStep())

slider.setPageStep(10)
print(slider.pageStep())

slider.setTracking(True)
slider.valueChanged.connect(lambda value: print(f"値が変更されました: {value}"))
print(slider.hasTracking())


slider.sliderMoved.connect(lambda value: print(f"スライダーが動きました: {value}"))
#========================================

layout.addWidget(slider)
window.setLayout(layout)
window.show()
app.exec()