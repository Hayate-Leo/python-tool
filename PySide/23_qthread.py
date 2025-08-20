from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtCore import QThread, Signal
import sys, time

# Workerクラス（別スレッドで動く処理）
class Worker(QThread):
    progress = Signal(int)  # メインスレッドへ進捗を通知

    def run(self):
        for i in range(1, 6):
            time.sleep(1)  # 重たい処理の代わり
            print("処理1")
            QThread.msleep(500)  # 0.5秒スリープ
            print("処理2")
            QThread.sleep(2)  # 2秒停止
            self.progress.emit(i)  # 結果を通知
            print('重たい処理を実行中...')
            QThread.usleep(100)  # 100マイクロ秒停止
            print("高速処理")

# メインウィンドウ
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QThreadの基本")
        self.resize(300, 200)

        self.label = QLabel("待機中…", self)
        self.start_button = QPushButton("開始", self)
        self.terminate_button = QPushButton("強制終了", self)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.terminate_button)
        self.setLayout(layout)

        self.start_button.clicked.connect(self.start_thread)
        self.terminate_button.clicked.connect(self.terminate_thread)

    def start_thread(self):
        self.thread = Worker()
        self.thread.setPriority(QThread.HighestPriority)
        print(self.thread.priority())
        self.thread.progress.connect(self.update_label)
        self.thread.started.connect(lambda: print("スレッドが開始しました"))
        self.thread.finished.connect(lambda: print("スレッドが終了しました"))
        self.thread.start()
        print(self.thread.isRunning())
        # self.thread.wait()
        # print(self.thread.isFinished())
        print(QThread.currentThread()) 


    def terminate_thread(self):
        # self.thread.quit()
        self.thread.terminate()

    def update_label(self, value):
        self.label.setText(f"カウント: {value}")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
