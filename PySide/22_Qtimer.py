from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QProgressBar, QHBoxLayout
)
import sys, datetime


class TimerDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTimerデモ: 時計・カウンター・プログレスバー")
        self.resize(400, 200)

        # メインレイアウト
        layout = QVBoxLayout(self)

        # 時計エリア
        self.clock_label = QLabel("時計: --:--:--")
        layout.addWidget(self.create_clock_widget())

        # カウンターエリア
        self.counter_label = QLabel("カウンター: 0")
        layout.addWidget(self.create_counter_widget())

        # プログレスバーエリア
        self.progress = QProgressBar()
        layout.addWidget(self.create_progress_widget())

        # 各機能を開始
        self.start_clock()
        self.start_counter()
        self.start_progress()
        QTimer.singleShot(3000, lambda: print("3秒後に実行！"))

    # ---------- 時計 ----------
    def create_clock_widget(self):
        w = QWidget()
        box = QHBoxLayout(w)
        box.addWidget(self.clock_label)
        return w

    def start_clock(self):
        self.clock_timer = QTimer()
        self.clock_timer.timeout.connect(self.update_clock)
        self.clock_timer.setInterval(2000)
        print(self.clock_timer.interval())  # → 2000
        # self.clock_timer.setSingleShot(True)
        self.clock_timer.start()

    def update_clock(self):
        self.clock_label.setText(
            "時計: " + datetime.datetime.now().strftime("%H:%M:%S")
        )
        print(f'時計タイマー：{self.clock_timer.timerId()}')


    # ---------- カウンター ----------
    def create_counter_widget(self):
        w = QWidget()
        box = QHBoxLayout(w)
        box.addWidget(self.counter_label)
        return w

    def start_counter(self):
        self.count = 0
        self.counter_timer = QTimer()
        self.counter_timer.timeout.connect(self.update_counter)
        self.counter_timer.start(500)

    def update_counter(self):
        self.count += 1
        self.counter_label.setText(f"カウンター: {self.count}")
        if self.counter_timer.isActive():
            print("カウンターは動作中です")
            print(f'カウンタータイマー：{self.counter_timer.timerId()}')

    # ---------- プログレスバー ----------
    def create_progress_widget(self):
        w = QWidget()
        box = QHBoxLayout(w)
        box.addWidget(self.progress)
        return w

    def start_progress(self):
        self.value = 0
        self.progress_timer = QTimer()
        self.progress_timer.timeout.connect(self.update_progress)
        self.progress_timer.start(100)

    def update_progress(self):
        self.value += 1
        if self.value > 100:
            self.progress_timer.stop()
        self.progress.setValue(self.value)
        print(self.progress_timer.remainingTime())
        print(f'プログレスタイマー：{self.progress_timer.timerId()}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimerDemo()
    window.show()
    sys.exit(app.exec())
