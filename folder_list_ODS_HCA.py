# folder_list
# Last updated 201904051041

import os
import time
import datetime

output_file = open("ODS_HCA.txt", "w")

for root, dirs, files in os.walk("I:/"):
    for file in files:
        if file[0:8] == "ODS_HCA":
            print(os.path.join(root, file))
            output_file.write(os.path.join(root,file)+"\n")

input("The process is complete.")
