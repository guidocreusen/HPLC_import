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
        self.temp_frame = tk.Tk()
        self.ask_channel_number()
        self.temp_frame.destroy()
        
        
        
        
        #build channel controller first so it can be sent to the channel controller
        print("building controllers")        
        self.channel_controller = controllers.channel_controller.ChannelController(self.number_of_channels)
        self.GUI_controller = controllers.GUI_controller.GUIcontroller(self.channel_controller)
        
    def start(self):
        
        print("starting program")
        
        #creates the GUI controller
        self.GUI_controller.start_GUI()
        
    def ask_channel_number(self):
        
        print("asking channel number")
        answer = simpledialog.askinteger("Input", "Number of channels to combine?", parent=self.temp_frame, minvalue=0, maxvalue=4)
        print(str(answer))
        
        if answer is None:
            self.ask_channel_number()
        else:
            self.number_of_channels = answer
        
        
#creates the main controller and calls the start function
program = MainController()
program.start()
