import os
import shutil
#this program is gonna automatically move all the unneccesary stuff into one folder
sourcepath=input("Enter the path of the Desktop:  ")        #'C:\\Users\\AADARSH MEHDI\\Desktop'
os.chdir(sourcepath)
files=os.listdir()
if not os.path.exists('AllDATA'):
    os.mkdir('AllDATA')
for file in files:
    src=os.path.join(sourcepath,file)
    dsn=os.path.join(sourcepath,'AllDATA\\')
    if not str(file).endswith('.lnk'):
        print("Moving file:", file)
        shutil.move(src, dsn)
        print("Finished!")


