import os
import shutil
import sys
import time

def filesToFolder(dirPath = "C:\Downloads"):
    files = os.listdir(dirPath)
    folderSet = set()

    # find all file types
    for file in files:
        fileType = file.split(".")[-1]
        folderSet.add(fileType)

    # create folders
    for folder in folderSet:
        tempPath = dirPath + "\\" + folder
        if not os.path.exists(tempPath):
            os.makedirs(tempPath)
        
    # move files to folders
    for file in files:

        fileType = file.split(".")[-1]
        origPath = dirPath + "\\" + file
        destPath = dirPath + "\\" + fileType
        
        if os.path.isfile(origPath):
            try:
                print("Moving file: " + file)
                shutil.move(origPath, destPath)
            except:
                print("Error moving file: " + file)
        

interval = 100

try:
    while True:
        print("Checking for new files...")
        filesToFolder(sys.argv[1])
        time.sleep(interval)
except KeyboardInterrupt:
    print("Exiting...")