import json
from pathlib import Path
 
class journal():
    
    def __init__(self,name: str, pages:list):
        self.name = name
        self.pages = pages

    # return the number of pages in total 
    def get_num_pages(self):
        return len(self.pages)

    # return the content of a specific page number
    def get_index_page_content(self,index: int):
        #prevent index being out of range
        if index > 0 and index <= len(self.pages):
            # we extract 1 cuz list index starts in 0, and in the program starts in 1 
            index-= 1
            return self.pages[index]
            print("page content updated successfully")
        else:
            print("error: index out of range, there are ",self.get_num_pages()," pages, and you are triying to write in  page ",index)

    #inserts content in a specific page index 
    def write_content(self,index: int, content: str):

        #prevent index being out of range
        if index > 0 and index <= len(self.pages):
            # we extract 1 cuz list index starts in 0, and in the program starts in 1 
            index-= 1
            self.pages[index]= content
        else:
            print("error: index out of range, there are ",self.get_num_pages()," pages, and you are triying to write in  page ",index)
    #add page 
    def add_page(self):
        self.pages.append("new page "+str(len(self.pages)+1))

    #delete page specific page index 
    def delete_page(self,index: int):
        # we extract 1 cuz list index starts in 0, and in the program starts in 1 
        index-= 1
        self.pages.pop(index)

    #checks if a file exist, recives file name, returns true/false
    def this_file_exists(self,filename:str):

        try: 
            base_dir = Path(__file__).resolve().parent
            sub_dir= str(base_dir)+"/books/directory.json"
            with open(sub_dir,"r") as file:
                names_directory = json.load(file)

            for i in names_directory:
                if i == filename:
                    return True
            
            return False
        except:
            print("ubavle to read directory,json")
            pass
    # saves names of files in directory 
    def include_file(self, filename):

        try:
            base_dir = Path(__file__).resolve().parent
            sub_dir= str(base_dir)+"/books/directory.json" 
            # opens an reads file
            with open(sub_dir,"r") as file:
                names_directory = json.load(file)
                # adds new directory
                names_directory.append(filename)
            
            #saves the modified file 
            with open(sub_dir,"w") as file:
                json.dump(names_directory,file, indent=4)


        except:
            pass
    
    # delete file 
    def dele_file(self,filename):

        try: 
            base_dir = Path(__file__).resolve().parent
            sub_dir= str(base_dir)+"/books/directory.json"
            #checks if file exist 
            filename = filename+".json"
            if self.this_file_exists(filename) == True:
                with open(sub_dir,"r") as file:
                    names_directory = json.load(file)
                    # removes file from directory json file list
                    names_directory.remove(filename)
            
                with open(sub_dir,"w") as file:
                    json.dump(names_directory,file, indent=4)
                print(filename," deleted from list succesfully")
            
                file_path = "books/"+filename
                file_to_delete = Path(file_path)
                file_to_delete.unlink(missing_ok=True)
                print(filename," deleted from directory succesfully")
            else:
                print(filename," does not exists")


        except:
            pass

    #saves file ,# --- Serialization Method (Saving) ---
    def creates_new_jornal(self):

        file_name= str(self.name)+".json"
        if self.this_file_exists(file_name) == False:
            str_path = "books/"+self.name+".json"
            filepath = Path(str_path)
            """Serializes the current object's data and writes it to a JSON file."""
            # 1. Convert the object state to a dictionary
            data = {
                "name": self.name,
                "pages": self.pages
            }

            # 2. Write the dictionary to the file path
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Successfully saved jornal '{self.name}' to {filepath}")
         
            self.include_file(file_name)

        else:
            print(self.name+".json file already exists")
    
    #save changes 
    def save_changes(self):

        file_name= str(self.name)+".json"
        base_dir = Path(__file__).resolve().parent
        
        if self.this_file_exists(file_name) == True:
            str_path = str(base_dir)+"/books/"+self.name+".json"
            filepath = Path(str_path)
            """Serializes the current object's data and writes it to a JSON file."""
            # 1. Convert the object state to a dictionary
            data = {
                "name": self.name,
                "pages": self.pages
            }

            # 2. Write the dictionary to the file path
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Successfully updated jornal '{self.name}' to {filepath}")
        
        else:
            print("changes could not be saved ",self.this_file_exists(file_name), " file name ", file_name )
    # returns a list with all available files
    def get_journal_list(self):

        try: 
            with open("books/directory.json") as file:
                names_directory = json.load(file)

                return names_directory
        except:
            pass

    
    # --- Deserialization Method (Loading - A Class Method) ---
    # decorator
    @classmethod
    def load_journal(cls,filename):
        
        try: 
            base_dir = Path(__file__).resolve().parent
            sub_dir= str(base_dir)+"/books/"
            file_path = sub_dir+filename
            file_full_path = Path(file_path)
            with open(file_full_path,"r") as file: 
                journal_data = json.load(file)
            
            return cls(
                name = journal_data["name"],
                pages = journal_data["pages"]
            )
        except:
            print(filename, "could not be open")

class Initializer():

    def __init__(self):
        self
        pass
    

    @classmethod
    def get_available_books(self):

        base_dir = Path(__file__).resolve().parent
        sub_dir= str(base_dir)+"/books/directory.json"
        print(sub_dir)
        with open(sub_dir) as file:
            names_directory = json.load(file)
            print(names_directory)
            return names_directory


    @classmethod
    def Initialize(self, filename):
        return journal.load_journal(filename)


def return_list_book():
    base_dir = Path(__file__).resolve().parent
    sub_dir= str(base_dir)+"/books/directory.json"
    print(sub_dir)
    with open(sub_dir) as file:
        names_directory = json.load(file)
        print(names_directory)
        return names_directory

print(" jdkjdelkkkdñdlñdldñld ")
ty= journal("journal 4",[])
print(ty.name)
ty.creates_new_jornal()