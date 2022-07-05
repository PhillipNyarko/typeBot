import sys
import time
import pyautogui
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton


class TypeBot(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("AutoType")
        self.resize(300, 270)

        self.textEdit = QTextEdit()
        self.btnPress1 = QPushButton("Type")

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        self.setLayout(layout)

        self.btnPress1.clicked.connect(self.on_click)

    def on_click(self):
        textbox_value = self.textEdit.toPlainText()
        time.sleep(5)
        for line in textbox_value:
            pyautogui.typewrite(line)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TypeBot()
    win.show()
    sys.exit(app.exec_())


