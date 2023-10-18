import cv2
import pygame

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

pygame.init()
pygame.mixer.init()

music = pygame.mixer.Sound('yt1s.com - Breaking Bad Theme Low Quality-[AudioTrimmer.com].mp3') 
music_played = False

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if not music_played:
            music.play()
            music_played = True

    cv2.imshow('Yüz Algılama', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
