#PANAGIOTIS NTOUNETAS AM:2781

import numpy as numpy
from numpy import *
import matplotlib.pyplot as matplot
from PIL import Image
import sys
#https://en.wikipedia.org/wiki/Affine_transformation Me vasi ta 'image transformations' se ayth th selida.



#Epeksergasia eikonas
#1o orisma einai to: python askisi1.py

#img = numpy.array(Image.open(sys.argv[1])) #Eisagw thn eikona san 2o orisma
#k = int(sys.argv[2]) #Eisagw to katwfli san to 3o orisma

img = numpy.array(Image.open('trikoupi6.png')) #Ayth kai thn epomenh entolh tis vazete se sxolio kai vgazete tis apo panw
k=100											#wste na treksei opos to zhtate sthn ekfwnisi se terminal. Sthn prokeimenh oi times htan apo 50-250 me vima 50.
												#Doulevei kai gia oles tis times. Apla sto 250...255 ginetai teleiws maayrh, pou einai ki logiko.

x = img.shape[0] #grammes
y = img.shape[1] #sthles

#Tsekarw an h eikona mou einai egxrwmi h oxi, an einai thn metatrepw se grayscale
editedImg = numpy.zeros([x,y])

img = double(img) #Gia na ginei h diaresh grammh 27, n vgainei error/warning

if(len(img.shape) == 3): #An h eikona einai RGB, h diastash tou pinaka shape einai 3
	for i in range(1,x):
		for j in range(1,y):
			editedImg[i][j] = (img[i][j][0] + img[i][j][1] + img[i][j][2])/3
else:
	#for i in range(1,x):					#Kai oi 2 tropoi eite anathetontas apeyhteias to img sto neo pinaka
		#for j in range(1,y):				#eite me perasma twn pixel 1 pros 1 
			#editedImg[i][j] =  img[i][j]	#to einai sxedon to idio. Einai kai ta 2 dokimsmena.
			
	editedImg = img
	
	
#Ftiaxnw thn eikona mou me to katwfli
kImg = numpy.zeros([x,y])

#print('TIMI KATWFLIOU =',k) #Gia na emfaanistei to katwfli sto Jupyter cell.

for i in range (0,x):				#edw ginetai h efarmogh tou katwfliou. Osa pixels vriskontai katw apo to katwfli mayrizoun.
	for j in range(0,y):			#Osa einai panw, ginontai aspra. To apotelsma edw einai idio eite evaza 1 eite 255.
		if(editedImg[i][j]< k):
			kImg[i][j] = 0
		else:
			kImg[i][j] = 1

matplot.imshow(kImg, cmap="gray")
matplot.show()
	


