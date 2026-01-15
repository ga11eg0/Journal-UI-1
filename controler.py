import tkinter as tk
from practice_model import journal,Initializer
from view import Diary_UI
 
class Journal_controler:

    def __init__(self,window):
        
        self.initi = Initializer
        self.model = journal
        self.view = Diary_UI(window)

        self.view.bind_open_book(self.open_book)
        self.view.bind_next_btn(self.next)
        self.view.bind_back_btn(self.back)
        self.view.bind_add_pg_btn(self.add_pg)
        self.view.bind_del_pg_btn(self.del_pg)
        self.view.bind_on_pg_change(self.update_changes)
        self.view.bind_new_book_btn(self.new_book)
        self.view.on_send_callback = self.create_book
        self.view.bind_delete_btn(self.delete_book)
   
      
        self.current_book = None
        self.i_index = 1 
        self.f_index = 1



        self.update_view()


    def set_book_list(self):
        books = self.initi.get_available_books()
        print(books)
        self.view.update_book_list(books)  

    def open_book(self):
        option = self.view.chosen.get()
        print("opcion elegida, ", option)
        self.current_book = self.model.load_journal(option)
        print(self.current_book.get_index_page_content(1))
        self.view.view_set_text(self.current_book.get_index_page_content(1))
        self.i_index = 1
        self.f_index = self.current_book.get_num_pages()
        index = "1/"+str(self.f_index)
        self.view.view_set_index(index)
        

    def set_text(self, index: int):
        a = 9
        
    def set_the_index():
        a = 9
    
    def next(self):
        
        if self.i_index < self.f_index:
            print("next pressed ")
            self.i_index += 1
            print("i1", self.i_index)
            self.view.view_set_text(self.current_book.get_index_page_content(self.i_index))
            index = str(self.i_index)+"/"+str(self.f_index)
            self.view.view_set_index(index)
        
    def back(self):

        if self.i_index > 1:
            print("back pressed ")
            self.i_index -= 1
            print("i1", self.i_index)
            self.view.view_set_text(self.current_book.get_index_page_content(self.i_index))
            index = str(self.i_index)+"/"+str(self.f_index)
            self.view.view_set_index(index)

    def add_pg(self):
        print("add page btn pressed")
        print(self.current_book.pages)
        self.current_book.add_page()
        print(self.current_book.pages)
        self.f_index += 1
        self.i_index = self.f_index
        self.view.view_set_text(self.current_book.get_index_page_content(self.i_index))
        index = str(self.i_index)+"/"+str(self.f_index)
        self.view.view_set_index(index)
        self.current_book.save_changes()
    
    def del_pg(self):
        if self.i_index > 1 :
            print("delete page btn pressed")
            print(self.current_book.pages)
            self.current_book.delete_page(self.i_index)
            print(self.current_book.pages)
            self.i_index -= 1
            self.f_index = self.current_book.get_num_pages()
            self.view.view_set_text(self.current_book.get_index_page_content(self.i_index))
            index = str(self.i_index)+"/"+str(self.f_index)
            self.view.view_set_index(index)
            self.current_book.save_changes()
    
    def update_changes(self,event):
        print("text is being changed")
        text = self.view.view_get_text()
        print(text)
        self.current_book.write_content(self.i_index,text)
        self.current_book.save_changes()
        
    def update_view(self):
        self.set_book_list()
        print("current book",self.current_book)

    def new_book(self):
        print("new book btn pressed")
        self.view.New_book_popup_win()
    
    def create_book(self, book_name):
        print("send button pressed ")
        new = self.model(book_name,[" new page 1"])
        new.creates_new_jornal()
        self.current_book = new
        print(self.current_book.get_index_page_content(1))
        self.view.view_set_text(self.current_book.get_index_page_content(1))
        self.i_index = 1
        self.f_index = self.current_book.get_num_pages()
        index = "1/"+str(self.f_index)
        self.view.view_set_index(index)
        books = self.current_book.get_journal_list()
        self.view.update_book_list(books) 
        
    def delete_book(self):
        print("delete book btn pressed ")
        self.current_book.dele_file(self.current_book.name)
        books = self.initi.get_available_books()
        print(books)
        self.view.update_book_list(books)  
        self.current_book = None
        self.view.view_set_text("")
        self.view.view_set_index("")
   

if __name__ == "__main__":

    window = tk.Tk()
    App = Journal_controler(window)
    window.mainloop()