from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QDialog
)
from PyQt5.uic import loadUi
import sqlite3

class Admin (QDialog):
    def __init__(self):
        super(Admin, self).__init__()