import pickle
import os
work_dir= r'C:\Users\bhatiya\Desktop\LockdownWorkdone\renaming_testing\Kissing_ver'
namelist = pickle.load( open( r"C:\Users\bhatiya\Desktop\LockdownWorkdone\renaming_testing\save.p", "rb" ) )
print(namelist)
keys = namelist.keys()
print(keys)
images= os.listdir(work_dir)
cnt=0
for image in images:
    if image in keys:
        image_files1 = namelist[image] +".jpg"
        os.rename(work_dir + "\\" + image, work_dir + "\\" + image_files1)
        print("{} file renamed into {}".format(image, image_files1))
        print()

        cnt += 1

print("total {} files renamed..".format(cnt))
