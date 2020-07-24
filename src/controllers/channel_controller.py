#channel controller handles all channel instances as well as exporting

import classes.channel
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename 
from tkinter.filedialog import askdirectory

class ChannelController():
    
    def __init__(self, number_of_channels):
        
        print("building channel controller instance")
        
        self.n_channels = number_of_channels
        self.channels = []
        
        self.create_channels()
        
    def create_channels(self):
        
        print("creating channel instances")

        #loop through the number of channels, and create the channel objects
        for n in range(self.n_channels):
            
            print("creating channel " + str(n))
            self.channels.append(classes.channel.Channel())
            
    def export_measurements(self):
        
        #first ask for a folder to save to
        export_folder = askdirectory(initialdir = "", title = "Choose a folder.")
        print("chosen file path: " + export_folder)
        
        
        
        #overview of export function:
        # 1 - iterate through the first channel measurement list (enumerate)
        # 2 - iterature through the data points of each run
        # 3 - subtract baseline point for each, and write the result into new lists
        # 4 - write the data for each measurement into a file
        
        for n, run in enumerate(self.channels[0].measurement_runs):
            
            save_path = export_folder + "/" + run.filename.strip("UV_VIS_1.TXT") + ".TXT"
            save_file = open(save_path, 'w') # mode w means the file will be empty and overwritten
            
            save_file.write("time\tsignal1\tsignal2\tsignal3\tsubtracted1\tsubtracted2\tsubtracted3\tnormalized1\tnormalized2\tnormalized3\n")
            print("time\tsignal1\tsignal2\tsignal3")
                        
            s1 = run.signal_data
            s2 = self.channels[1].measurement_runs[1].signal_data
            s3 = self.channels[2].measurement_runs[2].signal_data
            
            bs1 = []
            bs2 = []
            bs3 = []
            ns1 = []
            ns2 = []
            ns3 = []
            
            #subtract background and append each line to lists bs1/2/3
            for m in range(len(run.time_data)):                
                bs1.append(s1[m] - self.channels[0].baseline_run.signal_data[m])
                bs2.append(s2[m] - self.channels[1].baseline_run.signal_data[m])
                bs3.append(s3[m] - self.channels[2].baseline_run.signal_data[m])
            
            #find min and max of subtracted channels
            s1max = max(bs1)
            s1min = min(bs1)                    
            s2max = max(bs2)
            s2min = min(bs2)
            s3max = max(bs3)
            s3min = min(bs3)
            
            for m, t in enumerate(run.time_data):                
                ns1.append((bs1[m]-s1min)/(s1max-s1min))
                ns2.append((bs2[m]-s2min)/(s2max-s2min))
                ns3.append((bs3[m]-s3min)/(s3max-s3min))
                
                save_file.write(str(t) + "\t" + str(s1[m]) + "\t" + str(s2[m]) + "\t" + str(s3[m]) + "\t" + str(bs1[m]) + "\t" + str(bs2[m]) + "\t" + str(bs3[m]) + "\t" + str(ns1[m])  + "\t" + str(ns2[m])  + "\t" + str(ns3[m]) + "\n")
