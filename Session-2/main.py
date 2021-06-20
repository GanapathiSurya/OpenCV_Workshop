import cv2
cap = cv2.VideoCapture(0)

classifier = cv2.CascadeClassifier("haarcade_classifier.xml")
while True :
    ret,image = cap.read()
    if ret :
        faces = classifier.detectMultiScale(image)
        for face in faces :
            x,y,w,h = face
            image = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),3)
            cv2.imshow('My Window',image)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('c'):
        cv2.imwrite('Surya.png',image)
