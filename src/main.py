import sys
from PyQt5.QtWidgets import QApplication
from app.components.Window.Main import MainWindow

# def loadStyleSheet(filename):
#     with open(filename, "r") as file:
#         return file.read()

def main():
    app = QApplication(sys.argv)
    # styleSheet = loadStyleSheet("styles/style.qss")
    # app.setStyleSheet(styleSheet)

    mainWindow = MainWindow()
    mainWindow.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()