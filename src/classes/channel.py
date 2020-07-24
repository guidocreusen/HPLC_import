#channel object class
#a channel has one or multiple measurements, and one or zero baselines
import classes.run
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilenames
from tkinter import messagebox # required for messagebox to work, even with tkinter/tk.messagebox as messagebox import isn't part of tkinter __init__

class Channel():
     
    column_time = 0
    column_signal = 2
    
    def __init__(self, n_headerlines):
        
        print("building channel instance")
        
        self.n_headerlines = n_headerlines
        
        #initialize baseline run object and measurement run objects
        self.baseline_run = None
        self.measurement_runs = []
        
    def load_baseline(self):
        
        print("loading baseline")
        
        self.baseline_run = None
        
        baseline_filepath = askopenfilename(initialdir = "", filetypes = (("Text File", "*.txt"),), title = "Choose a baseline file.")
           
        #create the baseline run instance as an attribute
        self.baseline_run = self.load_file_to_run(baseline_filepath)
        
    #asks for filepaths and loads the files into the run list. Sorts runs alphabetically
    def load_measurements(self):
        
        print("loading measurements")
        self.measurement_runs = []
        
        measurements_filepaths = askopenfilenames(initialdir = "", filetypes = (("Text File", "*.txt"),), title = "Choose measurement files.")
        measurements_filepaths_list = sorted(list(measurements_filepaths))
        print("\nloading files: " + str(measurements_filepaths_list))
        
        for n, filepath in enumerate(measurements_filepaths_list):
            self.measurement_runs.append(self.load_file_to_run(filepath))
            print("loaded measurement file " + str(filepath) + " to run")
            
    #takes a file path and returns a run instance, and None upon failure.
    def load_file_to_run(self, filepath):
        
        print("loading file " + str(filepath) + " into run instance")
       
        try:
            #load all lines from the file into a list, and remove the newline ends
            file = open(filepath, 'r')
            file_lines = [line.strip('\n') for line in file.readlines()]
            print("opened file")
                
            #remove header lines
            for n in range(self.n_headerlines):
                del file_lines[0]
            print("deleted header lines")
            
            run = classes.run.Run(self, filepath)
            print("created run instance")
        
            #read the lines into a run, with the class-specified column indexes
            for n, line in enumerate(file_lines):                
                line_data = line.split('\t')                
                run.time_data.append(float(line_data[self.column_time].replace(',','.')))
                run.signal_data.append(float(line_data[self.column_signal].replace(',','.')))
                
            print("file to run conversion successful")
            return run
                
        except:
            
            print("file to run conversion failed")
            return None
        


        