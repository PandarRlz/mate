import numpy as np

#conjunto de ele de la varible independiete
elementos = np.array([100,200,500,1000,2000])

#conjunto de ele de la variable dependiente
tiempo = np.array([2,4,10,20,40])
m,n=np.polyfit(elementos,tiempo,1)

print(f"La pendiente es {m:.2f}")
print(f"El coeficiente de poscicion es {n:.2f}")

#W

def tiempo(x): #Nombra funcion
    return 0.02*x #define funcion
print(f"Para 1500 ele el tiempo de ejecucion es de {tiempo(1500):.2f} ms")

#w

import numpy as np
from scipy.optimize import fsolve

def elementos(x): #nombrar funcion para la V.I
    return tiempo(x) - 50 # funcion igualdad a 0
x = np.linspace(0, 1500, 1) #parametros donde buscara solucion
solucion=fsolve(elementos, x)

print(f"Para 50 ms la cantidad de elementos es de {solucion[0]:.1f} unidades")
 