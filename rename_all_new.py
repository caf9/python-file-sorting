from asyncio.windows_events import NULL
import time
import os
import shutil
from os.path import join

#path = "C:/Users/caspe/Desktop/Iphone Sync/jpg"
#path = "C:/Users/caspe/Desktop/TEST"
path = "C:/Users/caspe/Desktop/Alle Filer/Video"
list_ = os.listdir(path)
increment = 0

database = {}

"""Create a database of all the files, to be able to work around duplicate dates."""
def create_db():
    new_database = {}
    for file_ in list_:
        path_to_file = join(path, file_)
        t = os.path.getmtime(path_to_file)
        t_str = time.ctime(t)
        t_obj = time.strptime(t_str)
        form_t = time.strftime("%d-%m-%Y %H:%M", t_obj)
        form_t = form_t.replace(":", "꞉")
        #print (form_t)
        #print (t)
        name, ext = os.path.splitext(file_)
        ext = ext[1:]
    
        if ext == '':
            continue
        else:
            if form_t in new_database:
                new_database[form_t] += 1
            else:
                new_database[form_t] = 0

    #print(new_database)
    return new_database

"""Do a simple reset of all filenames equal to the number of an incrementing integer."""
def reset_names():
    i = 10000
    for file_ in list_:
        path_to_file = join(path, file_)
        os.rename(path + "/" + file_, os.path.split(path_to_file)[0] + "/" + str(i) + os.path.splitext(path_to_file)[1])
        i += 1

"""Rename all files based on date."""
def rename_files():
    for file_ in list_:
        path_to_file = join(path, file_)
        t = os.path.getmtime(path_to_file)
        t_str = time.ctime(t)
        t_obj = time.strptime(t_str)
        form_t = time.strftime("%d-%m-%Y %H:%M", t_obj)
        form_t = form_t.replace(":", "꞉")

        if database.keys().__contains__(form_t):
            new_name = os.path.split(path_to_file)[0] + '/' + form_t + "-" + str(database[form_t]) + os.path.splitext(path_to_file)[1]
            database[form_t] -= 1
            os.rename(path_to_file, new_name)
        else:
            print("no images found")
            #continue

"""Sort all files into folders based on year."""
def sort_files_by_year():
    #year_folders = []

    # Sort all files into folders based on year
    for file_ in list_:
        #path_to_file = join(path, file_)
        name, ext = os.path.splitext(file_)
        month = name[3:5]
        year = name[6:10]
        ext = ext[1:]
        #print(month)
        #print(year)
        
        # folder 2021
        #   - folder for each month
        #       - all pics in correct "month" folder

        # We do not want folders, so skip it
        if ext == '':
            continue

        if os.path.exists(path + "/" + year):
            shutil.move(path + "/" + file_, path + "/" + year + "/" + file_)
        else:
            #new_year_folder = 
            os.makedirs(path + "/" + year)
            #year_folders.append(new_year_folder)
            shutil.move(path + "/" + file_, path + "/" + year + "/" + file_)
    
"""Sort the contents of each "year" folder, into "month" folders."""
def sort_each_year_folder_by_month():
    # Loop through each "year" folder
    # Inside each "year" sort files based on month
    for folder in list_:
        name, ext = os.path.splitext(folder)
        print (name)
        new_path = path + "/" + name
        new_list = os.listdir(new_path)

        # We only want folders
        if ext != '':
            continue

        for file_ in new_list:
            name, ext = os.path.splitext(file_)
            month = name[3:5]
            #ext = ext[1:]

            # We do not want folders, so skip it
            if ext == '':
                continue
            
            if os.path.exists(new_path + "/" + month):
                shutil.move(new_path + "/" + file_, new_path + "/" + month + "/" + file_)
            else:
                os.makedirs(new_path + "/" + month)
                shutil.move(new_path + "/" + file_, new_path + "/" + month + "/" + file_)

    

#

"""Step 1."""
#reset_names()

"""Step 2."""
#database = create_db()
#rename_files()

"""Step 3."""
#sort_files_by_year()
sort_each_year_folder_by_month()


