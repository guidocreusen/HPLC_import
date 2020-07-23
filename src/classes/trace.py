#trace object class
#a trace consists of a baseline, and multiple measurements
import classes.run
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilenames
from tkinter import messagebox # required for messagebox to work, even with tkinter/tk.messagebox as messagebox import isn't part of tkinter __init__

class Trace():
    
    def __init__(self):
        
        print("building trace object")
        
        #initialize baseline run object and measurement run objects
        self.baseline_run = None
        self.measurement_runs = {}
        
    def load_baseline(self):
        
        print("loading baseline file to trace")
        
        baseline_filepath = askopenfilename(initialdir = "", filetypes = (("Text File", "*.txt"),), title = "Choose a baseline file.")
        
        print ("\nloading file: " + baseline_filepath)
        
        try:
            baseline_file = open(baseline_filepath, 'r')
                
            # load all lines into a list, and remove the newline ends
            baseline_file_lines = [line.strip('\n') for line in baseline_file.readlines()] # in python3 map use is discouraged and ist comprehension is faster
                
            print("File readout:\n" + str(baseline_file_lines))
            
        except:
            
            return False
        
    def load_measurements(self):
        
        print("loading measurement files to trace")
        
        measurements_filepaths = askopenfilenames(initialdir = "", filetypes = (("Text File", "*.txt"),), title = "Choose measurement files.")
        measurements_filepaths_list = list(measurements_filepaths)
        
        
        print ("\nloading files: " + measurements_filepaths_list)

        