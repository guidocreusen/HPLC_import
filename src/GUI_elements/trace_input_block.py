import tkinter as tk

# creates a trace input block with the following features
#   shows a trace number
#   load and clear buttons for baseline and measurements
#   text field for name

class TraceInputBlock():
    
        def __init__(self, GUI_controller, trace_number):
            
            print("initializing trace input block " + str(trace_number))
            