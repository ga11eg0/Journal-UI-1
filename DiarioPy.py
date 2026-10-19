import tkinter as tk
from controler import Journal_controler 

if __name__ == "__main__":

    window = tk.Tk()
    App = Journal_controler(window)
    window.mainloop()
