#run object class
#a run is a HPLC run, and consists of a file path, data (time, signal, norm signal)

class Run():
    
    def __init__(self, trace):
        
        print("buidling run instance")
        
        self.time_data = []
        self.signal_data = []
        
        self.trace = trace