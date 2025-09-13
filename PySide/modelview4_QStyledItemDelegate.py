from PySide6.QtWidgets import (
    QApplication, QTableView, QStyledItemDelegate, QStyleOptionProgressBar, QStyle,
    QComboBox
)
from PySide6.QtGui import QStandardItemModel, QStandardItem, QColor
from PySide6.QtCore import Qt, QSize
import sys

class ProgressDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        # 数値をパーセントとして描画する（整数保存想定）
        try:
            value = int(index.data(Qt.DisplayRole))
        except Exception:
            super().paint(painter, option, index)
            return

        opt = QStyleOptionProgressBar()
        opt.rect = option.rect.adjusted(6, 8, -6, -8)
        opt.minimum = 0
        opt.maximum = 100
        opt.progress = max(0, min(100, value))
        opt.text = f"{opt.progress}%"
        opt.textVisible = True
        QApplication.style().drawControl(QStyle.CE_ProgressBar, opt, painter)

    def sizeHint(self, option, index):
        s = super().sizeHint(option, index)
        return QSize(s.width(), s.height() + 8)


class StatusDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        text = index.data(Qt.DisplayRole)
        # 背景色を条件で変える
        if isinstance(text, str):
            if "エラー" in text or "Error" in text:
                painter.save()
                painter.fillRect(option.rect, QColor(255, 200, 200))
                painter.restore()
            elif "完了" in text or "Done" in text:
                painter.save()
                painter.fillRect(option.rect, QColor(200, 255, 200))
                painter.restore()
        # 標準表示（テキスト描画）
        super().paint(painter, option, index)

    def createEditor(self, parent, option, index):
        cb = QComboBox(parent)
        cb.addItems(["未着手", "処理中", "完了", "エラー"])
        # 値確定と閉じる通知
        cb.activated.connect(lambda _idx, ed=cb: self.commitData.emit(ed))
        cb.activated.connect(lambda _idx, ed=cb: self.closeEditor.emit(ed))
        return cb

    def setEditorData(self, editor, index):
        val = index.data(Qt.DisplayRole)
        i = editor.findText(val)
        if i >= 0:
            editor.setCurrentIndex(i)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText(), Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect.adjusted(2, 2, -2, -2))


def build_model():
    model = QStandardItemModel(5, 3)
    model.setHorizontalHeaderLabels(["Task", "Progress", "Status"])
    rows = [
        ("ダウンロード", 10, "処理中"),
        ("解析", 40, "処理中"),
        ("レポート作成", 70, "処理中"),
        ("バックアップ", 100, "完了"),
        ("外部接続", 20, "エラー"),
    ]
    for r, (task, prog, status) in enumerate(rows):
        model.setItem(r, 0, QStandardItem(task))
        # Progress を数値として保持（重要）
        model.setData(model.index(r, 1), prog, Qt.DisplayRole)
        model.setItem(r, 2, QStandardItem(status))
    return model

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = QTableView()
    model = build_model()
    view.setModel(model)
    view.setItemDelegateForColumn(1, ProgressDelegate(view))
    view.setItemDelegateForColumn(2, StatusDelegate(view))
    view.resize(640, 300)
    view.show()
    sys.exit(app.exec())
