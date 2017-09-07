import cv2
from cv2 import imshow

print(cv2.__version__)

imagem = cv2.imread('opencv-python.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", imagemCinza)
cv2.waitKey()