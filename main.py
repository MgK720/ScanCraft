import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.pushButton.clicked.connect(self.on_button_click)

    # def on_button_click(self):
    #     print("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
