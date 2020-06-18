# ncp_finder
# Last updated 201903271440

import os
import time
import datetime

root = "S:/BraunE"
output_filename = "file_finder_S_BraunE_onetoc2.txt"
file_extension = ".onetoc2"

def main(root, output_filename,file_extension):
    # Create output file
    output_file = open(output_filename, "w")
    print("Opened file", output_filename)
    # Loop through the folders and files
    for root, dirs, files in os.walk(root):
        print("Starting at root",root)
        for file in files:
            print("Exaluating file",file)
            if file.endswith(file_extension):
                file_time = time.ctime(os.path.getmtime(os.path.join(root, file)))
                file_date = str(datetime.datetime.strptime(file_time, "%a %b %d %H:%M:%S %Y"))
                output_file.write(str(file_date[0:10])+" "+os.path.join(root,file)+"\n")
    return

print("The process is starting.")
main(root,output_filename,file_extension)
input("The process is complete. Press enter to quit.")
