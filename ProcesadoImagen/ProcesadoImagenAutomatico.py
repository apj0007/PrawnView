from PrawnView.ProcesadoImagen.LeerMostrar import LeerMostrar,muestra_imagenes
from PrawnView.ProcesadoImagen.procesarZip import procesarZip

class ProcesadoImagenAutomatico():

  def __init__(self):
    self.pr_leerMostrar=LeerMostrar()

  def ProcesadoImagenAutomatico(self,img):
    self.pr_leerMostrar=LeerMostrar()
    
    v=self.pr_leerMostrar.leer_mostrar_imagen(img)
