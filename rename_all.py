from asyncio.windows_events import NULL
import time
import os
from os.path import join
  
  
# Getting the path of the file
path = "C:/Users/caspe/Desktop/TEST"

# This will create a properly organized
# list with all the filename that is
# there in the directory
list_ = os.listdir(path)

# Last interated element
last_t = NULL
# Increment for duplicate files
increment = 0

for file_ in list_:
    # Create the full path to the file.
    full_path = join(path, file_)

    # Obtaining the modification time (in seconds)
    # of the file (datatype=int)
    t = os.path.getmtime(full_path)

    # Converting the time to an epoch string
    # (the output timestamp string would
    # be recognizable by strptime() without
    # format quantifers)
    t_str = time.ctime(t)
    
    # Converting the string to a time object
    t_obj = time.strptime(t_str)
    
    # Transforming the time object to a timestamp
    # of ISO 8601 format
    form_t = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
    
    # Since colon is an invalid character for a
    # Windows file name Replacing colon with a
    # similar looking symbol found in unicode
    # Modified Letter Colon " " (U+A789)
    form_t = form_t.replace(":", "꞉")

    # If current file was created at the same time as last file
    #if os.path.exists(last_t):
    if last_t == os.path.split(full_path)[0] + '/' + form_t + "-" + str(increment) + os.path.splitext(full_path)[1] or last_t == os.path.split(full_path)[0] + '/' + form_t + "-" + str(increment-1) + os.path.splitext(full_path)[1] or last_t == os.path.split(full_path)[0] + '/' + form_t + os.path.splitext(full_path)[1]:
        """Add an increment at the end of the file name."""
        rename = os.path.split(full_path)[0] + '/' + form_t + "-" + str(increment) + os.path.splitext(full_path)[1]
        os.rename(full_path, rename)
        last_t = rename
        increment += 1
    else:
        """Name the file after it's creation time stamp."""
        rename = os.path.split(full_path)[0] + '/' + form_t + os.path.splitext(full_path)[1]
        os.rename(full_path, rename)
        last_t = rename
        increment = 0
    #else:
    #    print("stop")
    #    rename = os.path.split(full_path)[0] + '/' + form_t + "-" + str(increment) + "-" + str(increment2) + os.path.splitext(full_path)[1]
    #    os.rename(full_path, rename)
    #    last_t = rename
     #   increment2 += 1

    