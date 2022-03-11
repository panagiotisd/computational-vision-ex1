#PANAGIOTIS NTOUNETAS AM:2781

import numpy as numpy
from numpy import *
import matplotlib.pyplot as matplot
from PIL import Image
import sys
from datetime import datetime
startTime = datetime.now()
'''
Xrhsimopoihsa tous typous apo tis diafaneies DIP, eidika
tin "DIP 2017 10a Katatmisi" sel.12-21. Gia auto ola ta 
sxolia kanoun parapompi ekei.
'''

input = numpy.array(Image.open(sys.argv[1])) 			#Osa einai se sxolia edw einai gia na treksw Jupyter NB.
#input = numpy.array(Image.open('trikoupi6_low.png'))
output = sys.argv[2]
#output = 'out.png'
wsize = sys.argv[3]
#wsize = 7
wsize = int(wsize)

m = input.shape[0]	#grammes
n = input.shape[1]	#stiles

#To parakatw kommati metatropis RGB einai copy paste apo to 1o mou set, askisi 1.
#Tsekarw an h eikona mou einai egxrwmi h oxi, an einai thn metatrepw se grayscale
new = numpy.zeros([m,n])

input = double(input) #Gia na ginei h diaresh grammh 27, n vgainei error/warning

if(len(input.shape) == 3): #An h eikona einai RGB, h diastash tou pinaka shape einai 3
	for i in range(1,m):
		for j in range(1,n):
			new[i][j] = (input[i][j][0] + input[i][j][1] + input[i][j][2])/3
else:
	for i in range(1,m):
		for j in range(1,n):
			new[i][j] =  input[i][j]


B = numpy.zeros([m,n])

K = 100
print('Endiktiko katwfli pou efarmozetai: ', K)
print('Window size: ', wsize, 'X', wsize)

for a in range (1,m): #Diasxizw thn eikona pixel pros pixel
	for b in range (1,n):

		x_geitonwn_plus = a+(wsize//2) #gia kathe window size rythmizw tous geitones
		x_geitonwn_minus = a-(wsize//2)
		y_geitonwn_plus = b+(wsize//2)
		y_geitonwn_minus = b-(wsize//2)

		if(x_geitonwn_plus > m): #Elegxw to dosmeno window size na mhn
			x_geitonwn_plus = m  #vgainei ektos oriwn ths eikonas
		if(x_geitonwn_minus < 0):
			x_geitonwn_minus = 1
		if(y_geitonwn_plus > n):
			y_geitonwn_plus = n
		if(y_geitonwn_minus < 0):
			y_geitonwn_minus = 1
	
		counter = [0] * 256
		pk1 =0
		pk2 =0
		mk1 =0
		mk2 =0
		p = [0]*255
		p1 = [0]*255
		p2 = [0]*255
		m1 = [0]*255
		m2 = [0]*255
		for i in range (x_geitonwn_minus, x_geitonwn_plus): #loop geitonwn
			for j in range (y_geitonwn_minus, y_geitonwn_plus):
				for k in range (0, 255):
					if(k == new[i][j]):	#an to xrwma sto keli einai metaksy 0..255
						counter[k] = counter[k] + 1	#kane ton counter tou sugkekrimenou xromatos + 1

				for i in range (0,K):
					p[i] = counter[i]/(wsize**2)	#kanonikopoihmeno istogramma, gia kathe 
					p1[i] = p[i]		#pithanothta kathgorias C1
				pk1 = sum(p1)
		
				for i in range (0,K):
					if(pk1 == 0):
						m1[i] = 0
					else:
						m1[i] =(1/pk1) * (i*p[i])	#mesi entasi kathgorias C1
				mk1 = sum(m1)
		
				for j in range (K+1, 254):
					p[j] = counter[j]/(wsize**2)
					p2[j] = p[j]	#pithanothta C2
					if(p2[j] < 0):
						p2[j] = -p2[j]
				p2_k = sum(p2)

				for j in range (K+1, 254):
					if(pk2 == 0):
						m2[j] = 0
					else:
						m2[j] =(1/pk2) * (j*p[j])	#mesi entasi kathgorias C2
				mk2 = sum(m2)
		
		
		m_g = pk1*mk1 + pk2*mk2
		
		
		sb = pk1*((mk1 - m_g)**2) + pk2*((mk2 - m_g)**2)	#diakymansi metaksy kathgoriwn
			

		B[a][b] = sb		# megisto k (k*)
		



for a in range (1,m):
	for b in range (1,n):
		if(new[a][b] <= B[a][b]):	#Sygkrinw kathe pixel tis eikonas me to megisto katwfli ston B
			new[a][b] = 0
		else:
			new[a][b] = 255

matplot.imshow(new, cmap = 'gray')
matplot.show()
Image.fromarray(new.astype(numpy.uint8)).save(output)
print("Xronos: ", datetime.now() - startTime)






