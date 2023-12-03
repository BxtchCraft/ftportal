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
# src/app/components/TitleBar/TitleBar.py
# Author: Morrigan Zierk

import os
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel

from app.components.IconButton.IconButton import IconButton

class TitleBar(QWidget):
    def __init__(self, parent=None):
        super(TitleBar, self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setObjectName("titleBar")
        self.setStyleSheet("#titleBar { background-color: #101323; }")

        stylesheet_path = os.path.join(os.path.dirname(__file__), 'style.qss')
        with open(stylesheet_path, "r") as file:
            self.setStyleSheet(file.read())

        base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        # FTPortal Window Icon
        ftportal_icon_path = os.path.join(base_path, 'resources', 'icons', 'ftportal_icon.svg')
        self.iconLabel = QLabel(self)
        self.iconLabel.setPixmap(QPixmap(ftportal_icon_path))
        self.iconLabel.setObjectName("logoIcon")
        
        # Window Title
        self.titleLabel = QLabel('FTPortal', self)
        
        # Icon Buttons
        minimize_icon_path = os.path.join(base_path, 'resources', 'icons', 'minimize.svg')
        minimize_hover_icon_path = os.path.join(base_path, 'resources', 'icons', 'minimize_hover.svg')
        self.minimizeButton = IconButton(minimize_icon_path, minimize_hover_icon_path, self)

        maximize_icon_path = os.path.join(base_path, 'resources', 'icons', 'maximize.svg')
        maximize_hover_icon_path = os.path.join(base_path, 'resources', 'icons', 'maximize_hover.svg')
        self.maximizeButton = IconButton(maximize_icon_path, maximize_hover_icon_path, self)

        close_icon_path = os.path.join(base_path, 'resources', 'icons', 'close.svg')
        close_hover_icon_path = os.path.join(base_path, 'resources', 'icons', 'close_hover.svg')
        self.closeButton = IconButton(close_icon_path, close_hover_icon_path, self)

        buttonSize = 36
        self.minimizeButton.setFixedSize(buttonSize, buttonSize)
        self.maximizeButton.setFixedSize(buttonSize, buttonSize)
        self.closeButton.setFixedSize(buttonSize, buttonSize)

        self.minimizeButton.setIconSize(QSize(12, 1))
        self.maximizeButton.setIconSize(QSize(12, 12))
        self.closeButton.setIconSize(QSize(12, 12))
        self.closeButton.setObjectName("closeButton")

        # Add Widgets to TitleBar Layout
        layout.addWidget(self.iconLabel)
        layout.addWidget(self.titleLabel, 1)
        layout.addWidget(self.minimizeButton)
        layout.addWidget(self.maximizeButton)
        layout.addWidget(self.closeButton)

        # Connect Signals
        self.minimizeButton.clicked.connect(self.minimizeWindow)
        self.maximizeButton.clicked.connect(self.maximizeWindow)
        self.closeButton.clicked.connect(self.closeWindow)
    
    def minimizeWindow(self):
        self.window().showMinimized()
    
    def maximizeWindow(self):
        if self.window().isMaximized():
            self.window().showNormal()
        else:
            self.window().showMaximized()
    
    def closeWindow(self):
        self.window().close()