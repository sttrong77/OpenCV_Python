import cv2

classificadorFace = cv2.CascadeClassifier('cascades\\haarcascade_frontalface_default.xml')

classificadorOlhos = cv2.CascadeClassifier('cascades\\haarcascade_eye.xml')


image = cv2.imread('pessoas\\beatles.jpg')

imageCinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Transformando imagem em escala de cinza

facesDetectadas = classificadorFace.detectMultiScale(imageCinza)

for(x, y, l, a ) in facesDetectadas:
    cv2.rectangle(image, (x, y), (x + l, y + a), (0, 0, 255), 2)
    regiao = image[y:y + a, x:x + l] # pega a região do olho que está dentro de uma face
    regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
    olhosDetectados = classificadorOlhos.detectMultiScale(regiaoCinzaOlho, scaleFactor = 1.1, minNeighbors=3)
    print(olhosDetectados)
    for(ox, oy, ol, oa) in olhosDetectados:
        cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (255, 0, 255), 2)


cv2.imshow("Faces e olhos encontradas", image)
cv2.waitKey()