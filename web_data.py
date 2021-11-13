import cv2
def capture(user_id):
    # print ("capturing user")
    # print (user_id)
    camera = cv2.VideoCapture(0)
    face_dectector= cv2.CascadeClassifier("D:\Image processing\AlgoExperts\Face_dec.xml")
    id = str(user_id)
    count = 0

    while True:
        success, frame = camera.read()
        # print ("Taking images")
        frame = cv2.flip(frame, 1)
        grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces= face_dectector.detectMultiScale(grey,minNeighbors=6)
        for x,y,w,h in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            frame[y:y+h,x:x+w]
            count = count + 1
            cv2.imwrite("Data Set/user."+id+"."+str(count)+".jpeg", frame[y:y+h,x:x+w])
        if count > 50:
            break

    return frame