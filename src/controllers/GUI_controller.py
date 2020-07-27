import tkinter as tk
import GUI_elements.channel_input_block

class GUIcontroller():
    
    def __init__(self, channel_controller):
        
        print("building GUI controller object")
        self.channel_controller = channel_controller
         
        print("initializing GUI root / master frame")
        self.master = tk.Tk() # top level Frame, which also can start the program
        self.master.title("import, subtract, and combine HPLC channels") # sets the title displayed in the window frame bar
        
        #initiate creation of the channel input blocks
        self.build_channel_input_blocks()
        
        #initiate creation of the options block
        self.build_options_block()
        
        self.build_export_block()
        
    def build_channel_input_blocks(self):
        
        print("creating channel input blocks")
        self.channel_input_blocks = [] #creates a list for the channel input block objects
            
        #creates the input block objects
        for n in range(self.channel_controller.n_channels):
                    
            self.channel_input_blocks.append(GUI_elements.channel_input_block.ChannelInputBlock(self, self.channel_controller, self.master, n))
            self.channel_input_blocks[n].main_frame.pack()
                    
            print("created channel input block instance " + str(n))
            
    def build_options_block(self):
        print("building options frame")
        
        self.channel_controller.export_baseline_subtr = tk.IntVar()
        self.channel_controller.export_norm = tk.IntVar()
        print(str(self.channel_controller.export_baseline_subtr.get()))
        print(str(self.channel_controller.export_norm.get()))
        
        
        options_frame = tk.Frame(self.master, relief = tk.GROOVE, bd = 3)
        tk.Checkbutton(options_frame, text = "subtract baseline", variable = self.channel_controller.export_baseline_subtr).grid(row = 0)
        tk.Checkbutton(options_frame, text = "normalize (0-1)", variable = self.channel_controller.export_norm).grid(row = 1)
        options_frame.pack()
                    
    def build_export_block(self):
            
        print("building export frame")
        export_frame = tk.Frame(self.master, relief = tk.GROOVE, bd = 3)
        tk.Button(export_frame, text = "export", command = self.export_measurements, padx = 10, pady = 2).pack()
        export_frame.pack()
        
        
    def export_measurements(self):
        
        print("starting export")
        self.channel_controller.export_measurements()
        
        
        
    def start_GUI(self):
        
        self.master.mainloop()