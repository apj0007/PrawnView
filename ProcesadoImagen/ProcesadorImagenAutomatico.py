from ProcesadoImagen.LeeImagen import LeeImagen

class ProcesadorImagenAutomatico():

  def __init__(self):
    self.pr_LeeImagen=LeeImagen()


  @classmethod
  def ProcesadorAutomatico(self,img):

    self.pr_LeeImagen=LeeImagen()

    
    self.pr_LeeImagen.leer_imagen(img)
    self.pr_LeeImagen.muestra_imagenes(img,img)

 
