from PrawnView.ProcesadoImagen.LeerMostrar import LeerMostrar

class ProcesadorImagenAutomatico():

  def __init__(self):
    self.pr_leerMostrar=LeerMostrar()
    print("init")
  @classmethod
  def ProcesadorAutomatico(img):
    print("1")
    #self.pr_leerMostrar=LeerMostrar()
    print("2")
    LeerMostrar.leer_mostrar_imagen(img)
    #self.pr_leerMostrar.leer_mostrar_imagen(img)

 
