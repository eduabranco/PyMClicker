import pyautogui
import time
from clicker import Clicker

class ClickerManager:
    def __init__(self):
        """
        Initializes the Clicker class.
        """
        self.clicker = Clicker()

    def click(self):
        """
        Starts the clicking process based on the selected button and duration.
        """
        if self.clicker.isclicking:
            print("Clicking is already in progress.")
            return
        self.clicker.isclicking = True
        button = self.clicker.selected_button
        duration = self.clicker.selected_duration

    def stop_clicking(self):
        """
        Stops the clicking process.
        """
    
    def set_button(self, button):
        """
        Sets the button to be used for clicking.
        :param button: The button to be used (e.g., "left", "right", "middle").
        """

    def set_click_type(self, click_type):
        type_of_click = ["Hold", "Single", "Multiple"]
        """
        Sets the type of click to be performed.
        :param click_type: The type of click (e.g., "Hold", "Single", "Multiple").
        """


    def set_hotkey(self, hotkey):
        """
        Sets the hotkey for starting/stopping the clicking process.
        :param hotkey: The hotkey to be set (e.g., "Ctrl+C").
        """

    def set_duration(self, duration):
        """
        Sets the duration for which the clicking will occur.
        :param duration: Duration in seconds.
        """
