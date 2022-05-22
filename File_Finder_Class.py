#
# File_Finder_Class.py
# Last updated 202104180900

import os

class File_Finder_Class:
    def __init__(self):
        pass

    def get_all_file_list(self, root):
        file_list = list() # The thing to return
        
        for root, dirs, files in os.walk(root):
            for file in files:
                file_list.append(os.path.join(root, file))

        return file_list

    def get_matching_list(self, root, search_term, search_type):
        matching_list = list() # The thing to return

        if search_type == 1: # Starts with
            for file in self.get_all_file_list(root):
                file_path_split = file.split("/")
                file_name = file_path_split[-1]

                if file_name[0:len(search_term)] == search_term: 
                    matching_list.append(file)

        elif search_type == 2:  # Contains
            for file in self.get_all_file_list(root):
                if search_term in file:
                    print(f"File: {file}")
                    print(f"Root: {root}")
                    matching_list.append(file)
                    hold_for_user = input("")
        
        elif search_type == 3: # Ends with
            for file in self.get_all_file_list(root):
                if file.endswith(search_term): 
                    matching_list.append(file)

        return matching_list

    def write_html(self, file_list):
        with open("file_finder.html", "w") as html_output_file:
            # Write header
            header = """
                <!DOCTYPE html>
                <html>
                    <head>
                        <title>File Finder</title>
                    </head>
                    <body>
                    <h1 style="font-family:verdana;">Search Results:</h1>
                """
            html_output_file.write(header)

            # Write rows
            for file in file_list:
                html_output_file.write("<p><a href=" + file + ">" + file + "</a></p>")
            
            # Write footer
            html_output_file.write("</body></html>")

    def get_intersection_list(self, list_1, list_2):
        intersection_lists = list()
        set_1 = set(list_1)
        set_2 = set(list_2)
        set_intersection = set_1.intersection(set_2)
        intersection_lists = list(set_intersection)
        
        return intersection_lists
    
if __name__ == "__main__":
    finder = File_Finder_Class()
    
    root = r"H:\Timeline\2021"
    
    #search_term = "pdf"
    #search_term = "test"
    search_term = "recycle"

    # Testing searching files
##    for file in finder.get_all_file_list(root): print(file)
##    for file in finder.get_matching_list(root, search_term, 3): print(file) # 3 is ends with
##    for file in finder.get_matching_list(root, search_term, 2): print(file) # 2 is contains
##    for file in finder.get_matching_list(root, search_term, 1): print(file) # 1 is starts with
##    for file in finder.return_intersection(finder.get_matching_list(root, "t", 1),finder.get_matching_list(root, "pdf", 3)): print(file)
    

    # Testing writing html
##    finder.write_html(finder.get_all_file_list(root))

    finder.write_html(finder.get_matching_list(root, search_term, 2))

##    finder.write_html(finder.get_intersection_list(finder.get_matching_list(root, "Track-it", 1),
##                                                 finder.get_matching_list(root, "docx", 3)
##                                                 )
##                      )

'''
            for file in files:
                if file.endswith(self.file_extension) and file[0:8] == self.filename_prefix:
                    file_time = time.ctime(os.path.getmtime(os.path.join(self.root, file)))
                    file_date = str(datetime.datetime.strptime(file_time, "%a %b %d %H:%M:%S %Y"))
                    
                    output_file.write(str(file_date[0:10]) + " " + os.path.join(self.root,file) + "\n")
'''

