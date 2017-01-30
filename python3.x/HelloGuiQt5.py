'''
.SYNOPSIS
    Hello Python.
.DESCRIPTION
    Hello python with PyQt5
.NOTES
    File Name      : Hello World.ps1
    Author         : gajendra d ambi
    Date           : 2016
    Prerequisite   : python 3.5.x
    Copyright      - None
.LINK
    Script posted over: https://github.com/MrAmbiG/
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle('Hello World')
    w.show()

    sys.exit(app.exec_())