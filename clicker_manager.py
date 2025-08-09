import pyautogui
import time
from clicker import Clicker
import time

class ClickerManager:
    def __init__(self):
        """
        Initializes the Clicker class.
        """
        self.clicker = Clicker()

    def start_clicking(self):
        """
        Starts the clicking process based on the current settings.
        """
        if not self.clicker.isclicking:
            self.clicker.isclicking = True
            print("Clicking started with settings:", self.clicker.get_status())
            self.start_time = time.time()
            self._perform_mouse_clicks()
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

    def _perform_mouse_clicks(self):
        """
        Performs the clicking actions based on the current settings.
        """
        while (time.time() - self.start_time) < self.clicker.selected_duration:
            if not self.clicker.isclicking:
                break
            pyautogui.click(button=self.clicker.selected_button,)
        self.stop_clicking()

    def set_mouse_button(self, button):
        """
        Sets the mouse button to be used for clicking.
        :param button: The mouse button to be set (e.g., "left", "right", "middle").
        """
        if button not in ["left", "right", "middle"]:
            print(f"Invalid mouse button: {button}. Please choose from left, right, or middle.")
            return
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
        self.clicker.selected_hotkey.append(hotkey)
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
    
    def set_clicker_options(self):
        """
        Sets the options for the clicker.
        """
        button = input("Enter mouse button (left/right/middle): ").strip().lower()
        self.set_mouse_button(button)

        key = input("Enter keyboard key (a/b/c/...): ").strip().lower()
        self.set_keyboard_key(key)

        hotkey = input("Enter hotkey (e.g., Ctrl+C): ").strip().lower()
        self.clicker.selected_hotkey = []
        self.set_hotkey(hotkey)

        click_type = input("Enter click type (Single/Double): ").strip().lower()
        self.set_click_type(click_type)

        duration = float(input("Enter duration (in seconds): ").strip())
        self.set_duration(duration)

        b_or_k = input("Enter 'b' for button or 'k' for key: ").strip().lower()
        self.set_button_or_key(b_or_k)

    def run(self):
        """
        Starts the ClickerManager to handle clicking operations.
        """
        print("ClickerManager is running. Use start_clicking() to begin clicking.")
        while True:
            command = input("Enter command (start/stop/set/exit): ").strip().lower()
            if command == "start":
                self.start_clicking()
            elif command == "stop":
                self.stop_clicking()
            elif command == "set":
                self.set_clicker_options()
            elif command == "exit":
                self.stop_clicking()
                break
            else:
                print("Unknown command. Please use 'start', 'stop', 'set', or 'exit'.")