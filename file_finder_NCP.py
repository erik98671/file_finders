# ncp_finder
# Last updated 201902261015

import os
import time
import datetime

output_file = open("file_finder_I_NCP.txt", "w")

for root, dirs, files in os.walk("I:/"):
    for file in files:
        if file.endswith(".NCP"):
            file_time = time.ctime(os.path.getmtime(os.path.join(root, file)))
            file_date = str(datetime.datetime.strptime(file_time, "%a %b %d %H:%M:%S %Y"))
            output_file.write(str(file_date[0:10])+" "+os.path.join(root,file)+"\n")

input("The process is complete.")
