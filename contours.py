import numpy as np
import matplotlib.pyplot as plt

from parcours_contours import *


"""CONTOURS"""
#necessite un tableau numpy de 1 et 0 de dimension 2

#supprime les pixels noirs adjacents a quatre pixels noirs
def supprime_centre(image):
    a,b = image.shape
    pixel_del = image[0:a-2,1:b-1]+image[2:a,1:b-1]+image[1:a-1,0:b-2]+image[1:a-1,2:b]+image[1:a-1,1:b-1]
    pixel_del = np.array(pixel_del==5,dtype=int)
    image[1:a-1,1:b-1]-=pixel_del
    return image

#selectionne le plus grand contours de l'image (serie continue de un pixel de large)
#affiche l'image avant et le contours apres si show = True
def contour_max(image,show = False):
    #affichage image
    if show :
        plt.imshow(image)
        plt.title("l'image est :")
        plt.show()
    image=supprime_centre(image)
    a,b = image.shape
    maximum=-1
    for i in range (a):
        for j in range (b):
            if image [i,j]:
                contour = parcours_contours(image,i,j)
                image-=contour
                n=np.sum(contour)
                if n>maximum:
                    contourmax=contour
                    maximum=n
    if maximum==-1:
        contourmax=np.zeros((a,b))
    if show :
        plt.imshow(contourmax)
        plt.title("le contours est : (" + str(maximum) + " pixels)")
        plt.show()

    return contourmax