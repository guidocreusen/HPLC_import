#trace object class
#a trace consists of a baseline, and multiple measurements
import classes.run
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilenames

class Trace():
    
    def __init__(self):
        
        print("building trace object")
        
        #initialize baseline run object and measurement run objects
        self.baseline_run = None
        self.measurement_runs = {}
        
    def load_baseline(self):
        
        print("loading baseline file to trace")
        
        baseline_filepath = askopenfilename(initialdir = "", filetypes = (("Text File", "*.txt"),), title = "Choose a baseline file.")
        
    def load_measurements(self):
        
        print("loading measurement files to trace")
        
        measurements_filepath = askopenfilenames(initialdir = "", filetypes = (("Text File", "*.txt"),), title = "Choose measurement files.")
        
        