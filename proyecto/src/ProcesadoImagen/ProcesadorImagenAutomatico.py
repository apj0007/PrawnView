from src.ProcesadoImagen.LeeImagen import LeeImagen
from src.ProcesadoImagen.EntradaZip import EntradaZip
from src.ProcesadoImagen.TratamientoDeImagen import TratamientoDeImagen
from src.ProcesadoImagen.TratamientoRegiones import TratamientoRegiones



class ProcesadorImagenAutomatico():
  """
  Clase que contendra los tratamientos referentes a la imagen, recibiendo el path y la imagen binarizada.
  En esta clase se llama a los métodos del modulo TratamientoDeImage().Tmabien llamará
  TratamientoRegiones() para sacar los datos referentes al area el langostino y de l area de su melanosis.
    
  @author: Andrés Pérez Juárez
  @version: 1.0
  """
  def __init__(self):
    self.pr_LeeImagen=LeeImagen()
    self.pr_TratamientoDeImagen=TratamientoDeImagen()
    self.pr_TratamientoRegiones=TratamientoRegiones()
  
  @classmethod
  def ratio(self,areag,aream):
    """
    Con este metodo recogemos las areas del langostino y el area de su melanosis para despues 
    calcular el ratio.
        
    @param  areag: área de la gamba
    @param  aream: área de la melanosis
    @return ratio: aream/areag.
    """
    ratio=areag/aream
    return ratio


  @classmethod
  def ProcesadorAutomatico(self,path,binary):

    '''
    Método que se encarga de llamar a los modulos de TratamientoDeImagen() hasta sacar el skeleton
    y llamada a TratamientoRegiones() para conseguir las áreas necesarias para el ratio.

    @param  path: ruta de acceso a la imagen que deseamos tratar
    @param  binary: imagen binaria
    @return  area_langostino,area_total_melanosi: Área total del langostino y área total de la melanosis
    '''

    self.pr_LeeImagen=LeeImagen()
    self.pr_TratamientoDeImagen=TratamientoDeImagen()
    self.pr_TratamientoRegiones=TratamientoRegiones()

    
    img=self.pr_LeeImagen.leer_imagen(path)
    invbin=self.pr_TratamientoDeImagen.invertirbinarizar1(binary)
    sk=self.pr_TratamientoDeImagen.skeleton(binary)
    ojo=self.pr_TratamientoRegiones.detectar_ojo(img)
    centro_langostino,area_langostino=self.pr_TratamientoRegiones.detectar_region(img,binary)
    centro_regiones,area_total_melanosis=self.pr_TratamientoRegiones.detectar_region(img,ojo)

    
    return area_langostino,area_total_melanosis
