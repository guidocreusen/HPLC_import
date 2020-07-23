#trace controller handles all trace objects
#a trace holds multiple measurements, and a single baseline

import classes.trace
from tkinter.filedialog import askopenfilename

class TraceController():
    
    def __init__(self, number_of_traces):
        
        print("building trace controller instance")
        
        self.n_traces = number_of_traces
        self.traces = []
        
        self.create_traces()
        
    def create_traces(self):
        
        print("creating trace instances")

        #loop through the number of traces, and create the trace objects
        for n in range(self.n_traces):
            
            print("creating trace " + str(n))
            self.traces.append(classes.trace.Trace())
            
    def export_measurements(self):
        
        #overview of export function:
        # 1 - iterate through the first trace measurement list (enumerate)
        # 2 - iterature through the data points of each run
        # 3 - subtract baseline point for each, and write the result into new lists
        # 4 - write the data for each measurement into a file
        
        for n, run in enumerate(self.traces[0].measurement_runs):
            for m, t in enumerate(run.time_data):
                
                s1 = run.signal_data[m]
                s2 = self.traces[1].measurement_runs[n].signal_data[m]
                s3 = self.traces[2].measurement_runs[n].signal_data[m]
                new_row = [t, s1, s2, s3]
                
                print(str(new_row))
                
            
