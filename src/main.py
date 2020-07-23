#this script can import multiple HPLC traces, subtract a baseline for each, and then unify them into a single file
#uses tkinter GUI

#import the controller classes
import controllers.GUI_controller
import controllers.trace_controller


class MainController:
    
    def __init__(self):
        
        print("initializing program")
        
        self.number_of_traces = 3
        
        #build trace controller first so it can be sent to the trace controller
        print("building controllers")        
        self.trace_controller = controllers.trace_controller.TraceController(self.number_of_traces)
        self.GUI_controller = controllers.GUI_controller.GUIcontroller(self.trace_controller)
        
        
    def start(self):
        
        print("starting program")
        
        #creates the GUI controller
        self.GUI_controller.start_GUI()
        
        
#creates the main controller and calls the start function
program = MainController()
program.start()
