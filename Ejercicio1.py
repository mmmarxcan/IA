import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

suma = a+b
#print("Suma:",suma)

producto_punto = np.dot(a,b) #producto punto 
#print("Producto punto: ", producto_punto)

distancia = np.linalg.norm(a-b)
#print("Distancia euclidiana: ",distancia)

#Normalizar un vector

v = np.array([3,4])
norma = np.linalg.norm(v)
v_normalizado = v / norma

#print("Vector Original ", v)
#print("Vector Normalizado ", v_normalizado)

datos = np.random.randint(0,10,100)
media = np.mean(datos)
varianza = np.var(datos)
desviacion = np.std(datos)

"""print("Media",media)
print("Varianza",varianza)
print("Desviacion estandar",desviacion)"""

M = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])
det = np.linalg.det(M)
inv = np.linalg.inv(M)
print("Transpuesta: \n",M.T)
print("Determinante:",det)
print("Inversa: \n", inv)
