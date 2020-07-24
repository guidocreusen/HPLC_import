import tkinter as tk

# creates a channel input block with the following features
#   shows a channel number
#   load and clear buttons for baseline and measurements
#   text field for name

class ChannelInputBlock():
    
        def __init__(self, GUI_controller, channel_controller, master_frame, channel_number):
            
            print("building channel input block instance " + str(channel_number))
            
            #catches the parameters and saves them as attributes for the instance
            self.GUI_controller = GUI_controller
            self.channel_controller = channel_controller
            self.channel_number = channel_number
            self.channel = channel_controller.channels[channel_number]
            self.master_frame = master_frame
            
            #creates tkinter IntVars to show the number of files loaded
            self.n_baseline = tk.IntVar(0)
            self.n_measurements = tk.IntVar(0)
            
            #initializing frame attributes, not sctrictly necessary but for clarity
            self.main_frame = None
            self.title_subframe = None
            self.buttons_subframe = None
            
            #calls the functions that build the GUI
            self.build_input_block()
            
            self.build_title_subframe()
            self.title_subframe.pack()
            
            self.build_buttons_subframe()
            self.buttons_subframe.pack()
            
        def build_input_block(self):
                        
            # creates the tkinter Frame object holding the sub-frames (label, load/clear buttons, file count, name filed)
            self.main_frame = tk.Frame(self.master_frame, relief = tk.GROOVE, bd = 3)
            
        def build_title_subframe(self):
            
            print("building title subframe for channel " + str(self.channel_number + 1))
            
            self.title_subframe = tk.Frame(self.main_frame)
            tk.Label(self.title_subframe, text = "channel " + str(self.channel_number + 1), font = "Helvetica 12 bold").pack(pady = 3)
            
        def build_buttons_subframe(self):
            
            print("building buttons subframe for channel " + str(self.channel_number + 1))
            
            self.buttons_subframe = tk.Frame(self.main_frame)
            
            tk.Label(self.buttons_subframe, text = "measurement files", font = "Helvetica 10").grid(row = 0, column = 0, padx = 5)
            tk.Button(self.buttons_subframe, text = "load", command = self.load_measurements, padx = 10, pady = 2).grid(row = 0, column = 1, padx = 5, pady = 2)
            tk.Button(self.buttons_subframe, text = "clear", command = self.clear_measurements, padx = 10, pady = 2).grid(row = 0, column = 2, padx = 5, pady = 2)
            
            tk.Label(self.buttons_subframe, text = "baseline file", font = "Helvetica 10").grid(row = 1, column = 0, padx = 5)
            tk.Button(self.buttons_subframe, text = "load", command = self.load_baseline, padx = 10, pady = 2).grid(row = 1, column = 1, padx = 5, pady = 2)
            tk.Button(self.buttons_subframe, text = "clear", command = self.clear_baseline, padx = 10, pady = 2).grid(row = 1, column = 2, padx = 5, pady = 2)
            
            tk.Label(self.buttons_subframe, textvariable = self.n_measurements, font = "Helvetica 12 bold").grid(row = 0, column = 3, padx = 5)
            tk.Label(self.buttons_subframe, textvariable = self.n_baseline, font = "Helvetica 12 bold").grid(row = 1, column = 3, padx = 5)
            
        def load_measurements(self):
            
            print("clicked load measurements button")
            
            self.channel.load_measurements()
            self.n_measurements.set(len(self.channel.measurement_runs))
            
            
        def clear_measurements(self):
            
            print("clicked clear measurements button")
            self.channel.measurement_runs = {}
            self.n_measurements.set(len(self.channel.measurement_runs))

            
        def load_baseline(self):
            
            print("clicked load baseline button")
            
            self.channel.load_baseline()
            
            if self.channel.baseline_run:
                self.n_baseline.set(1)
            else:
                self.n_baseline.set(0)
            
            
        def clear_baseline(self):
            
            print("clicked clear baseline button")
            self.channel.baseline_run = None
            
            if self.channel.baseline_run:
                self.n_baseline.set(1)
            else:
                self.n_baseline.set(0)