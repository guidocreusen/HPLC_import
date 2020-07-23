import tkinter as tk
import GUI_elements.trace_input_block

class GUIcontroller():
    
    def __init__(self, trace_controller):
        
        print("building GUI controller object")
        self.trace_controller = trace_controller
         
        print("initializing GUI root / master frame")
        self.master = tk.Tk() # top level Frame, which also can start the program
        self.master.title("import, subtract, and combine HPLC traces") # sets the title displayed in the window frame bar
        
        #initiate creation of the trace input blocks
        self.build_trace_input_blocks()
        
        self.build_export_block()
        
    def build_trace_input_blocks(self):
        
        print("creating trace input blocks")
        self.trace_input_blocks = {} #creates a list for the trace input block objects
            
        #creates the input block objects
        for n in range(self.trace_controller.number_of_traces):
                    
            self.trace_input_blocks[n] = GUI_elements.trace_input_block.TraceInputBlock(self, self.trace_controller, self.master, n)
            self.trace_input_blocks[n].main_frame.pack()
                    
            print("created trace input block instance " + str(n))
                    
    def build_export_block(self):
            
        print("building export frame")
        export_frame = tk.Frame(self.master, relief = tk.GROOVE, bd = 3)
        tk.Button(export_frame, text = "export", command = self.export_measurement, padx = 10, pady = 2).pack()
        export_frame.pack()
        
        
    def export_measurement(self):
        
        print("starting export")
        
    def start_GUI(self):
        
        self.master.mainloop()