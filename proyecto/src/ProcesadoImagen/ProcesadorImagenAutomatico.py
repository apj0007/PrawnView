from PrawnView.ProcesadoImagen.LeeImagen import LeeImagen
from PrawnView.ProcesadoImagen.EntradaZip import EntradaZip
from PrawnView.ProcesadoImagen.TratamientoDeImagen import TratamientoDeImagen
from PrawnView.ProcesadoImagen.TratamientoRegiones import TratamientoRegiones

class ProcesadorImagenAutomatico():

  def __init__(self):
    self.pr_LeeImagen=LeeImagen()
    self.pr_TratamientoDeImagen=TratamientoDeImagen()
    self.pr_TratamientoRegiones=TratamientoRegiones()


  @classmethod
  def ProcesadorAutomatico(self,path):

    self.pr_LeeImagen=LeeImagen()
    self.pr_TratamientoDeImagen=TratamientoDeImagen()
    self.pr_TratamientoRegiones=TratamientoRegiones()

    
    img=self.pr_LeeImagen.leer_imagen(path)
    gray=self.pr_TratamientoDeImagen.escala_grises(img)
    binary=self.pr_TratamientoDeImagen.binarizar(gray)
    invbin=self.pr_TratamientoDeImagen.invertirbinarizar1(binary)
    sk=self.pr_TratamientoDeImagen.skeleton(binary)
    ojo=self.pr_TratamientoRegiones.detectar_ojo(img)
    centro_langostino,area_langostino=self.pr_TratamientoRegiones.detectar_region(img,invbin)
    centro_regiones,area_total_melanosis=self.pr_TratamientoRegiones.detectar_region(img,ojo)
    
    
    self.pr_LeeImagen.muestra_imagenes(img)
    self.pr_LeeImagen.muestra_imagenes(gray)
    self.pr_LeeImagen.muestra_imagenes(binary)
    self.pr_LeeImagen.muestra_imagenes(sk)
    
    print("\ncentro_langostino",centro_langostino,"\narea_langostino",area_langostino)
    print("\ncentro_regiones",centro_regiones,"\narea_total_melanosis",area_total_melanosis)
