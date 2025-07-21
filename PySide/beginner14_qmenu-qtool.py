from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QToolBar
from PySide6.QtGui import QAction
import sys

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMenuBarとQToolBar")

        # メニューバー作成
        menubar = self.menuBar()
        file_menu = QMenu("ファイル", self)
        menubar.addMenu(file_menu)
        file_menu2 = menubar.addMenu("編集")

        # アクション作成
        open_action = QAction("開く", self)
        file_menu.addAction(open_action)
        edit_action = QAction("編集", self)
        file_menu2.addAction(edit_action)
        file_menu.addSeparator()
        file_menu.setTitle("Open")
        # file_menu.clear()
        if file_menu.isEmpty():
            print("空のメニューです")
        else:
            print("アクションがあります")
        # file_menu.setEnabled(False)  # グレーアウトされて選択不可に
        open_action.setShortcutVisibleInContextMenu(True)

        # ツールバー作成
        toolbar = QToolBar("メインツールバー", self)
        self.addToolBar(toolbar)
        toolbar.addAction(open_action)
        toolbar.addAction(edit_action)
        toolbar.addSeparator()
        toolbar.addSeparator()
        # toolbar.setMovable(False)  # 固定化
        # toolbar.setFloatable(True)
        from PySide6.QtCore import Qt
        toolbar.setAllowedAreas(Qt.TopToolBarArea | Qt.LeftToolBarArea)
        view_action = toolbar.toggleViewAction()
        file_menu.addAction(view_action)

        # toolbar.setOrientation(Qt.Vertical)
        from PySide6.QtGui import QIcon
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        # アクション追加（アイコン + テキスト）
        open_action = QAction(QIcon.fromTheme("document-open"), "開く", self)
        save_action = QAction(QIcon.fromTheme("document-save"), "保存", self)

        toolbar.addAction(open_action)
        toolbar.addAction(save_action)

window = MainWindow()
window.show()
sys.exit(app.exec())