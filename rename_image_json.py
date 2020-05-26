import pickle
import json
import os
import cv2
work_dir= r'/home/ayushi/sad_data/neeraj_images/'
json_file = r'/home/ayushi/sad_data/neeraj/sexual_part_detection_27_04_P2_2.json'
name_dict= {}
images= os.listdir(work_dir)
count=1


with open(json_file, 'r+') as file:

    json_data = json.load(file)

    via_img_metadata = json_data['_via_img_metadata']

    for (image_id, attr) in via_img_metadata.items():

        filename = attr['filename']
        if filename in images:

            print(' workking on file ' + filename)

            newname= str(count)+'_nj_'+".jpg"
            name_dict[filename]= newname
            im= cv2.imread(work_dir +'//' +filename)
            os.rename(work_dir + "//" + filename, work_dir + "//" + newname)
            print("{} file renamed into {}".format(filename, newname))
            size= attr['size']

            image_idnew = str(count)+'_nj_'+".jpg"+ str(size)
            attr['filename'] = newname
            via_img_metadata[image_idnew] = via_img_metadata[image_id]
            del via_img_metadata[image_id]
            count=count+1


with open(json_file, 'w') as jsonFile:
    json.dump(json_data, jsonFile)

print(name_dict)