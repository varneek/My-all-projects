import cv2
import face_recognition as fr
import numpy as np
import csv
from datetime import datetime

# capturing video cam

video_capture = cv2.VideoCapture(0)

# load known faces

varneek1_image = fr.load_image_file("varneek1.jpg")
varneek1_encoding = fr.face_encodings(varneek1_image)[0]
varneek_image = fr.load_image_file("varneek.jpg")
varneek_encoding = fr.face_encodings(varneek_image)[0]

known_faces_encoding = [varneek1_encoding,varneek_encoding]
known_faces_name = ['varneek1','varneek']

#to copy names in the list

attendance = known_faces_name.copy()

face_locations = []
face_encodings = []

# get the current date and time

now = datetime.now()
current_date = now.strftime("%d-%m-%y")

f = open(f"{current_date}.csv","w+",newline="")
lnwritter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

# recognise faces
    face_locations = fr.face_locations(rgb_frame)
    face_encodings = fr.face_encodings(rgb_frame,face_locations)

    for face_encoding in face_encodings:
        matches = fr.compare_faces(known_faces_encoding, face_encoding)
        face_distance = fr.face_distance(known_faces_encoding, face_encoding)
        best_match = np.argmin(face_distance)

        if(matches[best_match]):
            name = known_faces_name[best_match]
        
        if name in known_faces_name:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomleftcorner = (10,100)
            fontscale = 1.5
            fontcolor = (255, 0 , 0)
            thickness = 3
            linetype = 2

            cv2.putText(frame, name, bottomleftcorner,font,fontscale,fontcolor,thickness,linetype) 

            if name in attendance:
                attendance.remove(name)
                current_time = now.strftime("%H-%M-%S")
                lnwritter.writerow([name,current_time])

    cv2.imshow("face detector", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
