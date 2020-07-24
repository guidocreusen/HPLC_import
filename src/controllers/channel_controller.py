#channel controller handles all channel instances as well as exporting to file

import classes.channel
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename 
from tkinter.filedialog import askdirectory

class ChannelController():
    
    def __init__(self, number_of_channels, n_headerlines):
        
        print("building channel controller instance")
        
        self.n_channels = number_of_channels
        self.n_headerlines = n_headerlines
        self.channels = []
        
        self.create_channels()
        
    def create_channels(self):
        
        print("creating channel instances")

        #loop through the number of channels, and create the channel objects
        for n in range(self.n_channels):
            
            print("creating channel " + str(n))
            self.channels.append(classes.channel.Channel(self.n_headerlines))
            
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
            
            #create header string and write to file
            header_string = "time"
            for m in range(self.n_channels):
                header_string += "\tsignal" + str(m + 1)
            for m in range(self.n_channels):
                header_string += "\tsubtracted" + str(m + 1)
            for m in range(self.n_channels):
                header_string += "\tnornmalized" + str(m + 1)
            header_string += "\n"
            save_file.write(header_string)
            print(header_string)
                        
            #load run signal data into different lists
            runs = []
            for m in range(self.n_channels):
                runs.append(self.channels[m].measurement_runs[n].signal_data)
            
            #create an empty list to load baseline-subtracted runs into
            bg_subtr_runs = []
            for m in range(self.n_channels):
                bg_subtr_runs.append([])
            
            #subtract background and append each line the bg_subtr data list of the respective channel
            for m in range(len(run.time_data)):
                for i in range(self.n_channels):
                    bg_subtr_runs[i].append(runs[i][m] - self.channels[i].baseline_run.signal_data[m])
                
            #create an empty list to load normalized (baseline subtr.) runs into
            norm_subtr_runs = []
            for m in range(self.n_channels):
                norm_subtr_runs.append([])
            
            
            #find min and max of background-subtracted channels, correct, and save into list of normalizedrun data
            run_maxima = []
            run_minima = []
            for m in range(self.n_channels):
                run_maxima.append(max(bg_subtr_runs[m]))
                run_minima.append(min(bg_subtr_runs[m]))
            
            for m, t in enumerate(run.time_data):                
                write_string = str(t)
                
                for i in range(self.n_channels):
                    norm_subtr_runs[i].append((bg_subtr_runs[i][m]-run_minima[i])/(run_maxima[i]-run_minima[i]))
                    write_string += "\t" + str(runs[i][m])
                
                for i in range(self.n_channels):
                    write_string += "\t" + str(bg_subtr_runs[i][m])
                    
                for i in range(self.n_channels):
                    write_string += "\t" + str(norm_subtr_runs[i][m])
                    
                write_string += "\n"
                
                save_file.write(write_string)
