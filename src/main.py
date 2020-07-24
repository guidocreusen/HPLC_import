#this script can import multiple HPLC channels, subtract a baseline for each, and then unify them into a single file
#uses tkinter GUI

#import the controller classes
import controllers.GUI_controller
import controllers.channel_controller


class MainController:
    
    def __init__(self):
        
        print("initializing program")
        
        self.number_of_channels = 3
        
        #build channel controller first so it can be sent to the channel controller
        print("building controllers")        
        self.channel_controller = controllers.channel_controller.ChannelController(self.number_of_channels)
        self.GUI_controller = controllers.GUI_controller.GUIcontroller(self.channel_controller)
        
        33
    def start(self):
        
        print("starting program")
        
        #creates the GUI controller
        self.GUI_controller.start_GUI()
        
        
#creates the main controller and calls the start function
program = MainController()
program.start()
