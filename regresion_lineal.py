import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


X = np.random.rand(50,1) * 10
Y = 2 * X + 1 + np.random.randn(50,1)

modelo = LinearRegression()
modelo.fit(X,Y)
y_pred = modelo.predict(X)
plt.scatter(X, Y, label="Datos")
plt.plot(X, y_pred, color="red", label="Modelo")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

print("Pendiente:", modelo.coef_[0])
print("Intersección:", modelo.intercept_)