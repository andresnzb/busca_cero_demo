#! /usr/bin/env python

'''
Este es un script que busca el punto de
interseccion entre seno y coseno usando
el metodo de la biseccion.
'''

import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)
plt.clf()

x_values = np.linspace(0, np.pi, 100)
plt.plot(x_values, np.sin(x_values), label='sin(x)')
plt.plot(x_values, np.cos(x_values), label='cos(x)')

plt.xlabel('x [radianes]')
plt.legend()

def biseccion(func, a, b):
	'''
	Recibe una funcion y dos puntos en lados
	opuestos a una raiz, y encuentra la raiz
	usando el metodo de la biseccion.
	'''
	p = (a + b) / 2.
	if func(p) == 0:
		return p
	if func(a) * func(p) > 0:
		a = p
	else:
		b = p
	return p

def seno_menos_coseno(x):
	return np.sin(x) - np.cos(x)

raiz = biseccion(seno_menos_coseno, 0, 2)
plt.axvline(raiz)
plt.show()
