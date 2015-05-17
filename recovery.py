
import os
import shutil

def fileVisit(a, dir, files):
    for f in files:
        print f
        fileName, fileExtension = os.path.splitext(f)
        if fileExtension == ".jpg" or fileExtension == ".png":
            shutil.copyfile(os.path.join(dir, f), 'images/'+f)

os.path.walk('/Users/dani/Pictures/', fileVisit, None)
    
