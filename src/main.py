# this script can import multiple HPLC traces, subtract a baseline for each, and then unify them into a single file
# uses tkinter GUI

#import the controller classes
import controllers.GUI_controller


class MainController:
    
    def __init__(self):
        
        print("initializing program")
        
        #TODO: create a GUI controller here
        
    def start(self):
        
        print("starting program")
        
        self.GUI_controller = controllers.GUI_controller.GUIcontroller()
        self.GUI_controller.start_GUI()
        
program = MainController()
program.start()
