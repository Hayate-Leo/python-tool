from PySide6.QtWidgets import QApplication, QListView, QMainWindow
from PySide6.QtCore import QStringListModel
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListView + QStringListModel")

        # データ（Pythonリスト）
        items = ["りんご", "みかん", "バナナ", "ぶどう"]

        # モデルを作成
        self.model = QStringListModel()
        self.model.setStringList(items)
        self.model.setStringList(["赤", "青", "緑"])
        print(self.model.stringList())
        self.model.insertRows(1, 2)  # 1行目から2行追加
        self.model.removeRows(0, 1)  # 先頭行を削除
        idx = self.model.index(0)
        self.model.setData(idx, "変更後の文字列")
        print(self.model.data(idx))
        print(self.model.rowCount())
        print(self.model.flags(idx))

        # ビューを作成
        self.view = QListView()
        self.view.setModel(self.model)

        self.setCentralWidget(self.view)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())