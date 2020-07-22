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
            
            #initializing frame attributes, not sctrictly necessary but for clarity
            self.main_frame = None
            self.title_subframe = None
            
            self.build_input_block()
            
            self.build_title_subframe()
            self.title_subframe.pack()
            
        def build_input_block(self):
            
            print("building trace input block " + str(self.trace_number))
            
            # creates the tkinter Frame object holding the sub-frames (label, load/clear buttons, file count, name filed)
            self.main_frame = tk.Frame(self.master_frame, relief = tk.GROOVE, bd = 3)
            
        def build_title_subframe(self):
            
            print("building title subframe for trace " + str(self.trace_number))
            
            self.title_subframe = tk.Frame(self.main_frame)
            tk.Label(self.title_subframe, text = "trace " + str(self.trace_number), font = "Helvetica 12 bold").pack(pady = 3)