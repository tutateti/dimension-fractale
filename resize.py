import numpy as np

"""REDIMENSIONNEMENT (supression des bords blancs)"""
def resize(img,show = False): #img must be as 0 and 1 nd.array
    (p, q) = img.shape
    if show : print((p, q))
    for i in np.arange(0, p, 1):
        if np.sum(img[i,:]) :
            l=i
            break
    for i in np.arange(p-1, -1, -1):
        if np.sum(img[i,:]) :
            r=i
            break
    for j in np.arange(0, q, 1):
        if np.sum(img[:,j]) :
            t=j
            break
    for j in np.arange(q-1, -1, -1):
        if np.sum(img[:,j]) :
            b=j
            break
    if show : print(l, r, t, b)
    return img[l:(r+1),t:(b+1)]