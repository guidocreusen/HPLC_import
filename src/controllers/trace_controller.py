#trace controller handles all trace objects
#a trace holds multiple measurements, and a single baseline

import classes.trace
from tkinter.filedialog import askopenfilename

class TraceController():
    
    def __init__(self, number_of_traces):
        
        print("building trace controller instance")
        
        self.number_of_traces = number_of_traces
        self.traces = {}
        
        self.create_traces()
        
    def create_traces(self):
        
        print("creating trace instances")

        #loop through the number of traces, and create the trace objects
        for n in range(self.number_of_traces):
            
            print("creating trace " + str(n))
            self.traces[n] = classes.trace.Trace()
