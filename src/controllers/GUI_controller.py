import tkinter as tk
import GUI_elements.trace_input_block

class GUIcontroller():
    
    def __init__(self):
        
        print("initializing GUI controller")
         
        print("initializing GUI root / master frame")
        self.master = tk.Tk() # top level Frame, which also can start the program
        self.master.title("import, subtract, and combine HPLC traces") # sets the title displayed in the window frame bar
        
        #initiate creation of the trace input blocks
        self.build_trace_input_blocks()
        
    def build_trace_input_blocks(self):
        
            print("building trace input frames")
            self.trace_input_blocks = {} #creates a list for the trace input block objects
            
            #creates the input block objects
            for trace_number in range(4):
                    self.trace_input_blocks[trace_number] = GUI_elements.trace_input_block.TraceInputBlock(self, trace_number)
                    print("created trace input block object " + str(trace_number))
                    
        
    def start_GUI(self):
        
        self.master.mainloop()