import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTableView, QComboBox, QLabel
)
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont

# Matplotlib（Qt連携）
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar
)
from matplotlib.figure import Figure


class TableGraphApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableView × Matplotlib グラフ切り替え")
        self.resize(900, 650)
        self.setFont(QFont("Meiryo", 10))

        # レイアウト
        layout = QVBoxLayout(self)

        # モデルとビュー
        self.model = QStandardItemModel(5, 2)  # 5行2列
        self.model.setHorizontalHeaderLabels(["X", "Y"])
        self.view = QTableView()
        self.view.setModel(self.model)

        # Matplotlib
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        # ツールバー
        self.toolbar = NavigationToolbar(self.canvas, self)

        # グラフ種類の選択UI
        self.graph_selector_label = QLabel("グラフタイプ:")
        self.graph_selector = QComboBox()
        self.graph_selector.addItems(["折れ線グラフ", "棒グラフ"])
        self.graph_selector.currentIndexChanged.connect(self.update_plot)
        typ = self.graph_selector.currentText()
        print(typ)

        # レイアウトに追加
        layout.addWidget(self.view)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.graph_selector_label)
        layout.addWidget(self.graph_selector)
        layout.addWidget(self.canvas)

        # データ変更時にグラフ更新
        self.model.dataChanged.connect(self.update_plot)

        # 初期データをセット
        self.set_initial_data()
        self.update_plot()

    def set_initial_data(self):
        """初期データをモデルにセット"""
        data = [(1, 10), (2, 15), (3, 8), (4, 12), (5, 18)]
        for row, (x, y) in enumerate(data):
            self.model.setItem(row, 0, QStandardItem(str(x)))
            self.model.setItem(row, 1, QStandardItem(str(y)))

    def update_plot(self):
        """テーブルのデータを読み取り、選択されたグラフを描画"""
        x, y = [], []
        for row in range(self.model.rowCount()):
            item_x = self.model.item(row, 0)
            item_y = self.model.item(row, 1)
            if item_x and item_y:
                text = item_x.text()
                try:
                    x_val = float(item_x.text())
                    y_val = float(item_y.text())
                    x.append(x_val)
                    y.append(y_val)
                except ValueError:
                    continue  # 数値変換できないセルはスキップ

        # グラフをクリア
        self.ax.clear()

        # グラフタイプを選択
        graph_type = self.graph_selector.currentText()
        if x and y:
            if graph_type == "折れ線グラフ":
                self.ax.plot(x, y, marker="o", linestyle="-", color="blue", label="Line")
            elif graph_type == "棒グラフ":
                self.ax.bar(x, y, color="green", label="Bar")

            self.ax.set_xlabel("X")
            self.ax.set_ylabel("Y")
            self.ax.set_title(f"Dynamic {graph_type}", fontname='Meiryo')
            self.ax.legend()

        # 描画更新
        self.canvas.draw_idle()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableGraphApp()
    window.show()
    sys.exit(app.exec())
