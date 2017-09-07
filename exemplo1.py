import cv2

classificador = cv2.CascadeClassifier('cascades\haarcascade_frontalface_default.xml')

image = cv2.imread('pessoas\\pessoas4.jpg')
imageCinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Transformando imagem em escala de cinza

facesDetectadas = classificador.detectMultiScale(imageCinza, scaleFactor=1.1, minNeighbors=9, minSize=(30,30))

print(len(facesDetectadas))

for(x, y, l, a ) in facesDetectadas:
    print(x, y, l, a)
    cv2.rectangle(image, (x,y), (x + l, y + a), (0, 0, 255), 2)

cv2.imshow("Faces encontradas", image)
cv2.waitKey()