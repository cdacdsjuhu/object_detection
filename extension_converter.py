from PIL import Image
import glob
extensions= [ 'jpeg', 'png', 'ppm', 'bmp', 'pgm', 'tiff', 'bmp', 'JPEG', 'PNG', 'PPM', 'BMP', 'PGM', 'TIFF', 'BMP']
count=0
extenlist=[]
for exten in extensions:
    for file in glob.glob(r"C:\Users\bhatiya\Desktop\LockdownWorkdone\renaming_testing\Kissing_ver\*.%s"%(exten)):
        print(file)
        name= file[71:]
        extenlist.append(name)
        im = Image.open(file)
        #print(im)
        rgb_im = im.convert('RGB')

        rgb_im.save(file.replace("%s" %(exten), "jpg" ), quality=99)
        count= count+1


print("count is " + str(count))

with open(r'C:\Users\bhatiya\Desktop\LockdownWorkdone\renaming_testing\extension.txt', 'w') as filehandle:
    for listitem in extenlist:
        filehandle.write('%s\n' % listitem)
