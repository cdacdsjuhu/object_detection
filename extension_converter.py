from PIL import Image
import glob
extensions= ['png', 'jpeg', 'gif', 'svg']
count=0
extenlist=[]
for exten in extensions:
    for file in glob.glob("F:\\test_extension_image\*.%s"%(exten)):
        print(file)
        name= file[24:]
        extenlist.append(name)
        im = Image.open(file)
        #print(im)
        rgb_im = im.convert('RGB')

        rgb_im.save(file.replace("%s" %(exten), "jpg" ), quality=99)
        count= count+1


print("count is " + str(count))

with open(r'C:\Users\bhatiya\Desktop\LockdownWorkdone\json\extension.txt', 'w') as filehandle:
    for listitem in extenlist:
        filehandle.write('%s\n' % listitem)