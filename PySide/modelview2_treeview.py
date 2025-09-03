from PySide6.QtWidgets import QApplication, QTreeView, QMainWindow
from PySide6.QtGui import QStandardItemModel, QStandardItem
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTreeView の基本")
        self.resize(400, 300)

        # モデル作成
        model = QStandardItemModel(0, 2)
        model.setHorizontalHeaderLabels(["項目名", "説明"])
        model.setHorizontalHeaderLabels(["カテゴリ", "説明"])

        # 階層データを追加
        # parent1 = QStandardItem("フルーツ")
        # parent1.appendRow([QStandardItem("リンゴ"), QStandardItem("赤い果物")])
        # parent1.appendRow([QStandardItem("バナナ"), QStandardItem("黄色い果物")])

        # parent2 = QStandardItem("野菜")
        # parent2.appendRow([QStandardItem("ニンジン"), QStandardItem("オレンジ色の野菜")])
        # parent2.appendRow([QStandardItem("キャベツ"), QStandardItem("緑の野菜")])

        # model.appendRow([parent1, QStandardItem("果物のカテゴリ")])
        # model.appendRow([parent2, QStandardItem("野菜のカテゴリ")])

        # TreeView 設定
        tree = QTreeView()
        tree.setModel(model)
        tree.expandAll()  # すべて展開して表示

        self.setCentralWidget(tree)

        root = model.invisibleRootItem()
        root.appendRow([QStandardItem("フォルダA"), QStandardItem("説明A")])

        parent = QStandardItem("親カテゴリ")
        desc   = QStandardItem("このカテゴリの説明")
        model.invisibleRootItem().appendRow([parent, desc])

        child1 = QStandardItem("子1")
        child1_desc = QStandardItem("子1の説明")
        parent.appendRow([child1, child1_desc])          # 末尾に追加

        parent.insertRow(0, [QStandardItem("先頭子"), QStandardItem("説明")])  # 先頭に挿入
        parent.removeRow(1)  # 2番目の子を削除

        # idx  = model.indexFromItem(parent)      # Item → Index
        # item = model.itemFromIndex(idx)         # Index → Item

        from PySide6.QtCore import Qt
        hits = model.findItems("親カテゴリ", flags=Qt.MatchContains | Qt.MatchRecursive, column=0)
        for it in hits:
            idx = model.indexFromItem(it)
            tree.setExpanded(idx, True)  # 見つけた項目を展開表示
            print(idx)

        from PySide6.QtWidgets import QAbstractItemView as AIV
        tree.setEditTriggers(AIV.NoEditTriggers)   # すべて禁止
        # 例：ダブルクリックで編集
        # tree.setEditTriggers(AIV.DoubleClicked)

        from PySide6.QtWidgets import QHeaderView
        tree.setHeaderHidden(True)
        tree.header().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        tree.header().setSectionResizeMode(1, QHeaderView.Stretch)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
