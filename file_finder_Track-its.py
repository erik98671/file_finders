# ncp_finder
# Last updated 201910250926

import os
import time
import datetime

import File_Finder

if __name__ == "__main__":
    root = r"H:\Timeline"
    output_filename = "file_finder_H_Track-it.txt"
    file_extension = ".docx"
    filename_prefix = "Track-it"
    
    finder = File_Finder.File_Finder(root, output_filename, file_extension, filename_prefix)
    finder.main()

