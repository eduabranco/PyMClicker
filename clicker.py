import pyautogui
import time
import interface

class Clicker:
    def __init__(self, selected_button="left", selected_duration=0.1):
        """
        Initializes the Clicker class.
        Sets up the clicker with a default button and duration.
        """
        self.selected_button = selected_button
        self.selected_duration = selected_duration
    
    def click(self):
        """
        Performs a click action at the current mouse position.
        If button is not specified, uses the default button.
        If duration is not specified, uses the default duration.
        """
        pyautogui.click(button=self.selected_button, duration=self.selected_duration)
    def set_button(self, button):
        """
        Sets the button to be used for clicking.
        """
        self.selected_button = button
    def set_duration(self, duration):
        """
        Sets the duration for the click action.
        """
        self.selected_duration = duration
    def get_button(self):
        """
        Returns the currently selected button.
        """
        return self.selected_button
    def get_duration(self):
        """
        Returns the currently selected duration.
        """
        return self.selected_duration
    def start_clicking(self):
        """
        Starts the clicking process.
        This method can be extended to include more complex clicking logic.
        """
        while True:
            self.click()
            time.sleep(self.selected_duration)
    def stop_clicking(self):
        """
        Stops the clicking process.
        This method can be extended to include logic to stop clicking.
        """
        # Placeholder for stopping logic
        pass
    def open_interface(self):
        """
        Opens the PyMClicker interface.
        This method initializes and runs the interface.
        """
        interface_instance = interface.PyMClickerInterface()
        interface_instance.root.mainloop()
