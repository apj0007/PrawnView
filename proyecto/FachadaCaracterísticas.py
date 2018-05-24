# -*- coding: utf-8 -*-
"""FachadaCaracterísticas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UmS7W-fvGkWMP3hreWeE39CwpDBv_xMt
"""

from PrawnView.proyecto.src.ProcesadoImagen.ProcesadorImagenAutomatico import ProcesadorImagenAutomatico

class FachadaCaracterísticas():
    """
    Clase fachada para el mediador que se encargara de la entrada salida por ficheros.
    @var mediador: Instancia del mediador de pestañas que crea dicha fachada.
    @var escribecsv: Instancia de la clase que pasa a csv los datos o los lee de dicho fichero.
    @var dic: Diccionario de datos donde estalocalizado los string del codigo.
    @var configuraciontoxml: Instancia de la clase que lee y escribe los xml.
    @var estad: Instancia de la clase que se encarga de lasestadisticas.   
    """

    def __init__(self,mediador,idioma):
      """
      Constructor de la clase FachadaEntradaSalida que inicializa y prepara todos
      los objetos que tendremos que usar mas adelante en la clase.
      """
      self.pr_ProcesadorImagenAutomatico=ProcesadorImagenAutomatico()
    
    @classmethod
    def ratio(self,path,binary):
      self.pr_ProcesadorImagenAutomatico=ProcesadorImagenAutomatico()
      areag,aream=ProcesadorImagenAutomatico.ProcesadorAutomatico(path,binary)
      ratio=aream/areag
      return areag,aream,ratio
