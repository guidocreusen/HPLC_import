#this script can import multiple HPLC channels, subtract a baseline for each, and then unify them into a single file
#uses tkinter GUI

#import the controller classes
import controllers.GUI_controller
import controllers.channel_controller
import tkinter as tk
from tkinter import simpledialog

class MainController:
    
    def __init__(self):
        
        print("initializing program")
        
        self.number_of_channels = 1
        self.n_headerlines = 0
        
        self.temp_frame = tk.Tk()
        self.temp_frame.lift()
        self.ask_channel_number()
        self.ask_headerline_number()
        self.temp_frame.destroy()
        
        
        
        
        #build channel controller first so it can be sent to the channel controller
        print("building controllers")        
        self.channel_controller = controllers.channel_controller.ChannelController(self.number_of_channels, self.n_headerlines)
        self.GUI_controller = controllers.GUI_controller.GUIcontroller(self.channel_controller)
        
    def start(self):
        
        print("starting program")
        
        #creates the GUI controller
        self.GUI_controller.start_GUI()
        
    def ask_channel_number(self):        
        print("asking number of channels")
        answer = simpledialog.askinteger("Input", "Number of channels to combine?", parent=self.temp_frame, minvalue=1, maxvalue=10)
        print(str(answer))
        
        if answer is None:
            self.ask_channel_number()
        else:
            self.number_of_channels = answer
            
    def ask_headerline_number(self):
        
        print("asking number of header lines")
        answer = simpledialog.askinteger("Input", "How many header lines does the file have? (standard 77 for Chromeleon)", parent=self.temp_frame, minvalue=0, maxvalue=1000)
        print(str(answer))
        
        if answer is None:
            self.ask_headerline_number()
        else:
            self.n_headerlines = answer
        
        
#creates the main controller and calls the start function
program = MainController()
program.start()
