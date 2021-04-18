# File_Finder
# Last updated 202011091100

import os
import time
import datetime

class File_Finder:
    def __init__(self, root, output_filename, file_extension, filename_prefix):
        self.root = root
        self.output_filename = output_filename
        self.file_extension = file_extension
        self.filename_prefix = filename_prefix
    
    def main(self):
        print("The process is starting.")
        
        # Create output file
        output_file = open(self.output_filename, "w")        
        print("Opened file", self.output_filename)
        
        # Loop through the folders and files
        for self.root, dirs, files in os.walk(self.root):
            #print("Starting at root", self.root)
            
            for file in files:
                if self.filename_prefix in file:
                    file_time = time.ctime(os.path.getmtime(os.path.join(self.root, file)))
                    file_date = str(datetime.datetime.strptime(file_time, "%a %b %d %H:%M:%S %Y"))
                    output_file.write(str(file_date[0:10])+" "+os.path.join(self.root,file)+"\n")
                    print(str(file_date[0:10])+" "+os.path.join(self.root,file)+"\n")

        input("The process is complete. Press enter to quit.")

if __name__ == "__main__":
    root = r"H:\Timeline\2020"
    output_filename = "file_finder_H_NCPDP.txt"
    file_extension = ["*","*"]
    filename_prefix = "NCPDP"
    
    finder = File_Finder(root, output_filename, file_extension, filename_prefix)
    finder.main()

