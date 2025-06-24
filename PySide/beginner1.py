import PySide6
print(PySide6.__version__)

import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel('Hello PySide6!')
label.show()
sys.exit(app.exec())