import numpy as np
import matplotlib.pyplot as plt

from NB import *
from resize import *
from contours import *


"""FONCTION FINALE"""
def traitement_image(adresse, show = False , showall = False, ctrs = True , rsz = True , seuil = -1, nb = True, noir = 'clair'):
    """
    adresse : adresse de l'image a importer
    show : montrer l'image une fois traitee (def=False)
    showall : afficher les debugs des sous fonctions (def=False)
    nb : transformer l'image en noir&blanc (def=True)
    seuil : seuil de la transformation en noir&blanc (def=determination auto)
    ctrs : contourer l'image / seulement si nb (def=True)
    rsz : redimensionner l'image, supression des bandes de blanc /seulement si nb (def=True)
    """

    title = "Image"
    if nb :
        title += " en noir & blanc"
        image_tr = NB(adresse, seuil,show = showall,noir = noir)
        if ctrs :
            title += ", contouree"
            image_tr =  contour_max(image_tr , show = showall)
        if rsz :
            title += ", redimensionnee"
            image_tr = resize(image_tr , show = showall)
    else : image_tr = np.array(plt.imread(adresse), dtype=int)

    if show :
        plt.imshow(image_tr)
        plt.title(title)
        plt.show()

    return image_tr