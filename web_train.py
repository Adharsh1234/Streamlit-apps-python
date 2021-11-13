# import cv2
# import numpy as np
# import os
# from PIL import Image

# def trainer():
#     path = "Data Set"
#     face_list = []
#     ids = []
#     recognizer = cv2.face.LBPHFaceRecognizer_create()

#     for img in os.listdir(path):
#         img_path=os.path.join(path, img)
#         # print(img_path)
#         # open_img=Image.open(img_path)
#         # open_img.convert("L")
#         open_img=cv2.imread(img_path,0)
#         # open_img=np.array(open_img,'uint8')
#         face_list.append(open_img)
#         get_id=img.split(".")[1]
#         ids.append(int(get_id))


#     print("Training Face Recognition Started")
#     recognizer.train(face_list,np.array(ids))
#     recognizer.write("My_Web_Model.xml")
#     print("Training Face Recognition Completed")
