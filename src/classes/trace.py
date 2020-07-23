#trace object class
#a trace consists of a baseline, and multiple measurements
import classes.run
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilenames
from tkinter import messagebox # required for messagebox to work, even with tkinter/tk.messagebox as messagebox import isn't part of tkinter __init__

class Trace():
    
    headerlines = 77
    column_time = 0
    column_signal = 2
    
    def __init__(self):
        
        print("building trace object")
        
        #initialize baseline run object and measurement run objects
        self.baseline_run = None
        self.measurement_runs = {}
        
    def load_baseline(self):
        
        baseline_filepath = askopenfilename(initialdir = "", filetypes = (("Text File", "*.txt"),), title = "Choose a baseline file.")
           
        #create the baseline run instance as an attribute
        self.baseline_run = self.load_file_to_run(baseline_filepath)
        
        
    def load_measurements(self):
        
        print("loading measurement files to trace")
        
        measurements_filepaths = askopenfilenames(initialdir = "", filetypes = (("Text File", "*.txt"),), title = "Choose measurement files.")
        measurements_filepaths_list = list(measurements_filepaths)
        
        
        print ("\nloading files: " + measurements_filepaths_list)
        
    #takes a file path and returns a run instance
    def load_file_to_run(self, filepath):
        
        print("loading file " + str(filepath) + " into run instance")
       
        try:
            #load all lines from the file into a list, and remove the newline ends
            file = open(filepath, 'r')
            file_lines = [line.strip('\n') for line in file.readlines()]
            print("opened file")
                
            #remove header lines
            for n in range(self.headerlines):
                del file_lines[0]
            print("deleted header lines")
            
            run = classes.run.Run(self)
            print("created run instance")
        
            #read the lines into a run, with the class-specified column indexes
            for n, line in enumerate(file_lines):                
                line_data = line.split('\t')                
                run.time_data[n] = float(line_data[self.column_time].replace(',','.'))
                run.signal_data[n] = float(line_data[self.column_signal].replace(',','.'))
                
            print("file to run conversion successful")
            return run
                
        except:
            
            print("file to run conversion failed")
            return None
        


        