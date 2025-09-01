import cv2
import matplotlib.pyplot as plt

img = cv2.imread("imagen.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

(h, w ) = img.shape[:2]
center = (w//2 , h//2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img_rgb, M ,(w,h))

resized = cv2.resize(img_rgb , (200, 200))


## escala de grises
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray , 100 , 200)

plt.subplot(1,2,1)
plt.imshow(rotated)
plt.title("Imagen rotado")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(resized)
plt.axis("off")
plt.title("Imagen Reescalada")

plt.imshow(edges, cmap='gray')
plt.title("Bordes canny")
plt.axis("off")

plt.show()