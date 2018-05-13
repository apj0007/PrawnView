from PrawnView.ProcesadoImagen.LeerMostrar import LeerMostrar
#from PrawnView.ProcesadoImagen.ProcesarZip import ProcesarZip
from PrawnView.ProcesadoImagen.TratamientoDeImagen import TratamientoDeImagen

class ProcesadorImagenAutomatico():

  def __init__(self):
    self.pr_leerMostrar=LeerMostrar()

  def ProcesadoImagen(self,img):
    self.pr_leerMostrar=LeerMostrar()
    
    self.pr_leerMostrar.leer_mostrar_imagen(img)
