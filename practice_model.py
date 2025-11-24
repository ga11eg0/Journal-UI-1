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
    def delete_content(self,index: int):
        # we extract 1 cuz list index starts in 0, and in the program starts in 1 
        index-= 1
        self.pages.pop(index)

    #checks if a file exist, recives file name, returns true/false
    def this_file_exists(self,filename:str):

        try: 
            with open("books/directory.json","r") as file:
                names_directory = json.load(file)

            for i in names_directory:
                if i == filename:
                    return True
            
            return False
        except:
            pass
    # saves names of files in directory 
    def include_file(self, filename):

        try: 
            with open("books/directory.json","r") as file:
                names_directory = json.load(file)
                names_directory.append(filename)
            
            with open("books/directory.json","w") as file:
                json.dump(names_directory,file, indent=4)


        except:
            pass
    
    # delete file 
    def dele_file(self,filename):

        try: 
            if self.this_file_exists(filename) == True:
                with open("books/directory.json","r") as file:
                    names_directory = json.load(file)
                    names_directory.remove(filename)
            
                with open("books/directory.json","w") as file:
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
    def save(self):

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
        elif self.this_file_exists(file_name) == True:
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
            print(f"Successfully updated jornal '{self.name}' to {filepath}")

        else:
            print(self.name+".json file already exists")
    
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
            file_path = "/home/paris/Documents/paris/Documents/Proyectos/OOP/books/"+filename
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

        try: 
            with open("/home/paris/Documents/paris/Documents/Proyectos/OOP/books/directory.json") as file:
                names_directory = json.load(file)

                return names_directory
        except:

            print("could not open available books")

    @classmethod
    def Initialize(self, filename):
        return journal.load_journal(filename)



