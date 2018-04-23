import matplotlib.pyplot as plt 
import math
from skimage.io import imread
from skimage import io

def leer_mostrar_imagen(file,debug=False):

  img =imread(file)
  plt.subplot(211)
  io.imshow(img)
  return img

def muestra_imagenes(imagenes):
  num_images = len(imagenes)
  if num_images<2:
    print("Se debe pasar más de una imagen")
    return 0
  
  lado = math.ceil(num_images**0.5)
  tam_image = 7
  
  for i in range(len(imagenes)):
    plt.subplot(lado,lado,i+1)
    io.imshow(imagenes[i])
 
  io.show()
