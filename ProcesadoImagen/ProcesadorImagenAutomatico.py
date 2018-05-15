from PrawnView.ProcesadoImagen.LeeImagen import LeeImagen
from PrawnView.ProcesadoImagen.EntradaZip import EntradaZip
from PrawnView.ProcesadoImagen.TratamientoDeImagen import TratamientoDeImagen
from PrawnView.ProcesadoImagen.TratamientoSkeleton import TratamientoSkeleton

class ProcesadorImagenAutomatico():

  def __init__(self):
    self.pr_LeeImagen=LeeImagen()
    self.pr_TratamientoDeImagen=TratamientoDeImagen()
    self.pr_TratamientoSkeleton=TratamientoSkeleton()


  @classmethod
  def ProcesadorAutomatico(self,path):

    self.pr_LeeImagen=LeeImagen()
    self.pr_TratamientoDeImagen=TratamientoDeImagen()
    self.pr_TratamientoSkeleton=TratamientoSkeleton()

    
    img=self.pr_LeeImagen.leer_imagen(path)
    gray=self.pr_TratamientoDeImagen.escala_grises(img)
    binary=self.pr_TratamientoDeImagen.binarizar(gray)
    sk=self.pr_TratamientoDeImagen.skeleton(binary)
    ojo=self.pr_TratamientoSkeleton.detectar_ojo(img)
    centro_langostino,area_langostino=self.pr_TratamientoSkeleton.detectar_region(binary)
    centro_regiones,area_total_melanosis=self.pr_TratamientoSkeleton.detectar_region(ojo)
    
    
    self.pr_LeeImagen.muestra_imagenes(img)
    self.pr_LeeImagen.muestra_imagenes(gray)
    self.pr_LeeImagen.muestra_imagenes(binary)
    self.pr_LeeImagen.muestra_imagenes(sk)
    


 
