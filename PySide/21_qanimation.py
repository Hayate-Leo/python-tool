from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import QPropertyAnimation, QRect, QAbstractAnimation
import sys

app = QApplication(sys.argv)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPropertyAnimationの例")
        self.resize(400, 300)

        self.button = QPushButton("動くボタン", self)
        self.button.setGeometry(50, 50, 100, 40)

        # アニメーション設定
        self.anim = QPropertyAnimation(self.button, b"geometry")
        self.anim.setTargetObject(self.button)
        self.anim.setPropertyName(b"geometry")
        self.anim.setDuration(5000)  # 1秒
        self.anim.setStartValue(QRect(50, 50, 100, 40))
        # self.anim.setStartValue(QRect(0, 0, 100, 30))
        self.anim.setEndValue(QRect(250, 200, 100, 40))
        self.anim.setLoopCount(1)  # 3回繰り返す
        time = self.anim.currentTime()
        print(time)

        # from PySide6.QtCore import QEasingCurve
        # self.anim.setEasingCurve(QEasingCurve.OutBounce)

        if self.anim.state() == QAbstractAnimation.Running:
            print("動作中")

        # self.anim.pause()
        # self.anim.resume()
        self.anim.setDirection(QAbstractAnimation.Backward)
        dir = self.anim.direction()
        print(dir)
        self.anim.start()
        self.anim.finished.connect(self.on_animation_finished)

    def on_animation_finished(self):
        print("アニメーションが終了しました！")

window = Window()
window.show()
sys.exit(app.exec())