from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar
from PySide6.QtCore import Qt
import sys

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()

progress = QProgressBar()
progress.setMinimum(0)
progress.setMaximum(100)
progress.setValue(50)

#=========================================
#ここにコードを追加します
print(progress.minimum())
print(progress.maximum())

progress.setValue(70)
print(progress.value())

progress.setTextVisible(True)
print(progress.isTextVisible())

progress.setFormat("%p% 完了")
print(progress.format())

# progress.reset()

# progress.setInvertedAppearance(True)
print(progress.invertedAppearance())

progress.setOrientation(Qt.Vertical)
print(progress.orientation())
#=========================================

layout.addWidget(progress)
window.setLayout(layout)
window.show()
app.exec()