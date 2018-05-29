# sudo apt install python-pyqt5
# https://pythonspot.com/category/pyqt5/

# La aplicacion podría ir por pestañas
# https://pythonspot.com/pyqt5-tabs/

# imagen
# https://pythonspot.com/category/pyqt5/page/3/


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QLineEdit, QMessageBox,QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot



class A:
    def metodo1(self):
        print("Metodo1")

class B:
    def metodo2(self):
        print("Metodo2")

class C:
    def metodo3(self):
        print("Metodo3")

class Fachada:
    def __init__(self):
        self.a = A()
        self.b = B()
        self.c = C()

    def segmenta(self):
        print('segm')
        self.a.metodo1()
        self.b.metodo2()
        self.c.metodo3()
    
    def melanosis(self):
        print("Melanosis")

    def skeleton(self):
        print("Skeleton")


class Mediator:
    def __init__(self,parent):
        self.fachada = Fachada()
        self.parent=parent
        
    
    def registra_boton_carga(self,boton_carga,label):
        self.boton_carga = boton_carga
        self.label=label
        self.boton_carga.triggered.connect(self.carga)
        


    def registra_boton_segmenta(self,boton_segmenta):
        self.boton_segmenta = boton_segmenta
        self.boton_segmenta.triggered.connect(self.fachada.segmenta)

    def registra_boton_melanosis(self,boton_melanosis):
        self.boton_melanosis = boton_melanosis
        self.boton_melanosis.triggered.connect(self.fachada.melanosis)

    def registra_boton_skeleton(self,boton_skeleton):
        self.boton_skeleton = boton_skeleton
        self.boton_skeleton.triggered.connect(self.fachada.skeleton)

    def registra_info_text(self,info_text):
        self.info_text = info_text

    def segmenta(self):
        print('Segmenta')
        self.fachada.segmenta()
        self.info_text.setText("Segmentado")

    def carga(self):
        print('Carga imagen')
        pixmap, _ = QFileDialog.getOpenFileName(self.parent,"QFileDialog.getOpenFileName()", "","All Files (*)",'/home')
        imagePath = pixmap[0]
        pixmap = QPixmap(pixmap)
        self.label.setPixmap(pixmap)     
        #self.resize(pixmap.width(),pixmap.height())

    

 
 

class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PrawnView'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.initUI()
        
        




 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label = QLabel(self)
        
	
        mainMenu = self.menuBar() 

        fileMenu = mainMenu.addMenu('Archivo')
        toolsMenu = mainMenu.addMenu('Procesado de imagen')
        helpMenu = mainMenu.addMenu('Ayuda')
 
        exitButton = QAction(QIcon('exit24.png'), 'Salir', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Salir de la aplicación')
        exitButton.triggered.connect(self.close)
        
	#QAction (String, paret)
        openButton = QAction('Abrir', self)
        openButton.setShortcut('Ctrl+O')
        openButton.setStatusTip('Abrir Imagen')


        segmentaButton = QAction('Segmentar', self)
        segmentaButton.setShortcut('Ctrl+S')
        segmentaButton.setStatusTip('Segmentar Imagen')

        ratioButton = QAction('Cantidad de melanosis', self)
        ratioButton.setShortcut('Ctrl+m')
        ratioButton.setStatusTip('Calcula el ratio de melanosis')

        
        skeletonButton = QAction('Skeleton', self)
        skeletonButton.setShortcut('Ctrl+k')
        skeletonButton.setStatusTip('Muestra Skeleton')

        

        fileMenu.addAction(exitButton)
        fileMenu.addAction(openButton)

        toolsMenu.addAction(segmentaButton)
        toolsMenu.addAction(ratioButton)
        toolsMenu.addAction(skeletonButton)



        
        # Create widget
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(0, 350)
        self.textbox.resize(280,40)

        self.mediator = Mediator(self)
        self.mediator.registra_boton_carga(openButton,self.label)
        self.mediator.registra_boton_segmenta(segmentaButton)
        self.mediator.registra_boton_melanosis(ratioButton)
        self.mediator.registra_boton_skeleton(skeletonButton)
        self.mediator.registra_info_text(self.textbox)

        
        
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
