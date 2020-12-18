from qgis.PyQt.QtWidgets import *
from .impact_table_dialog import Ui_dlgImpacts


class DlgTable(QDialog,Ui_dlgImpacts):
    def __init__(self):
        super(DlgTable, self).__init__()
        self.setupUi(self)
        
        #extend size of second column in table
        self.tblImpacts.setColumnWidth(1,300)