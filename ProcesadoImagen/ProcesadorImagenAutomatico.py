from PrawnView.ProcesadoImagen.LeeImagen import LeeImagen
from PrawnView.ProcesadoImagen.EntradaZip import EntradaZip

class ProcesadorImagenAutomatico():

  def __init__(self):
    self.pr_LeeImagen=LeeImagen()


  @classmethod
  def ProcesadorAutomatico(self,path):

    self.pr_LeeImagen=LeeImagen()

    
    img=self.pr_LeeImagen.leer_imagen(path)
    self.pr_LeeImagen.muestra_imagenes([img,img])

 
