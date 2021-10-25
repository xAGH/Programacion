import cv2 as cv

capturar_video = cv.VideoCapture(0)

if not capturar_video.isOpened():
    print("No se encontró cámara")
    exit()

while True:
    _,frame = capturar_video.read()
    cv.imshow("Imagen de cámara", frame)
    
    if cv.waitKey(1) == ord("q"):
        break

capturar_video.release()
cv.destroyAllWindows()