import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QCoreApplication

# --- 高DPI対応を有効化 ---
# Qt 5.14 以降では基本的に自動対応するが、明示する方が安心
QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS入門：ボタンデザイン集")
        self.setFont(QFont("Meiryo", 12))

        layout = QVBoxLayout()

        # --- 色違いボタン ---
        primary_btn = QPushButton("標準のボタン")
        primary_btn.setObjectName("primaryBtn")
        primary_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        success_btn = QPushButton("Success")
        success_btn.setObjectName("successBtn")
        success_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        danger_btn = QPushButton("危険")
        danger_btn.setObjectName("dangerBtn")
        danger_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # --- アウトラインボタン ---
        outline_btn = QPushButton("アウトラインボタン")
        outline_btn.setObjectName("outlineBtn")
        outline_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # --- サイズ変更ボタン ---
        large_btn = QPushButton("大きいボタン")
        large_btn.setObjectName("largeBtn")
        large_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        small_btn = QPushButton("小さいボタン")
        small_btn.setObjectName("smallBtn")
        small_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # --- 幅いっぱいのボタン（Full Width） ---
        fixed_btn = QPushButton("固定のボタン")
        fixed_btn.setObjectName("fixedBtn")
        fixed_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        full_btn = QPushButton("可変のボタン")
        full_btn.setObjectName("fullBtn")
        full_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # --- 非アクティブ（無効化）ボタン ---
        disabled_btn = QPushButton("非アクティブ")
        disabled_btn.setObjectName("disabledBtn")
        disabled_btn.setEnabled(False)
        disabled_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # レイアウトに追加
        layout.addWidget(primary_btn)
        layout.addWidget(success_btn)
        layout.addWidget(danger_btn)
        layout.addWidget(outline_btn)
        layout.addWidget(large_btn)
        layout.addWidget(small_btn)
        layout.addWidget(fixed_btn)
        layout.addWidget(full_btn)
        layout.addWidget(disabled_btn)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open(r"C:\Users\kamis\python-tool\PySide\sytle.qss", "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
