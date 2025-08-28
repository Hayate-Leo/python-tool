from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableView + QStandardItemModel 入門")

        # 1) モデル作成（行3・列2）
        model = QStandardItemModel(3, 2, self)
        model.setHorizontalHeaderLabels(["名前", "年齢"])

        # 2) データ投入（QStandardItem を使う）
        model.setItem(0, 0, QStandardItem("Alice"))
        model.setItem(0, 1, QStandardItem("23"))
        model.setItem(1, 0, QStandardItem("Bob"))
        model.setItem(1, 1, QStandardItem("31"))
        model.setItem(2, 0, QStandardItem("Charlie"))
        model.setItem(2, 1, QStandardItem("28"))
        

        # 3) View にモデルをセット
        view = QTableView(self)
        view.setModel(model)
        m = view.model()
        print(m)

        # 4) 使い勝手向上（任意）
        view.setSortingEnabled(True)                     # ヘッダクリックでソート
        view.setSelectionBehavior(QTableView.SelectRows) # 行単位選択
        view.resizeColumnsToContents()                   # 列幅自動調整

        self.setCentralWidget(view)

        # 行数・列数の設定
        model.setRowCount(8)
        model.setColumnCount(5)
        rows = model.rowCount()
        cols = model.columnCount()
        print(f'列数：{rows}')
        print(f'行数：{cols}')

        model.setHorizontalHeaderLabels(["名前", "年齢", "部署"])

        item = QStandardItem("Misa")
        item.setEditable(False)
        model.setItem(0, 0, item)
        text = model.item(0, 0).text()
        print(text)

        idx = model.index(0, 1)
        model.setData(idx, 42, role=Qt.DisplayRole)
        val = model.data(idx, Qt.DisplayRole)
        print(f'idx = {idx}')
        print(f'val = {val}')

        # model.insertRow(1)
        # model.removeColumn(2)
        # model.clear()

        view.setSortingEnabled(True)                  # UIでソート可能
        model.sort(2, Qt.AscendingOrder)              # コードで実行

        from PySide6.QtWidgets import QAbstractItemView as AIV
        view.setEditTriggers(AIV.NoEditTriggers)      # 編集不可
        # 例: AIV.DoubleClicked, AIV.SelectedClicked, AIV.AllEditTriggers など
        # サイズ調整
        view.resizeColumnsToContents()
        # ヘッダー
        # hh = view.horizontalHeader()
        # hh.setStretchLastSection(True)    # 最終列を余白に合わせる
        # view.verticalHeader().setVisible(False)  # 行番号非表示

        idx = model.index(0, 0)
        item = model.itemFromIndex(idx)
        idx2 = model.indexFromItem(item)
        print(idx)
        print(item)
        print(idx2)

        hits = model.findItems("Bob", Qt.MatchContains, 0)  # 0列目から検索
        for it in hits:
            print(it.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(500, 300)
    w.show()
    sys.exit(app.exec())
