# # CODE-1

# import cv2
# import os
# import time
# import matplotlib.pyplot as plt


# cap = cv2.VideoCapture(0)
    
# if cap.isOpened():
#     ret, frame = cap.read()
#     print(ret)
#     print(frame)
# else:
#     ret = False

# img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# #directory = r"C:/Users/smarty/Desktop/"
# directory = r"/Users/pranavkhurana/Desktop/honeypotDebugged1/ss_webcam/"
# os.chdir(directory)
# print(os.listdir(directory)) 
# filename = 'Intruder.jpg'
# cv2.imwrite(filename, img1) 


# cap.release()



#CODE-1 ALTERNATE
import cv2
import os

cam = cv2.VideoCapture(0)

cv2.namedWindow("INTRUDER's REAL TIME PICTURE")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        directory = r"C:/Users/HP/Downloads/honeypot-project1/honeypotDebugged1/ss_webcam"
        os.chdir(directory)
        img_name = "intruder_image_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()



#CODE-2

# # import the opencv library
# import cv2
  
  
# # define a video capture object
# vid = cv2.VideoCapture(0)
  
# while(True):
      
#     # Capture the video frame
#     # by frame
#     ret, frame = vid.read()
  
#     # Display the resulting frame
#     cv2.imshow('pranavs video', frame)
      
#     # the 'q' button is set as the
#     # quitting button you may use any
#     # desired button of your choice
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
  
# # After the loop release the cap object
# vid.release()
# # Destroy all the windows
# cv2.destroyAllWindows()


# #CODE-3

# import cv2

# cap = cv2.VideoCapture(0)

# while(True):

#    # capture frame-by-frame
#    ret, frame = cap.read()

#    # Gray scale conversion
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#    # display the resulting frame
#    cv2.imshow("goeduhub", gray)

#    # press 'q' to remove window
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the capture
# cap.release()
# cv2.destroyAllWindows()

# #CODE-4: -------ERROR - save a video
# import numpy as np  
# import os
# import cv2  

# cap = cv2.VideoCapture(0)  

# # Define the codec and create VideoWriter object  

# fourcc = cv2.VideoWriter_fourcc(*'XVID')  
# out = cv2.VideoWriter('output.mp4',0x7634706d, 100.0, (640,480))  

# # name="pranav_video"
# # self._name = name + '.mp4'
# # self._cap = VideoCapture(0)
# # self._fourcc = VideoWriter_fourcc(*'MP4V')
# # self._out = VideoWriter(self._name, self._fourcc, 20.0, (640,480))

# directory = r"/Users/pranavkhurana/Desktop/honeypotDebugged1/ss_webcam/"
# os.chdir(directory)
# print(os.listdir(directory)) 

# while(cap.isOpened()):  
#     ret, frame = cap.read()  

#     if ret==True:  
#         out.write(frame)  
#         cv2.imshow('frame',frame)
        
#         if cv2.waitKey(1) & 0xFF == ord('q'):  
#             break
#     else:  
#         break  

# # Release everything if job is finished  
# cap.release()  
# out.release()  
# cv2.destroyAllWindows()  


#CODE-5

# import cv2

# img = cv2.VideoCapture(0)
# ret, frame = imgc.read()
# cv2.imshow('image',frame)
# k = cv2.waitKey(0)
# if k == 27:         # wait for ESC key to exit
#     cv2.destroyAllWindows()
# elif k == ord('s'): # wait for 's' key to save and exit
#     cv2.imwrite('messigray.png',img)
#     cv2.destroyAllWindows()



