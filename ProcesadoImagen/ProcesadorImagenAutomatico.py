from ProcesadoImagen.LeeImagen import LeeImagen

class ProcesadorImagenAutomatico():

  def __init__(self):
    self.pr_leer_imagen=leer_imagen()
    self.pr_leer_imagen=muestra_imagenes()

  @classmethod
  def ProcesadorAutomatico(self,img):

    self.pr_leer_imagen=leer_imagen()
    self.pr_leer_imagen=muestra_imagenes()
    
    pr_leer_imagen.leer_imagen(img)

 
