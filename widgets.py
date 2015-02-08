# -*- coding: utf-8 -*-
"""
widgets used by spread builder
Copyright 2015 Jev Kuznetsov
licence : BSD

"""


from PyQt4.QtCore import Qt
from PyQt4.QtGui import *

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from tradingWithPython_dev.lib import qtpandas

from scratchpad import fakeData

class Dock(QDockWidget):
    """ Simplified interface to QDockWidget.

    """
    def __init__(self, title, parent, childType,
                 area=Qt.LeftDockWidgetArea,
                 allowedAreas=Qt.AllDockWidgetAreas,
                 autoAddDock=True,
                 features=QDockWidget.AllDockWidgetFeatures):
        """ Constructor.
        
        Parameters
        ------------
        title : dock title
        parent : ancestor widget
        childType : callable to produce child widget
        area  : default dock area
        allowedAreas : dock widget allowed areas
        autoAddDock : if True, dock widget is added to parent
        features : dock widget features
        """
        QDockWidget.__init__(self, title, parent)
        self.setObjectName(title)
        #self.setAllowedAreas(allowedAreas)
        self.setFeatures(features)
        self.setWidget(childType(self))
        if autoAddDock:
            parent.addDockWidget(area, self)


class SymbolsList(QListWidget):
    """ 
    list of stock symbols  
    """
    def __init__(self, parent=None):
        QListWidget.__init__(self,parent)
        self.setMaximumWidth(80)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        
        
    def setSymbols(self,symbols):
        
        self.clear()
        for symbol in symbols:
            self.addItem(symbol)
    

class PlotWidget(QWidget):
    """
    matplotlib plot widget
    """
    def __init__(self,parent):
        super(PlotWidget,self).__init__(parent)
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        self.ax = self.figure.add_subplot(111) # create an axis

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)      
       
    def clear(self):
        self.ax.cla()
        
    def test(self):
        """ plot random data """
        
        df = fakeData()
        
        #self.ax.hold(False) # discard old data
        #self.ax.plot(df,'o-')
        self.clear()
        df.plot(ax=self.ax)        
        
        self.canvas.draw()

class SpreadWidget(QWidget):
    """ main widget for working with spreads """

    def __init__(self,parent):
        super(SpreadWidget,self).__init__(parent)
        
        self.table = qtpandas.DataFrameWidget(self)
        
        self.plot = PlotWidget(self)

        layout = QVBoxLayout()
        #layout.addWidget(self.table)
        layout.addWidget(self.plot)
        self.setLayout(layout)       
        
    def test(self):
        self.plot.test()
        
   
# --------------------------- test code -------------------------------

class MainWindow(QDialog):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        widget = SpreadWidget(self)
        button = QPushButton('Test')
        button.clicked.connect(widget.test)
        
        layout = QVBoxLayout()
        layout.addWidget(widget)
        layout.addWidget(button)
        
        self.setLayout(layout)
        
        
        
if __name__ == '__main__':
    print 'starting'
    
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())    
    
    print 'done.'