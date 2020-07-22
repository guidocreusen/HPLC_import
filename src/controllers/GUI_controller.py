import tkinter as tk

class GUIcontroller():
    
    def __init__(self):
        
        print("initializing GUI controller")
         
        print("initializing GUI root / master frame")
        self.master = tk.Tk() # top level Frame, which also can start the program
        self.master.title("import, subtract, and combine HPLC traces") # sets the title displayed in the window frame bar
        
    def start_GUI(self):
        
        self.master.mainloop()