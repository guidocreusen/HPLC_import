#trace object class
#a trace consists of a baseline, and multiple measurements
import classes.run

class Trace():
    
    def __init__(self):
        
        print("building trace object")
        
        #initialize baseline run object and measurement run objects
        self.baseline_run = None
        self.measurement_runs = {}
        
        