#Una fabrica de neumaticos dispone de dos precios de venta para sus neumaticos del tipo 185/65 R15 T88
#para un Peugeot 207. El precio de cada neumatico al detalle es de 40 mil 
#pesos, mientras que el precio 
#unitario del mismo neumatico al por mayor es de 30 mil pesos, 
#considerando en este  ́ ultimo caso un costo 
#fijo adicional de 40 mil pesos por el total de la compra.
#a) Define las funciones que modelan los distintos precios.
#b) ¿Cuantos neumaticos se debe comprar para que el precio al por mayor
#sea mas conveniente? Compara  
#de forma grafica.}

#V.I cant de neumaticos.
#V.D costo a pagar.

def D(x):#forma por detalle
    return 40000*x

def M(x):#forma por mayor
    return 40000+30000*x
#GRAFICAR

import matplotlib.pyplot as plt
import numpy as np

def D(x):
    return 40000*x


def M(x):
    return 40000+30000*x

x = np.arange(0, 10, 1) #Define valores para el eje x: desde, hasta, diferencia de 1 en 1 x ejemplo

plt.plot(x, D(x), label = 'Al detalle') #Indicar lo que se grafica: x, función
plt.plot(x, M(x), label = 'Al por mayor') #Indicar lo que se grafica: x, función
plt.xlim(0 , 10) #Indica desde-hasta en eje x
plt.title('Costo a pagar segun candidad de neumaticos') #Indica título del gráfico
plt.xlabel('Cantidad de neumaticos') #Nombre eje x
plt.ylabel('Costo a pagar ($)') #Nombre eje y

plt.legend()
plt.grid(True) #Indicamos que haya cuadrícula
plt.show()



#DESPEJAR EL VALOR DE X

import numpy as np
from scipy.optimize import fsolve

def Interseccion(x): #Nombrar función para la V.I.

    return D(x) - M(x)#Función igualada a 0

x = np.linspace(0, 10, 1) #Parámetros donde buscará solución

solucion=fsolve(Interseccion, x)

print( f'{solucion[0]:.1f}')
#comparativa de valores
print(f"Detalle : ${D(5)}")
print(f"Al por mayor se pagara: ${M(5)}")