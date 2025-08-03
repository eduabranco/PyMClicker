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
        Starts the clicking process based on the current settings.
        """
        if not self.clicker.isclicking:
            self.clicker.isclicking = True
            print("Clicking started with settings:", self.clicker.get_status())
            self._perform_clicks()
        else:
            print("Clicking is already in progress. Use stop_clicking to stop it.")

    def stop_clicking(self):
        """
        Stops the clicking process.
        """
        if self.clicker.isclicking:
            self.clicker.isclicking = False
            print("Clicking stopped.")
        else:
            print("Clicking is not in progress.")
            return

    def _perform_clicks(self):
        while self.clicker.isclicking:
            if self.clicker.b_or_k == "b":
                pyautogui.click(button=self.clicker.selected_button)
            else:
                pyautogui.hotkey(*self.clicker.selected_hotkey.split("+"))
            time.sleep(self.clicker.selected_duration)

    def set_mouse_button(self, button):
        """
        Sets the mouse button to be used for clicking.
        :param button: The mouse button to be set (e.g., "left", "right", "middle").
        """
        self.clicker.selected_button = button
        print(f"Mouse button set to: {button}")

    def set_keyboard_key(self, button):
        """
        Sets the keyboard key to be used for clicking.
        :param button: The keyboard key to be set (e.g., "a", "b", "c").
        """
        self.clicker.selected_button = button
        print(f"Keyboard key set to: {button}")

    def set_hotkey(self, hotkey):
        """
        Sets the hotkey for starting/stopping the clicking process.
        :param hotkey: The hotkey to be set (e.g., "Ctrl+C").
        """
        self.clicker.selected_hotkey = hotkey
        print(f"Hotkey set to: {hotkey}")

    def set_click_type(self, click_type):
        """
        Sets the type of click to be performed.
        :param click_type: The type of click (e.g., "Single", "Double").
        """
        self.clicker.selected_click_type = click_type
        print(f"Click type set to: {click_type}")

    def set_duration(self, duration):
        """
        Sets the duration for which the click action will be performed.
        :param duration: Duration in seconds.
        """
        self.clicker.selected_duration = duration
        print(f"Click duration set to: {duration} seconds")

    def set_button_or_key(self, b_or_k):
        """
        Sets whether the click action is a mouse button or a keyboard key.
        :param b_or_k: "b" for button, "k" for key.
        """
        self.clicker.b_or_k = b_or_k
        print(f"Button or key set to: {b_or_k}")

