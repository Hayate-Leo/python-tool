from PySide6.QtWidgets import QApplication, QMainWindow, QListView
from PySide6.QtGui import QStandardItemModel, QStandardItem
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("チェック付き QListView")

        # モデル
        self.model = QStandardItemModel()

        # データを追加（チェック可能にする）
        for fruit in ["りんご", "みかん", "バナナ", "ぶどう"]:
            item = QStandardItem(fruit)
            item.setCheckable(True)
            self.model.appendRow(item)

        # ビュー
        self.view = QListView()
        self.view.setModel(self.model)

        self.setCentralWidget(self.view)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
