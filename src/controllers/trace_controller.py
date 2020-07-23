#trace controller handles all trace objects
#a trace holds multiple measurements, and a single baseline

import classes.trace
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename 
from tkinter.filedialog import askdirectory

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
        
        #first ask for a folder to save to
        export_folder = askdirectory(initialdir = "", title = "Choose a folder.")
        print("chosen file path: " + export_folder)
        
        
        
        #overview of export function:
        # 1 - iterate through the first trace measurement list (enumerate)
        # 2 - iterature through the data points of each run
        # 3 - subtract baseline point for each, and write the result into new lists
        # 4 - write the data for each measurement into a file
        
        for n, run in enumerate(self.traces[0].measurement_runs):
            
            save_path = export_folder + "/" + run.filename.strip("UV_VIS_1.TXT") + ".TXT"
            save_file = open(save_path, 'w') # mode w means the file will be empty and overwritten
            
            save_file.write("time\tsignal1\tsignal2\tsignal3\tsubtr1\tsubtr2\tsubtr3\n")
            print("time\tsignal1\tsignal2\tsignal3")
                        
            for m, t in enumerate(run.time_data):
                
                s1 = run.signal_data[m]
                s2 = self.traces[1].measurement_runs[n].signal_data[m]
                s3 = self.traces[2].measurement_runs[n].signal_data[m]
                
                bs1 = s1 - self.traces[0].baseline_run.signal_data[m]
                bs2 = s2 - self.traces[1].baseline_run.signal_data[m]
                bs3 = s3 - self.traces[2].baseline_run.signal_data[m]
                
                print(str(t) + "\t" + str(s1) + "\t" + str(s2) + "\t" + str(s3) + "\t" + str(bs1) + "\t" + str(bs2) + "\t" + str(bs3))
                save_file.write(str(t) + "\t" + str(s1) + "\t" + str(s2) + "\t" + str(s3) + "\t" + str(bs1) + "\t" + str(bs2) + "\t" + str(bs3) + "\n")
                
                
                
            
