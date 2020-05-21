import os
import cv2
path=r"/home/ayushi/sad_data/Fellatio_ver"
images=os.listdir(path)

for image in images:
  imgp= path+'/'+ image
  print(imgp)
  im=cv2.imread(imgp,1)
  print(im)

#===Alternative Code
import utils_db
import cv2
import os
from PIL import Image


input_dir =  "./data/original/"

dataset = utils_db.get_dataset(input_dir)
paths, labels = utils_db.get_image_paths_and_labels(dataset)

print('Number of classes: %d' % len(dataset))
print('Number of images: %d' % len(paths))
        
for path in paths:
    #print(path)
    #im = cv2.imread(path)

    try:
      img = Image.open(path) # open the image file
      img.verify() # verify that it is, in fact an image
      
    except (IOError, SyntaxError) as e:
      print('Bad file:', path) # print out the names of corrupt files
      os.remove(path)
'''
