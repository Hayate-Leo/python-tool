from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QMouseEvent, QKeyEvent
from PySide6.QtCore import Qt

class MyWidget(QWidget):
    def mousePressEvent(self, event: QMouseEvent):
        print(f"マウスクリック：{event.pos()}")

    def keyPressEvent(self, event: QKeyEvent):
        print(f"キー入力：{event.key()}")

    def mousePressEvent(self, event):
        print("マウスが押されました")
        print(f"位置: {event.pos()}")
        # マウスが押されました
        # 位置: PySide6.QtCore.QPoint(385, 210)
    
    def mouseMoveEvent(self, event):
        print(f"マウス移動: {event.position()}")
        # マウス移動: PySide6.QtCore.QPointF(204.800000, 201.600000)
        # マウス移動: PySide6.QtCore.QPointF(204.800000, 202.400000)
        # マウス移動: PySide6.QtCore.QPointF(204.800000, 204.000000)
        # マウス移動: PySide6.QtCore.QPointF(204.800000, 204.800000)
        # マウス移動: PySide6.QtCore.QPointF(204.000000, 206.400000)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A:
            print("Aが押されました")
        # Aが押されました
    
    def keyReleaseEvent(self, event):
        print(f"キー離し: {event.key()}")
        # キー離し: 65

    def enterEvent(self, event):
        print("マウスがウィジェットに入りました")
    
    def leaveEvent(self, event):
        print("マウスがウィジェットから出ました")
    
    def event(self, event):
        print(f"イベントタイプ: {event.type()}")
        return super().event(event)
        # マウスがウィジェットに入りました
        #イベントタイプ: 173
        # イベントタイプ: 11
        # マウスがウィジェットから出ました
    
app = QApplication([])
window = MyWidget()
window.show()
app.exec()