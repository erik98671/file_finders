

import os

class Folder_Finder:
    def __init__(self, path, search_term):
        self.path = path
        self.search_term = search_term

    def search(self):
        print(f"Begining search of {self.path} for {self.search_term}")
        for root, dirs, files in os.walk(self.path):
            for folder in dirs:
                #print(f"{root}\{folder}")

                if "100237" in folder.upper():
                    print(f"{root}\{folder}")
                    hold_user = input("\nPress enter to continue search: ")

        print("Search complete")

if __name__ == "__main__":
    path = r"V:"
    search_term = "RECYCLE" # "RECYCLE"

    tool = Folder_Finder(path, search_term)
    tool.search()
    
