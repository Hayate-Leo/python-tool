from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt
import sys

class CustomWidget(QWidget):
    # QWidgetをクラス継承
    def __init__(self):
        super().__init__()
        self.setWindowTitle("カスタムウィジェットの例")
        # setGeometry(x, y, width, height)
        self.setGeometry(100, 50, 600, 200)
        # resize(width, height)
        # self.resize(400, 300)
        self.move(300, 50)
        # self.setFixedSize(250, 150)
        self.setMinimumSize(100, 80)
        self.setMaximumSize(500, 400)
        self.update()  # paintEvent() が再度呼ばれる
        # self.setStyleSheet("border: 2px solid red; background-color: lightblue;")
        # self.setEnabled(False)  # 無効化
        self.setToolTip("これは説明文です")
        self.setCursor(Qt.PointingHandCursor)

    def paintEvent(self, event):
        # paintEvent() をオーバーライド
        painter = QPainter(self)
        # painter.setBrush(QColor("skyblue"))
        painter.setBrush(QColor("yellow"))
        painter.drawRect(50, 50, 200, 100)
    
    def mousePressEvent(self, event):
        print(f"クリック位置: {event.position()}")
    
    def keyPressEvent(self, event):
        print(f"押されたキー: {event.key()}")
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, "確認", "本当に終了しますか？")
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        

app = QApplication(sys.argv)
window = CustomWidget()
window.show()
# window.hide()
sys.exit(app.exec())  