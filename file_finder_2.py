# ncp_finder
# Last updated 201902260830

import os
import time
import datetime

# Create array of menu items to select from
menu_items = ["Find files ending with"]

# Define the menu items
def get_menu_item():
    print("Menu:\n")
    for i in range(len(menu_items)):
        print((i+1), "-", menu_items[i])
    print("Q - Quit\n")
    menu_selection = input("Selection: ")
    print()
    return menu_selection

# Define the main loop
def main_loop():
    quit_flag = "N"
    while quit_flag == "N":
        selection = get_menu_item()
        if selection == "1":
            extension = get_extension()
            root_folder = get_root_folder()
            find_files(extension,root_folder)
            print("\nThe process is complete.\n")
        if selection.upper() == "Q":
            quit_flag = "Y"

# Define function(s)
def get_extension():
    user_input_extension = input("What is the file extension (txt, sql, doc, NCP): ")
    return user_input_extension

#
def get_root_folder():
    user_input_root_folder = input("What is the root folder (H:/): ")
    return user_input_root_folder

#
def find_files(extension,root_folder):
    output_file_name = "file_finder_2.txt"
    output_file = open(output_file_name, "w")
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file[-3:] == str(extension):
                file_time = time.ctime(os.path.getmtime(os.path.join(root, file)))
                file_date = str(datetime.datetime.strptime(file_time, "%a %b %d %H:%M:%S %Y"))
                output_file.write(str(file_date[0:10])+" "+os.path.join(root,file)+"\n")

# Run the main loop
main_loop()
