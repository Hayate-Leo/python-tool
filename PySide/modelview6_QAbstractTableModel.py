from PySide6.QtCore import Qt, QAbstractTableModel, QTimer, QModelIndex
from PySide6.QtWidgets import QApplication, QTableView
import sys, random

class CustomTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        super().__init__()
        self._data = data or [[0, 0, 0] for _ in range(5)]

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data[0])

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
    
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return f"列 {section}"
            if orientation == Qt.Vertical:
                return f"行 {section}"
    
    def insertRows(self, position, rows=1, parent=None):
        # 1. 追加開始をビューに通知
        self.beginInsertRows(parent or QModelIndex(), position, position + rows - 1)
        # 2. 内部データに行を挿入
        for _ in range(rows):
            self._data.insert(position, [0] * self.columnCount())
        # 3. 追加終了をビューに通知
        self.endInsertRows()
        return True
    
    def removeRows(self, position, rows=1, parent=None):
        self.beginRemoveRows(parent or QModelIndex(), position, position + rows - 1)
        for _ in range(rows):
            del self._data[position]
        self.endRemoveRows()
        return True


# 実行用
app = QApplication(sys.argv)
view = QTableView()
model = CustomTableModel()
view.setModel(model)


# 定期的に値を更新
def update_data():
    row, col = random.randint(0, 4), random.randint(0, 2)
    model.setData(model.index(row, col), random.randint(1, 100))
    print("データ:", model.data(model.index(row, col)))
    # 行を追加
    row_position = model.rowCount()
    model.insertRows(row_position, 1)
    # 行を削除
    model.removeRows(1)

# デバッグ用途で明示的に呼ぶ
print("行数:", model.rowCount())
print("列数:", model.columnCount())

timer = QTimer()
timer.timeout.connect(update_data)
timer.start(1000)

view.show()
sys.exit(app.exec())