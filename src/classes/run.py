#run object class
#a run is a HPLC run, and consists of a file path, data (time, signal, norm signal)

class Run():
    
    def __init__(self):
        
        print("buidling run object")
        
        self.time_data = {}
        self.signal_data = {}