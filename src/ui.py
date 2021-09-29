from PySide2.QtWidgets import QApplication, QPushButton

app = QApplication([])

if __name__ == "__main__":
    button = QPushButton("Click me")
    button.show()
    app.exec_()