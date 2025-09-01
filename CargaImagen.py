import cv2
import matplotlib.pyplot as plt

img = cv2.imread("imagen.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray], [0], None , [256],[0,256])


"""plt.imshow(img_rgb)
plt.title("Imagen Original")
plt.axis("off")
plt.show()
"""

"""plt.imshow(gray, cmap='gray')
plt.title("Escala de grises")
plt.axis("off")
plt.show()
"""

"""plt.plot(hist)
plt.title("Histograma")
plt.show()"""