# folder_list
# Last updated 201904051041

import os
import time
import datetime

output_file = open("Acrobat_folder_list.txt", "w")

for root, dirs, files in os.walk("C:/"):
    for file in files:
        if file.endswith(".exe"):
            print(os.path.join(root, file))
            output_file.write(os.path.join(root,file)+"\n")

input("The process is complete.")
