import streamlit as st
import cv2
import web_data
import json
import web_train
import datetime as dt
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

st.title("Smart Attendence Listing Web")
# camera = cv2.VideoCapture(0)
text_inputs = st.sidebar.text_input("Please enter your Full Name: ")
register_button = st.sidebar.button("Register Now")
img_placeholder1 = st.empty()
attendence_button = st.sidebar.button("Attendence")

if register_button:
    if len(text_inputs) > 3:
        open_db = open("database.json", "r+")
        load_db = json.load(open_db)
        load_db.update({len(load_db)+1: text_inputs})
        open_db.seek(0)
        json.dump(load_db,open_db)
        # print(load_db)
        # print(text_inputs)
        frame=web_data.capture(len(load_db))
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_placeholder1.image(frame)
        web_train.trainer()

    else:
        st.sidebar.text("Name is too short. Please renter")

class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.i = 0

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        i =self.i+1
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (95, 207, 30), 3)
            cv2.rectangle(img, (x, y - 40), (x + w, y), (95, 207, 30), -1)
            cv2.putText(img, 'F-' + str(i), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

        return img


if attendence_button:
    img=VideoTransformer.transform(frame)
    img_placeholder2 = st.empty()
    img_placeholder2.image(img)
    # camera=cv2.VideoCapture(0)
    # face_dectector = cv2.CascadeClassifier("D:\Image processing\AlgoExperts\Face_dec.xml")
    # recognizer = cv2.face.LBPHFaceRecognizer_create()
    # recognizer.read("My_Web_Model.xml")
    # open_name = open("database.json", "r+")
    # load_name = json.load(open_name)
    # stop= st.button("Stop",key="stop")
    # while True:
    #     sucess,frame=camera.read()
    #     frame=cv2.flip(frame,1)
    #     if sucess:
    #         grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #         faces = face_dectector.detectMultiScale(grey, minNeighbors=10)
    #         for x, y, w, h in faces:
    #             cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    #             # frame[y:y+h, x:x+w]
    #             id,confidence = recognizer.predict(grey[y:y+h, x:x+w])
    #             confidence = round(100-confidence)

    #             if confidence > 40:
    #                 cv2.putText(frame,load_name[str(id)],(x+5,y-5),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,0),3)
    #             else:
    #                 cv2.putText(frame,"Unknown",(x+5,y-5),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,0),3)

    #         frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            # 

    #     if stop:
    #         break