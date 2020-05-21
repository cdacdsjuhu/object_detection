import os
import cv2
path=r"/home/ayushi/sad_data/Fellatio_ver"
images=os.listdir(path)

for image in images:
  imgp= path+'/'+ image
  print(imgp)
  im=cv2.imread(imgp,1)
  print(im)