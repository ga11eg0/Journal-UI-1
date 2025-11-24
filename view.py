import tkinter as tk 
from tkinter import StringVar, ttk
from tkinter.ttk import Combobox

class Diary_UI:

    def __init__(self, window):

        self.window = window
        self.window.geometry("1000x800")

        self.chose_book_lab = tk.Label(window, text= "chose a book", font= "arial 12", bg =  '#A9DFBF')
        self.chose_book_lab.place(x= 20, y = 20,width= 150, height= 40)

        self.chosen = StringVar()
        self.book_list= Combobox(window, textvariable = self.chosen,state="readonly", width=150, font="arial 12")
        self.book_list.place( x= 20, y = 60, width= 150, height= 40)

        self.open_book_btn = tk.Button(window, text= "Open", font= "arial 12", bg= "#AD8DF8")
        self.open_book_btn.place( x= 20, y = 100,width= 150, height= 40)

        self.close_book_btn = tk.Button(window, text= "Close", font= "arial 12", bg= "#444FF3")
        self.close_book_btn.place( x= 20, y = 140,width= 150, height= 40)

        self.new_book_btn = tk.Button(window, text= "New Journal", font= "arial 12", bg= "#398BE9")
        self.new_book_btn.place( x= 20, y = 180,width= 150, height= 40)

        self.del_book_btn = tk.Button(window, text= "del current", font= "arial 12", bg= "#32F052")
        self.del_book_btn.place( x= 20, y = 220,width= 150, height= 40)

        self.del_pag_btn = tk.Button(window, text= "del",font= "arial 12", bg =  "#F15742")
        self.del_pag_btn.place( x= 180, y = 20, width= 60, height= 40)
        
        self.add_pag_btn = tk.Button(window, text= "add",font= "arial 12", bg =  "#51F142")
        self.add_pag_btn.place(x= 180, y = 60,width= 60, height= 40)

        self.back_btn = tk.Button(window, text= "Back",font= "arial 12", bg =  "#E7DA1E")
        self.back_btn.place(x= 390, y = 60,width= 100, height= 40)
        
        self.index_box = tk.Text(window,font= "arial 20")
        self.index_box.place(x= 490, y = 60,width= 100, height= 40)

        self.next_btn = tk.Button(window, text= "Next",font= "arial 12", bg =  "#2CB9E4")
        self.next_btn.place(x= 590 , y = 60,width= 100, height= 40) 

        self.text_page = tk.Text(window, height= 30, width= 80 , font= "arial 12")
        self.text_page.place( x = 180, y = 100  )

    def update_book_list(self,options: list):
        self.book_list.config( values= options)

    def bind_open_book(self, callback):
        self.open_book_btn.config(command=callback)



        



            

'''
if __name__ == "__main__":
    window= tk.Tk()
    app = Diary_UI(window)
    window.mainloop()
'''