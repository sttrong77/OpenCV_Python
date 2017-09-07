import cv2

video = cv2.VideoCapture(0) #webcam

classificadorFace = cv2.CascadeClassifier('cascades\\haarcascade_frontalface_default.xml')

while True:
    conectado, frame = video.read()

    frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    facesDetectadas = classificadorFace.detectMultiScale(frameCinza, minSize=(70, 70))

    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(frame, (x,y), (x + l, y + a), (0, 255, 0), 2)

    cv2.imshow("Captura de video webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows() #liberação de memória