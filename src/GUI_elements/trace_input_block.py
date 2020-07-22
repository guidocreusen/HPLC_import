import tkinter as tk

# creates a trace input block with the following features
#   shows a trace number
#   load and clear buttons for baseline and measurements
#   text field for name

class TraceInputBlock():
    
        def __init__(self, GUI_controller, master_frame, trace_number):
            
            print("initializing trace input block " + str(trace_number))
            
            self.GUI_controller = GUI_controller
            self.master_frame = master_frame
            self.trace_number = trace_number
            
            self.build_input_block()
            
        def build_input_block(self):
            
            print("building trace input block " + str(self.trace_number))
            
            # creates the tkinter Frame object holding the sub-frames (label, load/clear buttons, file count, name filed)
            self.main_frame = tk.Frame(self.master_frame, relief = tk.GROOVE, bd = 3)
            