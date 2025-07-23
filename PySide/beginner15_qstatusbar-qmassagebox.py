from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStatusBarとQMessageBox")

        # ステータスバー作成
        self.statusBar().showMessage("準備完了")
        # self.statusBar().showMessage("保存しました", 3000)
        # self.statusBar().clearMessage()
        msg = self.statusBar().currentMessage()
        print(msg)

        from PySide6.QtWidgets import QLabel
        label = QLabel("追加したラベル")
        self.statusBar().addPermanentWidget(label)

        # ボタン作成
        button = QPushButton("警告を表示")
        button.clicked.connect(self.show_warning)
        self.setCentralWidget(button)

        # メッセージボックス
        # QMessageBox.information(self, "完了", "保存が完了しました")
        # QMessageBox.warning(self, "警告", "入力内容に誤りがあります")
        # QMessageBox.critical(self, "致命的", "ファイルが破損しています")
        reply = QMessageBox.question(self, "確認", "上書きしますか？")
        if reply == QMessageBox.Yes:
            print("Yesが選ばれました")
        if reply == QMessageBox.No:
            print("Noが選ばれました")


    def show_warning(self):
        QMessageBox.warning(self, "警告", "これは警告メッセージです")
        self.statusBar().showMessage("警告しました", 3000)
    

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())