from PrawnView.ProcesadoImagen.LeeImagen import LeeImagen
from PrawnView.ProcesadoImagen.EntradaZip import EntradaZip
from PrawnView.ProcesadoImagen.TratamientoDeImagen import TratamientoDeImagen

class ProcesadorImagenAutomatico():

  def __init__(self):
    self.pr_LeeImagen=LeeImagen()
    self.pr_TratamientoDeImagen=TratamientoDeImagen()


  @classmethod
  def ProcesadorAutomatico(self,path):

    self.pr_LeeImagen=LeeImagen()
    self.pr_TratamientoDeImagen=TratamientoDeImagen()

    
    img=self.pr_LeeImagen.leer_imagen(path)
    gray=self.pr_TratamientoDeImagen.escala_grises(img)
    binary=self.pr_TratamientoDeImagen.binarizar(gray)
    
    self.pr_LeeImagen.muestra_imagenes([img,gray],binary)


 
