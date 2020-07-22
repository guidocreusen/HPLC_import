#this script can import multiple HPLC traces, subtract a baseline for each, and then unify them into a single file
#uses tkinter GUI

#import the controller classes
import controllers.GUI_controller


class MainController:
    
    def __init__(self):
        
        print("initializing program")
        
        self.GUI_controller = controllers.GUI_controller.GUIcontroller()
        
    def start(self):
        
        print("starting program")
        
        #creates the GUI controller
        self.GUI_controller.start_GUI()
        
        
#creates the main controller and calls the start function
program = MainController()
program.start()
