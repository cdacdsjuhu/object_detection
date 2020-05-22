

import os,cv2,json,filetype
from PIL import Image
import io,csv
import pandas as pd
from xml.etree.ElementTree import tostring
import xml.etree.cElementTree as ET

import os.path
from os import path

from xml.etree.ElementTree import Element, SubElement, Comment
import xml.etree.ElementTree as etree



json_file=r"/home/ayushi/sad_data/kissing/sexual_part_detection_kissing.json" 

out_path=r"/home/ayushi/sad_data/kissing/xmls"

work_dir=r"/home/ayushi/sad_data/Kissing_ver"
 
# download the xmls as per classes defined in list
region_category=["male_female_penetration","hand_job_to_girl","hand_job_to_boy","Cunnilingus","fellatio","kissing"]
#region_category=["breasts","Buttocks","penis","vulva"]
empty_images=0

li=[]

with open(json_file) as file:
    flag_dict = {}
 
    json_data = json.load(file)

    via_img_metadata = json_data['_via_img_metadata']


    for (image_id, attr) in via_img_metadata.items():

        filename = attr['filename']
        print(filename)
        
        file_size=attr['size']
                    
        ########################### Reading image file using opencv #############

        # get the Region attributes of file 
        regions = attr['regions']

        li=[]
        

        if regions==[]:
            #print("reading empty file with no attributes :{}".format(filename))
            empty_images+=1
            continue


        for parameters in regions:

            if os.path.exists(os.path.join(work_dir,filename)):
                img_path=work_dir+'/'+filename
                kind = filetype.guess(img_path) # or img != None
                if kind.extension=="jpg" or kind.extension=="png" or kind.extension=="jpeg" or kind.extension=="tiff" or kind.extension=="bmp":
                    img = cv2.imread(img_path)
                    #print("reading image file {}".format(img_path))
                    old_height,old_width,channel = img.shape
                    #print(old_height,old_width," height and weight of image")
            


                shape_attributes = parameters['shape_attributes']
                region_attributes = parameters['region_attributes']

                # extracting only rectangle shapes
                if shape_attributes['name'] == 'rect':
                    xmins = shape_attributes['x']
                    ymins = shape_attributes['y']
                    bbox_width = shape_attributes['width']
                    bbox_height = shape_attributes['height']

                    sexual_regions = region_attributes['sexual_regions']

                    for classid,_ in sexual_regions.items():

                        for cats in region_category:
                            if cats==classid:
                                print("filename:",filename)
                                print("old_height:",old_height)
                                print("old_width",old_width)
                                print("x:",xmins)
                                print("y:",ymins)
                                xmax=(xmins+bbox_width)
                                ymax=(ymins+bbox_height)
                                print("xmax:",xmax)      
                                print("ymax:",ymax)
                                print("width of bbox",bbox_width)
                                print("height of bbox",bbox_height)
                                print("class id is: ",classid)
                                print()
                                #my_dict[img_path]=[xmins,ymins,xmax,ymax]
                                li.append([classid,xmins,ymins,xmax,ymax])

                                print("creating xml file for {}".format(filename))

                                root = ET.Element("annotation")
                  
                                ET.SubElement(root, "folder").text = "OXFORD-IIIT Pet Dataset"
                                ET.SubElement(root, "filename").text = filename
                  
                  
                                source = ET.SubElement(root, "source")
                                ET.SubElement(source, "database").text = "OXFORD-IIIT Pet Dataset"
                                ET.SubElement(source, "annotation").text = "OXFORD-IIIT Pet Dataset"
                  
                  
                                size = ET.SubElement(root, "size")
                                ET.SubElement(size, "width").text = str(old_width)
                                ET.SubElement(size, "height").text = str(old_height)
                                ET.SubElement(size, "depth").text = "3"
                  
                  
                                ET.SubElement(root, "segmented").text = "0"
                   
                                for i in range(len(li)):
                                    object1 = ET.SubElement(root, "object")
                                    ET.SubElement(object1, "name").text = str(li[i][0])                          #classid
                                    ET.SubElement(object1, "pose").text = "Frontal"
                                    ET.SubElement(object1, "truncated").text = "0"
                                    ET.SubElement(object1, "occluded").text = "0"
                                    ET.SubElement(object1, "difficult").text = "0"
                      
                                    bndbox = ET.SubElement(object1, "bndbox")
                                    ET.SubElement(bndbox, "xmin").text =str(li[i][1])                #str(xmins)
                                    ET.SubElement(bndbox, "ymin").text =str(li[i][2])                #str(ymins)
                                    ET.SubElement(bndbox, "xmax").text =str(li[i][3])                #str((xmins+bbox_width))
                                    ET.SubElement(bndbox, "ymax").text =str(li[i][4])                #str((ymins+bbox_height))
                                         

                                    tree = ET.ElementTree(root)

                                    tree.write(out_path+"/"+filename+".xml")

                                print("xml file created for {}".format(filename))


print()
print("all xml files are created.....")
        



