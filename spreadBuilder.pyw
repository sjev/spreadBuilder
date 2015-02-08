# -*- coding: utf-8 -*-
"""
Spread builder. A gui tool used to identify and follow trading opportunities.


Copyright: Jev Kuznetsov
License: BSD

Project started on 08.02.2015

"""
import sys
from PyQt4 import QtGui

import widgets 

__version__ = "0.0.1"

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        #---flags
        self.dirty = False # indicate unsaved changes
        
        #----actions
        act_exit = QtGui.QAction( '&Exit', self)        
        act_exit.setStatusTip('Exit application')
        act_exit.triggered.connect(QtGui.qApp.quit)
        
        act_open = QtGui.QAction( '&Open', self)        
        act_open.setStatusTip('Load spreads')
        act_open.triggered.connect(self.test_fcn)
        
        act_useSymbol = QtGui.QAction( 'use', self)          
        act_useSymbol.triggered.connect(self.useSymbol)        
        
        act_test = QtGui.QAction( 'test', self)          
        act_test.triggered.connect(self.test_fcn)
        
        #---- menu
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(act_open)        
        fileMenu.addAction(act_exit)
        
        
        #---- toolbar
        toolbar = self.addToolBar('tools')
        toolbar.addAction(act_open)
        
        
        #---- statusbar
        self.statusBar().showMessage('Ready')
        
        # symbols dock
        self.dock_symbols = widgets.Dock('symbols',  self, widgets.SymbolsList) 
        lst = self.dock_symbols.widget()
        lst.setSymbols(['SPY','VXX','AAPL'])      
        lst.addAction(act_useSymbol)
        
        #-----prepare window
        self.setGeometry(100, 100, 600, 300) # init position and size
        self.setWindowTitle('SpreadBuilder v.' + __version__)    
        

    def useSymbol(self):
        """ adds symbol to a spread """
        lst = self.dock_symbols.widget()
        txt = lst.currentItem().text()
        self.statusBar().showMessage(txt + ' added')
        

    def test_fcn(self):
        """ dummy test function """
        self.statusBar().showMessage('test')


def main():
    print 'starting'
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

def test():
    print 'Done.'    

if __name__ == '__main__':
    main()
    #test()