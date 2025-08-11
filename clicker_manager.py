import pyautogui
import time
from clicker import Clicker
import threading

class ClickerManager(Clicker):
    def __init__(self):
        """
        Initializes the Clicker class.
        """
        super().__init__()
        self.isclicking = False
        self._click_thread = None

    def start_clicking(self):
        """
        Starts the clicking process based on the current settings.
        """
        if not self.isclicking:
            self.isclicking = True
            print("Clicking started with settings:", self.get_clicker_info())
            self._click_thread = threading.Thread(target=self._run_clicks, daemon=True)
            self._click_thread.start()
        else:
            print("Clicking is already in progress. Use stop_clicking to stop it.")

    def stop_clicking(self):
        """
        Stops the clicking process.
        """
        if self.isclicking:
            self.isclicking = False
            print("Clicking stopped.")
        else:
            print("Clicking is not in progress.")

    def _run_clicks(self):
        """The main loop for the clicking thread."""
        start_time = time.time()
        
        click_action = None
        if self.m_or_k == 'm':
            if self.selected_click_type == "Hold":
                self._perform_mouse_hold()
                self.isclicking = False
                return
            else: # Single or Double
                click_action = lambda: pyautogui.click(button=self.selected_button, clicks=1 if self.selected_click_type == "Single" else 2)
        elif self.m_or_k == 'k':
            if self.selected_click_type == "Hold":
                self._perform_keyboard_hold()
                self.isclicking = False
                return
            else: # Single or Double
                click_action = lambda: pyautogui.press(self.selected_button)

        if click_action:
            while self.isclicking and (time.time() - start_time) < self.selected_duration:
                click_action()
                # Add a small delay to prevent overwhelming the system
                # For double clicks, the interval is handled by pyautogui, but a small sleep is still good
                time.sleep(0.01)
        
        self.isclicking = False
        print("Clicking finished.")


    def _perform_mouse_hold(self):
        """
        Performs the mouse hold action based on the current settings.
        """
        pyautogui.mouseDown(button=self.selected_button)
        # Check periodically to allow stopping during hold
        end_time = time.time() + self.selected_duration
        while self.isclicking and time.time() < end_time:
            time.sleep(0.1)
        pyautogui.mouseUp(button=self.selected_button)

    def _perform_mouse_clicks(self):
        """
        Performs the clicking actions based on the current settings.
        """
        while (time.time() - self.start_time) < self.selected_duration:
            if not self.isclicking:
                break
            pyautogui.click(button=self.selected_button)
        self.stop_clicking()

    def _perform_keyboard_hold(self):
        """
        Performs the keyboard hold action based on the current settings.
        """
        pyautogui.keyDown(self.selected_button)
        # Check periodically to allow stopping during hold
        end_time = time.time() + self.selected_duration
        while self.isclicking and time.time() < end_time:
            time.sleep(0.1)
        pyautogui.keyUp(self.selected_button)

    def _perform_keyboard_clicks(self):
        """
        Performs the clicking actions based on the current settings.
        """
        while (time.time() - self.start_time) < self.selected_duration:
            if not self.isclicking:
                break
            pyautogui.press(self.selected_button)

    def set_mouse_button(self, button):
        """
        Sets the mouse button to be used for clicking.
        :param button: The mouse button to be set (e.g., "left", "right", "middle").
        """
        self.selected_button = button
        print(f"Mouse button set to: {button}")

    def set_keyboard_key(self, button):
        """
        Sets the keyboard key to be used for clicking.
        :param button: The keyboard key to be set (e.g., "a", "b", "c").
        """
        self.selected_button = button
        print(f"Keyboard key set to: {button}")

    def set_hotkey(self, hotkey):
        """
        Sets the hotkey for starting/stopping the clicking process.
        :param hotkey: The hotkey to be set (e.g., "Ctrl+C").
        """
        self.selected_hotkey = hotkey
        print(f"Hotkey set to: {hotkey}")

    def set_click_type(self, click_type):
        """
        Sets the type of click to be performed.
        :param click_type: The type of click (e.g., "Single", "Double", "Hold").
        """
        self.selected_click_type = click_type
        print(f"Click type set to: {click_type}")

    def set_duration(self, duration):
        """
        Sets the duration for which the click action will be performed.
        :param duration: Duration in seconds.
        """
        self.selected_duration = duration
        print(f"Click duration set to: {duration} seconds")

    def set_mouse_or_key(self, m_or_k):
        """
        Sets whether the click action is a mouse button or a keyboard key.
        :param m_or_k: "m" for mouse, "k" for key.
        """
        self.m_or_k = m_or_k
        print(f"Mouse or key set to: {m_or_k}")

#    def set_clicker_options(self):
#        """
#        Sets the options for the clicker.
#        """
#        while True:
#            m_or_k = input("Enter 'm' for mouse button or 'k' for key: ").strip().lower()
#            self.set_mouse_or_key(m_or_k)
#            if self.clicker.m_or_k == "m":
#                break
#            elif self.clicker.m_or_k == "k":
#                break
#            else:
#                print("Invalid input. Please enter 'm' or 'k'.")
#
#        if self.clicker.m_or_k == "m":
#            while True:
#                button = input("Enter mouse button (left/right/middle): ").strip().lower()
#                if button not in ["left", "right", "middle"]:
#                    print(f"Invalid mouse button: {button}. Please choose from left, right, or middle.")
#                    continue
#                self.set_mouse_button(button)
#                break
#        elif self.clicker.m_or_k == "k":
#            self.clicker.selected_button = []
#            while True:
#                key = input("Enter keyboard key (a/b/c/... or [ENTER] to end): ").strip().lower()
#                if key == "":
#                    break
#                self.set_keyboard_key(key)
#        
#        self.clicker.selected_hotkey = []
#        while True:
#            hotkey = input("Enter hotkey (e.g., Ctrl+C): ").strip().lower()
#            if hotkey == "":
#                break
#            self.set_hotkey(hotkey)
#
#        while True:
#            click_type = input("Enter click type (Single/Double/Hold): ").strip().lower()
#            if click_type not in ["single", "double", "hold"]:
#                print(f"Invalid click type: {click_type}. Please choose from Single, Double, or Hold.")
#                continue
#            self.set_click_type(click_type)
#            break
#
#        while True:
#            duration = input("Enter duration (in seconds) or just [ENTER] to use indefinitely: ").strip()
#            if duration == "":
#                self.set_duration(math.inf)
#                break
#            try:
#                duration = float(duration)
#                self.set_duration(duration)
#                break
#            except ValueError:
#                print(f"Invalid duration: {duration}. Please enter a number.")
#
#    def run(self):
#        """
#        Starts the ClickerManager to handle clicking operations.
#        """
#        print("ClickerManager is running. Use start_clicking() to begin clicking.")
#        while True:
#            command = input("Enter command (start/stop/set/exit): ").strip().lower()
#            if command == "start":
#                self.start_clicking()
#            elif command == "stop":
#                self.stop_clicking()
#            elif command == "set":
#                self.set_clicker_options()
#            elif command == "exit":
#                self.stop_clicking()
#                break
#            else:
#                print("Unknown command. Please use 'start', 'stop', 'set', or 'exit'.")