from PySide6.QtWidgets import QApplication, QMainWindow, QListView, QLineEdit, QVBoxLayout, QWidget
from PySide6.QtCore import QStringListModel
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("検索付き QListView")

        # 元データ
        self.items = ["りんご", "みかん", "バナナ", "ぶどう", "パイナップル", "メロン"]

        # モデル
        self.model = QStringListModel(self.items)

        # ビュー
        self.view = QListView()
        self.view.setModel(self.model)

        # 検索ボックス
        self.search = QLineEdit()
        self.search.setPlaceholderText("ここに文字を入力すると検索できます")
        self.search.textChanged.connect(self.filter_list)

        # レイアウト
        layout = QVBoxLayout()
        layout.addWidget(self.search)
        layout.addWidget(self.view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def filter_list(self, text):
        if text:
            filtered = [item for item in self.items if text in item]
        else:
            filtered = self.items
        self.model.setStringList(filtered)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
