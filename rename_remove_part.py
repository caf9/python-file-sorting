from asyncio.windows_events import NULL
import time
import os
from os.path import join
  
  
path = "C:/Users/caspe/Desktop/TEST"
list_ = os.listdir(path)

for file_ in list_:
    full_path = join(path, file_)

    name, ext = os.path.splitext(file_)
    name = name.replace(" conv", "")
    final_name = os.path.split(full_path)[0] + '/' + name + os.path.splitext(full_path)[1]
    #rename = file_.replace("conv", "")
    print(name)
    #print(file_)
    os.rename(full_path, final_name)

    