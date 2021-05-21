import os
import shutil

# Check to see if the Downloads folder has something
DOWNLOADS_FOLDER = f'{os.path.expanduser("~")}/Downloads'
try:
    os.path.isdir(DOWNLOADS_FOLDER)
except:
    print('The directory does not exist')


files = os.listdir(DOWNLOADS_FOLDER)
number_of_files = len(files)

# checks to see if there is anything inside the folders
if number_of_files > 0:
    print(f'Found {number_of_files} files and/or folders')
    for item in files:
        try:
            if os.path.isfile(os.path.join(DOWNLOADS_FOLDER, item)):
                # if item is a file then will remove using the os.remove() method
                os.remove(os.path.join(DOWNLOADS_FOLDER, item))
            else:
                # if item is a directory then will use shutil.rmtree to delete the folder inside
                shutil.rmtree(os.path.join(DOWNLOADS_FOLDER, item))
        except Exception as e:
            # prints out anything that goes wrong
            print(f'Unable to delete: f{item} \n Reason: f{e}')
print(f'There are no files left in the directory: \n\t{DOWNLOADS_FOLDER}')
