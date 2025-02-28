import sys
# from PySide.QtWidgets import QApplication
from PyQt5.QtWidgets import QApplication

from MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("System")
    window.resize(800, 800)
    window.show()
    sys.exit(app.exec())
