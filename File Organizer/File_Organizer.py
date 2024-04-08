import os
import shutil

home = os.path.expanduser('~')
source_dir = f"{home}/Downloads/"
files = os.listdir(source_dir)

filedict = {
    f"{home}/Documents/Downloaded Documents/": ('.pdf', '.doc', '.docx', '.html', '.htm', '.odt', '.xls', '.xlsx', '.ods', '.ppt', '.pptx', '.txt'),   
    f"{home}/Pictures/Downloaded Pictures/": ('.jpg', '.jpeg', '.png', '.gif'),
    f"{home}/Documents/Bank Statements/": ('.csv', '.json', '.xml'),
    f"{home}/Downloads/Zip Files/": ('.zip', ".7z", '.rar'),
    f"{home}/Downloads/Installers/": ('.exe', '.jar', '.msi'),
    f"{home}/Downloads/Rain Meter Skins/": ('.rmskin', '.rmmisc', '.rmpack'),
    f"{home}/Videos/Downloaded Videos/": ('.mp4', '.mov', '.avi', '.wmv', '.webm', '.flv'),
    f"{home}/Music/Downloaded Music/":  ('.mp3', '.m4a', '.flac', '.wav', '.wma', '.aac')
    }

#File Directory Creator
def create_dir(directory):
    for x in directory: #scans through file dictionary
       path_exist = os.path.exists(x) #determines if file directory exists
       if path_exist == False: #if it doesn't create it
           os.mkdir(x)
       
#Organizes Files
def organize_file(directory): 
    for file in files: #scans files in source directory
        for x in directory: #scans through file dictionary
            if file.endswith(tuple(directory[x])): #uses the ext tuples to see if any files match any extensions
                shutil.move(os.path.join(source_dir, file), os.path.join(x, file)) #moves file to proper folder\
                
if __name__ == "__main__":
    create_dir(filedict) #put dictionary name in parameter
    organize_file(filedict) #put dictionary name in parameter