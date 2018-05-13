from PrawnView.ProcesadoImagen.LeerMostrar import LeerMostrar
'''
class ProcesadorImagenAutomatico():

  def __init__(self):
    self.pr_leerMostrar=LeerMostrar()
  @classmethod
  def ProcesadorAutomatico(self,img):
    self.pr_leerMostrar=LeerMostrar()
    self.pr_leerMostrar.leer_mostrar_imagen(img)
'''
    
class ProcesadorImagenAutomatico():

  def __init__(self):
    self.pr_leerMostrar=LeerMostrar()
    

  def y(self,img):
    self.ProcesadoImagen(img)


  def ProcesadoImagen(self,img):
    self.pr_leerMostrar=LeerMostrar()
    self.pr_leerMostrar.leer_mostrar_imagen(img)
