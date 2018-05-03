from PrawnView.ProcesadoImagen.LeerMostrar import LeerMostrar
from PrawnView.descargar_extraer_zip import extraer_zip,descargar_zip_url

class ProcesadoImagenAutomatico():

  def __init__(self):
    self.pr_leerMostrar=LeerMostrar()

  def ProcesadoImagenAutomatico(sef,img):
    self.pr_leerMostrar=LeerMostrar()
    
    v=self.pr_leerMostrar.leer_mostrar_imagen(img)
