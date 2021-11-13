import streamlit as st
import cv2
import web_data
import json
import web_train
import datetime as dt

# camera = cv2.VideoCapture(0)
# st.title("Smart Attendence Listing Web")
# text_inputs = st.sidebar.text_input("Please enter your Full Name: ")
# register_button = st.sidebar.button("Register Now")
# img_placeholder1 = st.empty()
# attendence_button = st.sidebar.button("Attendence")

# if register_button:
#     if len(text_inputs) > 3:
#         open_db = open("database.json", "r+")
#         load_db = json.load(open_db)
#         load_db.update({len(load_db)+1: text_inputs})
#         open_db.seek(0)
#         json.dump(load_db,open_db)
#         # print(load_db)
#         print(text_inputs)
#         frame=web_data.capture(len(load_db))
#         frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         img_placeholder1.image(frame)
#         web_train.trainer()

#     else:
#         st.sidebar.text("Name is too short. Please renter")

# if attendence_button:
#     camera=cv2.VideoCapture(0)
#     face_dectector = cv2.CascadeClassifier("D:\Image processing\AlgoExperts\Face_dec.xml")
#     recognizer = cv2.face.LBPHFaceRecognizer_create()
#     recognizer.read("My_Web_Model.xml")
#     open_name = open("database.json", "r+")
#     load_name = json.load(open_name)
#     img_placeholder2 = st.empty()
#     stop= st.button("Stop",key="stop")
#     while True:
#         sucess,frame=camera.read()
#         frame=cv2.flip(frame,1)
#         if sucess:
#             grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#             faces = face_dectector.detectMultiScale(grey, minNeighbors=10)
#             for x, y, w, h in faces:
#                 cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
#                 # frame[y:y+h, x:x+w]
#                 id,confidence = recognizer.predict(grey[y:y+h, x:x+w])
#                 confidence = round(100-confidence)

#                 if confidence > 40:
#                     cv2.putText(frame,load_name[str(id)],(x+5,y-5),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,0),3)
#                 else:
#                     cv2.putText(frame,"Unknown",(x+5,y-5),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,0),3)

#             frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#             img_placeholder2.image(frame)

#         if stop:
#             break