import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QLineEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QSortFilterProxyModel, Qt, QRegularExpression

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 元のモデルを作成
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["名前", "年齢"])
        data = [("田中太郎", 25), ("佐藤花子", 30), ("鈴木一郎", 28), ("Sara", 34), ("Bob", 41)]
        for name, age in data:
            model.appendRow([QStandardItem(name), QStandardItem(str(age))])

        # Proxyモデルを作成（フィルタ機能付き）
        self.proxy = QSortFilterProxyModel()
        self.proxy.setSourceModel(model)
        self.proxy.setFilterKeyColumn(0)  # 名前の列でフィルタする
        orig = self.proxy.sourceModel()
        if orig is not None:
            print("元モデルの行数:", orig.rowCount())
        col = self.proxy.filterKeyColumn()
        print("フィルタ対象列:", col)

        rx = QRegularExpression("^田中")
        # self.proxy.setFilterRegularExpression(rx)
        if rx.isValid():
            print("現在のパターン:", rx.pattern())
        else:
            print("正規表現が未設定または無効です")

        # 大文字小文字を区別せずに検索（推奨）
        self.proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)
        # self.proxy.sort(1, Qt.AscendingOrder)

        # テーブルビュー
        self.view = QTableView()
        self.view.setModel(self.proxy)

        # 検索入力欄
        self.search = QLineEdit()
        self.search.setPlaceholderText("名前で検索…")
        self.search.textChanged.connect(self.filter_changed)

        layout = QVBoxLayout()
        layout.addWidget(self.search)
        layout.addWidget(self.view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def filter_changed(self, text):
        # 正規表現を使ったフィルタ
        self.proxy.setFilterRegularExpression(text)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
