# folder_list
# Last updated 201904051041

import os
import time
import datetime

path = r"I:\Archive\prd3\Madena_MMR\Claims\in"

output_file = open("Madina_folder_list.txt", "w")

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))
            output_file.write(os.path.join(root,file)+"\n")

input("The process is complete.")
