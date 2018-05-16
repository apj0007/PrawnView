import matplotlib.pyplot as plt 
import math
from skimage.io import imread
from skimage import io
class LeeImagen():
    """
    Clase que contiene las clases para leer una imagen y mostrarla por pantalla     en grande o en pequeño.
    
    @author: Andrés Pérez Juárez
    @version: 1.3
    """
    
    @classmethod
    def leer_imagen(self,file):
        """
        Función que permite leer  una imagen cargada
        
        @param file: imagen que se desea leer
 
        @return: se deuelve la imagen ya leida en python
        """
        img =imread(file)
        return img

    @classmethod
    def muestra_imagenes(self,image):
        """
        Función que permite mostrar varias imágenes, deben ser mas de 2 y se pueden mostrar en tamaño grande o más pequeño

        @param imagenes: Lista con las imágenes que se desea mostrar
        @param grandes: Boolean, que por defecto se encuentra a False, si esta en True mostrará las imagenes en tamaño grande

        """

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.imshow(image)
        plt.show()

