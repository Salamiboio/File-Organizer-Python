import os
import shutil
import time

source_dir = "/Users/Tyler/Downloads/"
files = os.listdir(source_dir)
filedict = {
    "/Users/Tyler/Documents/Downloaded Documents/": ('.pdf', '.doc', '.docx', '.html', '.htm', '.odt', '.xls', '.xlsx', '.ods', '.ppt', '.pptx', '.txt'),   
    "/Users/Tyler/Pictures/Downloaded Pictures/": ('.jpg', '.jpeg', '.png', '.gif'),
    "/Users/Tyler/Documents/Bank Statements/": ('.csv', '.json', '.xml'),
    "/Users/Tyler/Downloads/Zip Files/": ('.zip', ".7z", '.rar'),
    "/Users/Tyler/Downloads/Installers/": ('.exe', '.jar', '.msi'),
    "/Users/Tyler/Downloads/Rain Meter Skins/": ('.rmskin', '.rmmisc', '.rmpack'),
    "/Users/Tyler/Videos/Downloaded Videos/": ('.mp4', '.mov', '.avi', '.wmv', '.webm', '.flv'),
    "/Users/Tyler/Music/Downloaded Music":  ('.mp3', '.m4a', '.flac', '.wav', '.wma', '.aac')
    }

for file in files: #scans files in source directory
    for x in filedict: #scans through file dictionary
        if file.endswith(tuple(filedict[x])): #uses the ext tuples to see if any files match any extensions
            shutil.move(os.path.join(source_dir, file), os.path.join(x, file)) #moves file to proper folder