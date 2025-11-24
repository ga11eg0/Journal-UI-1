import tkinter as tk
from practice_model import journal,Initializer
from view import Diary_UI

class Journal_controler:

    def __init__(self,window):
        
        self.initi = Initializer
        self.model = journal
        self.view = Diary_UI(window)

        self.view.bind_open_book(self.open_book)

        self.current_book = None
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
    def update_view(self):
        self.set_book_list()



if __name__ == "__main__":

    window = tk.Tk()
    App = Journal_controler(window)
    window.mainloop()