import cv2
import face_recognition as fr

video_capture = cv2.VideoCapture(0)

face = []
while True:
    _, frame = video_capture.read()
    face = fr.face_locations(frame)
    
    for (x,y,z,n) in face:
        cv2.rectangle(frame, (y,x), (n,z),(255,0,0), 2)

    cv2.imshow("face detector", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()