import os
import shutil

source_dir = "/Users/Tyler/Downloads/"
files = os.listdir(source_dir)
filedict = {
    "C:/Users/Tyler/Documents/Downloaded Documents/": ('.pdf', '.doc', '.docx', '.html', '.htm', '.odt', '.xls', '.xlsx', '.ods', '.ppt', '.pptx', '.txt'),   
    "C:/Users/Tyler/Pictures/Downloaded Pictures/": ('.jpg', '.jpeg', '.png', '.gif'),
    "C:/Users/Tyler/Documents/Bank Statements/": ('.csv', '.json', '.xml'),
    "C:/Users/Tyler/Downloads/Zip Files/": ('.zip', ".7z", '.rar'),
    "C:/Users/Tyler/Downloads/Installers/": ('.exe', '.jar', '.msi'),
    "C:/Users/Tyler/Downloads/Rain Meter Skins/": ('.rmskin', '.rmmisc', '.rmpack'),
    "C:/Users/Tyler/Videos/Downloaded Videos/": ('.mp4', '.mov', '.avi', '.wmv', '.webm', '.flv'),
    "C:/Users/Tyler/Music/Downloaded Music/":  ('.mp3', '.m4a', '.flac', '.wav', '.wma', '.aac')
    }

for file in files: #scans files in source directory
    for x in filedict: #scans through file dictionary
        if file.endswith(tuple(filedict[x])): #uses the ext tuples to see if any files match any extensions
            shutil.move(os.path.join(source_dir, file), os.path.join(x, file)) #moves file to proper folder