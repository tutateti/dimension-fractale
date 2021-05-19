import numpy as np

"""PARCOURS CONTOURS"""
 # attention nécessite les coordonnées du pixel en haut à gauche du contour sinon ne fait rien de bien
 # penser avec la grille       ou dans case depart (passage de prenier deplacement au nouveau)
 # (-1,-1),(-1, 0),(-1, 1)    6     7     0           0     1     2
 # ( 0,-1), posit ,( 0, 1)    5  pt seul  1     ->    7  pt seul  3
 # ( 1,-1),( 1, 0),( 1, 1)    4     3     2           6     5     4

#choisit l'indice de la case ou commence tourne dans une liste
def casedepart(qr):
   q,r=qr
   return([[6,7,0],[5,'pt seul',1],[4,3,2]][q+1][r+1])

def tourne (contours,i,j,a):#sens horaire
    l=[(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]#positions de départ selon le denier déplacement
    for k in range (8):
        if contours[i+l[(k+a)%8][0],j+l[(k+a)%8][1]]:
            q,r=l[(k+a)%8]
            i,j=i+q,j+r
            return((i,j,q,r))
    return('pt seul')

def parcours_contours(contours,i,j,compte_pixel=False):# array 0,1 et coordonées du 1 en haut à gauche du contour
    i,j=i+1,j+1#+1 pour les contours plus loin
    k,l=i,j#position initiale
    a,b=contours.shape
    c=np.zeros((a+2,b+2),dtype=int)
    c[1:a+1,1:b+1]+=contours
    contours= c#création d'un contour blanc pour eviter certains bugs
    cs=np.zeros((a,b),dtype =int)#valeur retour
    q,r=0,1#mémoire du dernier déplacement
    t=tourne(contours,i,j,casedepart((q,r)))
    if t =='pt seul' :#cas du pt seul et modif de i,j pour le while
       cs[i-1,j-1]=1
       if compte_pixel :
          return(cs,1)
       return (cs)
    i,j,q,r=t
    cs[i-1,j-1]=1
    n=1#compteur de pixel revoyé si compte-pixel=True
    while l!=j or k!=i :
           i,j,q,r=tourne(contours,i,j,casedepart((q,r)))
           cs[i-1,j-1]=1
           n+=1
    if compte_pixel :
       return(cs,n)
    return (cs)