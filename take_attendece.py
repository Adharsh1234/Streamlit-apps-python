import cv2
camera=cv2.VideoCapture(0)
face_dectector = cv2.CascadeClassifier("Algoexperts\Face_dec.xml")
model = cv2.face.LBPHFaceRecognizer_create()
model.read("My_Web_Model.xml")
names = {1:"Adharsh"}

while True:
    sucess,frame=camera.read()
    frame=cv2.flip(frame,1)
    if sucess:
        
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_dectector.detectMultiScale(grey, minNeighbors=10)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            frame[y:y+h, x:x+w]
            id,confidence = model.predict(grey[y:y+h, x:x+w])
            confidence = round(100-confidence)

            if confidence > 40:
                cv2.putText(frame,names[id],(x+5,y-5),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,0),3)
            else:
                cv2.putText(frame,"Unknown",(x+5,y-5),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,0),3)


        # cv2.imshow('Face Recognition',frame)
        # end=cv2.waitKey(1)

        # if end == ord('q'):
        #     camera.release()
        #     cv2.destroyAllWindows()
        #     break