import sys
from PyQt5.QtWidgets import QApplication
from views.main_window import MainWindow
from load_db import init_db
if __name__ == "__main__":
    app = QApplication(sys.argv)
    init_db()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())