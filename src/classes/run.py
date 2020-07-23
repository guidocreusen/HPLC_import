#run object class
#a run is a HPLC run, and consists of a file path, data (time, signal, norm signal)

class Run():
    
    def __init__(self, trace, filepath):
        
        print("buidling run instance")
        
        self.time_data = []
        self.signal_data = []
        
        split_filepath = filepath.split('/')
        self.filename = split_filepath[len(split_filepath)-1]
        print("assigned file name " + self.filename)
        
        self.trace = trace