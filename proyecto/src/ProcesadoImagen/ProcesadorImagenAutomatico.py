from PrawnView.proyecto.src.ProcesadoImagen.LeeImagen import LeeImagen
from PrawnView.proyecto.src.ProcesadoImagen.EntradaZip import EntradaZip
from PrawnView.proyecto.src.ProcesadoImagen.TratamientoDeImagen import TratamientoDeImagen
from PrawnView.proyecto.src.ProcesadoImagen.TratamientoRegiones import TratamientoRegiones

class ProcesadorImagenAutomatico():

  def __init__(self):
    self.pr_LeeImagen=LeeImagen()
    self.pr_TratamientoDeImagen=TratamientoDeImagen()
    self.pr_TratamientoRegiones=TratamientoRegiones()
  
  @classmethod
  def ratio(self,areag,aream):
    ratio=areag/aream
    return ratio


  @classmethod
  def ProcesadorAutomatico(self,path,binary):

    self.pr_LeeImagen=LeeImagen()
    self.pr_TratamientoDeImagen=TratamientoDeImagen()
    self.pr_TratamientoRegiones=TratamientoRegiones()

    
    img=self.pr_LeeImagen.leer_imagen(path)
    #gray=self.pr_TratamientoDeImagen.escala_grises(img)
    #binary=self.pr_TratamientoDeImagen.binarizar(gray)
    invbin=self.pr_TratamientoDeImagen.invertirbinarizar1(binary)
    sk=self.pr_TratamientoDeImagen.skeleton(binary)
    ojo=self.pr_TratamientoRegiones.detectar_ojo(img)
    centro_langostino,area_langostino=self.pr_TratamientoRegiones.detectar_region(img,invbin)
    centro_regiones,area_total_melanosis=self.pr_TratamientoRegiones.detectar_region(img,ojo)

    
    self.pr_LeeImagen.muestra_imagenes(img)
    self.pr_LeeImagen.muestra_imagenes(gray)
    self.pr_LeeImagen.muestra_imagenes(binary)
    self.pr_LeeImagen.muestra_imagenes(sk)
    
    return area_langostino,area_total_melanosis
    
