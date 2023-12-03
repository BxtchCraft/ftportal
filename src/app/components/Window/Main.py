#                       ██                                                        
#                      ███                          ██            ██              
#                      ███     ███              ██████        ██████              
#    ███    ██ ████     █   ████████    ██████   ███████████   █████    ███     ██
# ██████  ████  ████  █████  █████    ██████████ ██████ █████  █████ ██████ ██████
#  █████   ████   ██  █████  █████   █████ ████  █████  █████  █████  █████  █████
#  ██████ █████   ██  █████  █████   █████       █████  █████  █████  █████  █████
#   █████ ██████████  █████  █████    █████     ██████  █████  █████  █████  █████
#   ███████ ███████   █████   ███████  █████████ █████  █████  █████  ████████████
#     █████   █████   ██████   █████     ████    ██████ ██████ █████    ███  █████
#                                                                      █████ █████
#                                                                      ████  ████ 
#                                                                      ████████                              
# src/app/components/Window/Window.py
# Author: Morrigan Zierk

import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from app.components.TitleBar.TitleBar import TitleBar

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.titleBar = TitleBar(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMenuWidget(self.titleBar)

        stylesheet_path = os.path.join(os.path.dirname(__file__), 'style.qss')
        with open(stylesheet_path, "r") as file:
            self.setStyleSheet(file.read())

        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName('centralContainer')
        self.setCentralWidget(self.centralWidget)
        self.centralLayout = QVBoxLayout(self.centralWidget)
        self.centralLayout.setContentsMargins(0, 0, 0, 0)
        # Add main content widgets to self.centralLayout when finished

        self.setWindowTitle('FTPortal')
        self.setGeometry(300, 300, 800, 600)

        
