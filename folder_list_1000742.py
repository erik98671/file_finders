# folder_list
# Last updated 202009110914

import os
import time
import datetime

output_file = open("1000742.txt", "w")

for root, dirs, files in os.walk(r"H:\Timeline\2020"):
    for file in files:
        if "1000742" in file:
            print(os.path.join(root, file))
            output_file.write(os.path.join(root, file)+"\n")

input("The process is complete.")
