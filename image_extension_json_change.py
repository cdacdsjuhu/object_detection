import json


namelist=[]
with open(r'C:\Users\bhatiya\Desktop\LockdownWorkdone\json\extension.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]

        # add item to the list
        namelist.append(currentPlace)
print(len(namelist))
print(namelist)

extensions= ['png', 'jpeg', 'gif', 'svg']
json_file = r'C:\Users\bhatiya\Desktop\LockdownWorkdone\renaming_testing\sexual_part_detection_kissing.json'
with open(json_file, 'r+') as file:
    flag_dict = {}

    json_data = json.load(file)

    via_img_metadata = json_data['_via_img_metadata']

    for (image_id, attr) in via_img_metadata.items():

        filename = attr['filename']
        if filename in namelist:
            print(' workking on file ' + filename)
            for extn in extensions:
                if extn in filename:
                    newname= filename.replace(extn , "jpg")
                    image_idnew= image_id.replace(extn , "jpg")
                    attr['filename'] = newname
                    via_img_metadata[image_idnew] = via_img_metadata[image_id]
                    del via_img_metadata[image_id]
                    

