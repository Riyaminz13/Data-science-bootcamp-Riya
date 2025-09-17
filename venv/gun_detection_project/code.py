import numpy as np
import cv2
import imutils
import datetime
import winsound
import time

gun_cascade = cv2.CascadeClassifier(r'D:\my my\python\venv\gun_detection_project\cascadef2.xml')
camera = cv2.VideoCapture(0)

firstFrame = None
gun_exist = None 
snapshot_taken = None
while True:
    ret, frame = camera.read()
    if not ret or frame is None:
        print("failed to grab frame.")
        break

    frame = imutils.resize(frame, width = 500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gun = gun_cascade.detectMultiScale(gray, 1.3, 5,minSize=(100,100))

    if len(gun) > 0:
        gun_exist = True
        # play sound alert 
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        # winsound.Beep(1000,500) # frequency: 1000HZ, duration: 500ms

    # save snapshot once 
        if not snapshot_taken:
            timestamp = datetime.datetime.now().strftime("%y-%m-%d_%H-%M-%S")
            filename = f"gun_detected_{timestamp}.jpg"
            cv2.imwrite(filename,frame)
            print(f"snapshot saved:{filename}")
            snapshot_taken = True

    time.sleep(1) #pause for 1 sec 
    for (x, y, w, h) in gun:
        frame = cv2.rectangle(frame, (x,y),(x+w, y+h),(255,0,0),2)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = frame[y : y + h, x : x + w]

    if firstFrame is None:
        firstFrame = gray
        continue

    cv2.imshow("security feed", frame)
    Key = cv2.waitKey(1) & 0xFF

    if Key == ord('q'):
        break

if gun_exist:
    print("guns detected")

else:
    print("gun not detected")

camera.release()
cv2.destroyAllWindows( )
