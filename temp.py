# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pylab import *
import matplotlib
import numpy as np

fe=8000
Te=1/fe
fo=1000

#Test préliminaire :
N=1024
n=arange(N)
figure(1)
plt.plot(n,'o')

x=cos(2*pi*n*fo/fe)
figure(2)
plt.plot(n,x)

figure(3)
plt.plot(n,x,'o-.')

figure(4)
plt.stem(n,x)

figure(5)
#Question 3.b :
X=fft(x,N)
plt.plot(abs(X))


# échelle en fréquences adaptée :
X=fft(x,N)
freq_reel=arange(N)/N*fe
figure(6)
plt.plot(freq_reel, abs(X))
figure(7)
plt.plot(freq_reel, abs(X),'o-.')


#Question 4 :
figure(8)
N=1024
 	# puis on fait varier N en fonction des valeurs de D=1/fo, 2/fo, 4/fo etc…
n=arange(N)
x=cos(2*pi*fo*n*Te)
plt.stem(n,x)

X=fft(x,N)
freq_reel=arange(N)/N*fe
figure(9)
plt.plot(freq_reel, abs(X))
figure(10)
plt.plot(freq_reel, abs(X),'o-.')

#Question 5 :
x=cos(2*pi*fo*n*Te)
M=1024
X=fft(x,M)

freq_reel=arange(M)/M*fe
figure(11)
plt.plot(freq_reel,abs(X))

X_shift=fftshift(X)

freq_reel_shift=arange(-M/2,M/2)/M*fe
figure(12)
plt.plot(freq_reel_shift,abs(X_shift))

import random, struct, math
N= 1024 
n=arange(N)
x=cos(2*pi*fo*n*Te)
random.seed(1)
w=np.random.randn(N)
figure(13)
plt.stem(n[0:50],w[0:50])
y=x+w   # <= nouveau signal bruité créé en perturbant x par w
figure(14) # signature temporelle des deux signaux x (propre) et y (bruité)
plt.stem(n[0:50],x[0:50])
figure(15)
plt.stem(n[0:50],y[0:50])





