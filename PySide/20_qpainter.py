from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor, QPen, QFont, QPixmap
import sys

class PaintWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)  # QPainterを初期化
        painter.setPen(QPen(QColor("blue"), 3))  # ペン色と太さ
        # painter.setPen(QPen(QColor("red"), 2))
        painter.setBrush(QColor("skyblue"))      # 塗りつぶし色
        painter.setBrush(QColor("yellow"))
        # painter.drawRect(10, 10, 80, 40)
        # painter.drawLine(0, 0, 100, 100)
        painter.setFont(QFont("Arial", 14))
        # painter.drawText(80, 80, "Hello QPainter")
        # 線を滑らかにする
        # painter.setPen(QPen(QColor("red"), 3))  # ペン色と太さ
        # painter.drawText(30, 30, "QPainter.Antialiasing = ON")
        # painter.setRenderHint(QPainter.Antialiasing)
        # painter.drawEllipse(50, 50, 80, 80)

        # painter.rotate(45) # 回転
        # painter.translate(50, 50) #移動
        # painter.scale(2, 2)

        # pixmap = QPixmap("PySide/useful-python-logo.png")
        # painter.drawPixmap(0, 0, pixmap)
        # painter.begin(self)
        # 描画処理
        # painter.end()
        painter.save()
        painter.setBrush(QColor("red"))      # 塗りつぶし色
        painter.restore()
        # painter.setOpacity(0.5)
        painter.fillRect(0, 0, 100, 50, QColor("green"))
        painter.drawRect(50, 50, 100, 50)  # 四角形を描画


app = QApplication(sys.argv)
window = PaintWidget()
window.resize(300, 200)
window.show()
sys.exit(app.exec())