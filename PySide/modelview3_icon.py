from PySide6.QtWidgets import QApplication, QMainWindow, QListView
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("アイコン付き QListView")

        # モデル
        self.model = QStandardItemModel()

        # アイテム（アイコン付き）
        fruits = [("りんご", "🍎"), ("みかん", "🍊"), ("バナナ", "🍌")]
        for name, emoji in fruits:
            item = QStandardItem(f"{emoji} {name}")
            self.model.appendRow(item)

        # ビュー
        self.view = QListView()
        self.view.setModel(self.model)

        self.setCentralWidget(self.view)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
