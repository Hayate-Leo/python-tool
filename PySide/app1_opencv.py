import sys
import cv2
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QImage, QPixmap


class CameraApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("リアルタイム画像解析アプリ（明るさ判定）")

        # --- UI ---
        self.video_label = QLabel("カメラ映像")
        self.result_label = QLabel("判定待ち...")
        self.result_label.setStyleSheet("font-size: 20pt; font-weight: bold;")
        self.result_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

        # --- カメラ設定 ---
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.result_label.setText("カメラが見つかりません")
            return

        # --- タイマーで更新 ---
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(100)  # 100msごとにフレーム更新

    # 判定処理の中で切り替え
    def update_result(self, result, brightness):
        self.result_label.setText(f"判定結果: {result} (明るさ={brightness:.1f})")
        if result == "OK":
            self.result_label.setStyleSheet("""
                color: white;
                font-weight: bold;
                background-color: blue;
                font-size: 32pt;
            """)
        else:
            self.result_label.setStyleSheet("""
                color: white;
                font-weight: bold;
                background-color: red;
                font-size: 32pt;
            """)

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        # --- 画像解析: 明るさを計算 ---
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        brightness = gray.mean()
        result = "OK" if brightness > 100 else "NG"
        
        # --- 判定を表示 ---
        self.update_result(result, brightness)

        # --- PySide用に変換して表示 ---
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        qimg = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
        self.video_label.setPixmap(QPixmap.fromImage(qimg))

    def closeEvent(self, event):
        """ウィンドウを閉じるときにカメラを解放"""
        if self.cap.isOpened():
            self.cap.release()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CameraApp()
    win.show()
    sys.exit(app.exec())
