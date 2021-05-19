import numpy as np
import matplotlib.pyplot as plt

"""NOIR & BLANC"""
#rentrer une image (array numpy de shape (a,b,3)) et le seuil renvoie l'image en noir et blanc (tableau numpy de 0 et 1)

def seuil(RGB) :
    (a,b)=RGB.shape
    y = np.array([445, 215, 230, 315, 195, 340, 235, 238, 320])
    xmoy = np.array([468.2150857834182, 218.68631746301443, 613.0925636574074, 338.8881871787812, 252.6242109375, 256.8581085205078, 245.15892028808594, 248.8688472811805, 262.58045959472656])
    xect = np.array([72.96140150457528, 120.97563893217499, 303.3137143423072, 146.29316950270834, 125.46026428871016, 63.721004285822346, 63.63264558435171, 123.20629224004448, 62.643284454830216])
    xdef = np.array([492636, 329588, 518400, 697344, 640000, 65536, 65536, 79152, 65536])
    xet = np.array([765, 707, 765, 764, 706, 598, 401, 716, 631])
    x1q = np.array([471, 150, 765, 180, 159, 228, 189, 141, 213])
    x3q = np.array([472, 195, 765, 448, 348, 255, 297, 342, 303])
    x1d = np.array([447, 133, 0, 139, 156, 212, 183, 130, 195])
    x9d = np.array([529, 446,  765, 516, 445, 300, 339, 436, 342])
    Pmoy = np.array(np.polyfit(xmoy, y, 4))
    Pect = np.array(np.polyfit(xect, y, 4))
    Pdef = np.array(np.polyfit(xdef, y, 4))
    Pet = np.array(np.polyfit(xet, y, 4))
    P1q = np.array(np.polyfit(x1q, y, 4))
    P3q = np.array(np.polyfit(x3q, y, 4))
    P1d = np.array(np.polyfit(x1d, y, 4))
    P9d = np.array(np.polyfit(x9d, y, 4))
    R1 = np.power(  np.abs((np.polyval(Pmoy,RGB.mean()) * np.polyval(Pect,np.sqrt(RGB.var())) * np.polyval(Pdef, a*b) * np.polyval(Pet,RGB.max()-RGB.min()) * np.polyval(P1q, np.percentile(RGB, 25)) * np.polyval(P3q, np.percentile(RGB, 75)) * np.polyval(P1d, np.percentile(RGB, 10)) * np.polyval(P9d, np.percentile(RGB, 90)) )), 1/8)
    if R1 > 770 :
        R1=445
    return R1


def NB (adresse,s = -1,show = False, noir = 'clair'):
    image = np.array(plt.imread(adresse), dtype=int)
    RGB = image[:,:,0]+image[:,:,1]+image[:,:,2]
    if s == -1 :
        s = seuil(RGB)
    if show : print(s)
    if noir == 'clair' : return np.array(RGB>s,dtype=int)
    else : return np.array(RGB<s,dtype=int)

