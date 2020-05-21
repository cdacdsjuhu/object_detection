import pickle
import json
json_file = r'C:\Users\bhatiya\Desktop\LockdownWorkdone\renaming_testing\sexual_part_detection_kissing.json'
count= 0
name_dict= {}
with open(json_file, 'r+') as file:
    flag_dict = {}

    json_data = json.load(file)

    via_img_metadata = json_data['_via_img_metadata']

    for (image_id, attr) in via_img_metadata.items():

        filename = attr['filename']
        #print( type(filename2))
        print(' workking on file ' + filename)

        newname= str(count)+'_'+filename[0]
        name_dict[filename]= newname

        image_idnew = str(count)+'_'+ image_id
        attr['filename'] = newname
        via_img_metadata[image_idnew] = via_img_metadata[image_id]
        del via_img_metadata[image_id]
        count=count+1


with open(json_file, 'r+') as jsonFile:
    json.dump(json_data, jsonFile)

print(name_dict)

pickle.dump( name_dict, open(r"C:\Users\bhatiya\Desktop\LockdownWorkdone\renaming_testing\save.p", "wb" ) )