from PrawnView.ProcesadoImagen.LeerMostrar import LeerMostrar

class ProcesadorImagenAutomatico():

  def __init__(self):
    self.pr_leerMostrar=LeerMostrar()
  @classmethod
  def ProcesadorAutomatico(self,img):
    self.pr_leerMostrar=LeerMostrar()
    self.pr_leerMostrar.leer_mostrar_imagen(img)
