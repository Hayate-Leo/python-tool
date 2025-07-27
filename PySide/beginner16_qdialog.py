from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout,
    QLabel, QFileDialog, QWidget
)
import sys

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("カスタムダイアログ")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("これはQDialogです"))
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDialogとQFileDialog")

        btn_dialog = QPushButton("QDialogを開く")
        btn_dialog.clicked.connect(self.open_dialog)

        btn_file = QPushButton("ファイルを開く")
        btn_file.clicked.connect(self.open_file)

        layout = QVBoxLayout()
        layout.addWidget(btn_dialog)
        layout.addWidget(btn_file)

        container = self.centralWidget() or QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_dialog(self):
        dialog = CustomDialog()
        dialog.setWindowTitle("設定ダイアログ")
        # dialog.setModal(True)  # モーダルにする
        # self.dialog.open()  # モーダル表示
        # dialog.open()  # モデルレス表示
        result = dialog.exec()  # モーダル表示（結果を受け取れる）
        if result == QDialog.Accepted:
            print("OKが押されました")
        elif result == QDialog.Rejected:
            print("キャンセルされました")

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "ファイルを開く", "", "すべてのファイル (*)")
        if filename:
            print(f"選択されたファイル: {filename}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()