import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtGui import QFont

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS入門：ボタンデザイン集")
        self.setFont(QFont("Meiryo", 12))

        layout = QVBoxLayout()

        # --- 色違いボタン ---
        primary_btn = QPushButton("標準のボタン: Primary")
        primary_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        primary_btn.setStyleSheet("""
            QPushButton {
                font-family: 'Yu Gothic UI';
                background-color: #007bff;
                color: white;
                border-radius: 6px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)

        success_btn = QPushButton("Success")
        success_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        success_btn.setStyleSheet("""
            QPushButton {
                font-family: 'Arial';
                background-color: #28a745;
                color: white;
                border-radius: 6px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #1e7e34;
            }
        """)

        danger_btn = QPushButton("Danger")
        danger_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        danger_btn.setStyleSheet("""
            QPushButton {
                font-family: 'Meiryo';
                background-color: #dc3545;
                color: white;
                border-radius: 6px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #a71d2a;
            }
        """)

        # --- アウトラインボタン ---
        outline_btn = QPushButton("アウトラインボタン")
        outline_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        outline_btn.setStyleSheet("""
            QPushButton {
                font-family: 'Meiryo';
                background-color: transparent;
                color: #007bff;
                border: 2px solid #007bff;
                border-radius: 6px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #007bff;
                color: white;
            }
        """)
        outline_btn.setObjectName("outlineBtn")
        app.setStyleSheet("""
        QPushButton#outlineBtn { border: 2px solid #007bff; background-color: transparent; }
        QPushButton#outlineBtn:hover { background-color: #007bff; color: white; }
        """)

        # --- サイズ変更ボタン ---
        large_btn = QPushButton("大きいボタン")
        large_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        large_btn.setStyleSheet("""
            QPushButton {
                font-family: 'Meiryo';
                background-color: #6c757d;
                color: white;
                font-size: 18px;
                border-radius: 6px;
                padding: 12px 24px;
            }
        """)

        small_btn = QPushButton("小さいボタン")
        small_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        small_btn.setStyleSheet("""
            QPushButton {
                font-family: 'Meiryo';
                background-color: #6c757d;
                color: white;
                font-size: 12px;
                border-radius: 6px;
                padding: 4px 8px;
            }
        """)

        # --- 幅いっぱいのボタン（Full Width） ---
        fixed_btn = QPushButton("固定のボタン")
        fixed_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        fixed_btn.setStyleSheet("""
            QPushButton {
                font-family: 'Meiryo';
                font-weight: bold;
                background-color: #17a2b8;
                color: white;
                font-size: 16px;
                border-radius: 6px;
                padding: 10px;
            }
        """)
        
        full_btn = QPushButton("可変のボタン")
        full_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        full_btn.setStyleSheet("""
            QPushButton {
                font-family: 'Meiryo';
                font-weight: bold;
                background-color: #17a2b8;
                color: white;
                font-size: 16px;
                border-radius: 6px;
                padding: 10px;
            }
        """)

        # --- 非アクティブ（無効化）ボタン ---
        disabled_btn = QPushButton("非アクティブ")
        disabled_btn.setEnabled(False)
        disabled_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        disabled_btn.setStyleSheet("""
            QPushButton {
                font-family: 'Meiryo';
                background-color: #6c757d;
                color: #d6d6d6;
                border-radius: 6px;
                padding: 8px 16px;
            }
        """)

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
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
