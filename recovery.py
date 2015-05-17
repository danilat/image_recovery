
import os
import shutil

dstDirectory = 'images/'
srcDirectory = '/Users/dani/Pictures/'

def fileVisit(a, dir, files):
    for f in files:
        fileName, fileExtension = os.path.splitext(f)
        if fileExtension == ".jpg" or fileExtension == ".png":
            shutil.copyfile(os.path.join(dir, f), dstDirectory + f)

if not os.path.exists(dstDirectory):
    os.makedirs(dstDirectory)
os.path.walk(srcDirectory, fileVisit, None)
    
