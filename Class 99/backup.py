import os 
import shutil

source = input("ENTER THE FOLDER NAME")
destination = input("ENTER THE DESTINATION FOLDER")

source = source + '/'
destination = destination + '/'
listOfFiles = os.listdir(source)
for file in listOfFiles: 
    shutil.copy((source + file), destination)