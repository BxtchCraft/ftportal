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
# src/app/components/IconButton/IconButton.py
# Author: Morrigan Zierk

import os
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon

class IconButton(QPushButton):
    def __init__(self, iconPath, hoverIconPath, parent=None):
        super().__init__(parent)

        base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        icon_abs_path = os.path.join(base_path, 'resources', 'icons', iconPath)
        hover_icon_abs_path = os.path.join(base_path, 'resources', 'icons', hoverIconPath)

        self.icon = QIcon(iconPath)
        self.hoverIcon = QIcon(hoverIconPath)
        self.setIcon(self.icon)
        self.setFixedSize(50, 50)
    
    def enterEvent(self, event):
        self.setIcon(self.hoverIcon)
        super().enterEvent(event)
    
    def leaveEvent(self, event):
        self.setIcon(self.icon)
        super().leaveEvent(event)