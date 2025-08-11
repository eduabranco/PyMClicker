from clicker_manager import ClickerManager
import tkinter as tk
import tkinter.ttk as ttk
import os
from settings import PyMClickerSettings
try:
    import keyboard  # optional, may require root
    _KEYBOARD_AVAILABLE = True
except (ImportError, OSError):
    keyboard = None
    _KEYBOARD_AVAILABLE = False

class PyMClickerInterface():
    def __init__(self):
        """
        Initializes the PyMClicker interface.
        Sets up the main application window and its components.
        """
        self.root = tk.Tk()
        self.root.title("PyMClicker")
        self.root.geometry("300x200")
        self.clicker_manager = ClickerManager()

        # Create a label
        self.label = ttk.Label(self.root, text="Welcome to PyMClicker!")
        self.label.pack(pady=10)

        # Create a button to start clicking
        self.switch_button = ttk.Button(self.root, text="Start Clicking", command=self.toggle_clicking)
        self.switch_button.pack(pady=5)

        # Create a button to open settings
        self.settings_button = ttk.Button(self.root, text="Settings", command=self.open_settings)
        self.settings_button.pack(pady=5)

        self.status = ttk.Label(self.root, text=self._hotkey_status_text())
        self.status.pack(pady=5)
        
        self.setup_hotkey()
        self.update_ui_loop()


    def _hotkey_status_text(self):
        hotkey = self.clicker_manager.selected_hotkey
        if _KEYBOARD_AVAILABLE:
            return f"Global hotkey ({hotkey}) is active."
        else:
            return f"Press '{hotkey}' in-window to toggle."

    def setup_hotkey(self):
        if _KEYBOARD_AVAILABLE:
            try:
                keyboard.add_hotkey(self.clicker_manager.selected_hotkey, self.toggle_clicking, suppress=True)
            except Exception as e:
                print(f"Could not set global hotkey: {e}")
                self.root.bind(f"<{self.clicker_manager.selected_hotkey}>", lambda e: self.toggle_clicking())
        else:
            # Focused-window hotkey (selected_hotkey) toggle
            self.root.bind(f"<{self.clicker_manager.selected_hotkey}>", lambda e: self.toggle_clicking())

    def update_ui_loop(self):
        if self.clicker_manager.isclicking:
            self.switch_button.config(text="Stop Clicking")
            self.label.config(text="Clicking...")
        else:
            self.switch_button.config(text="Start Clicking")
            self.label.config(text="Stopped.")
        
        self.root.after(100, self.update_ui_loop)

    def toggle_clicking(self):
        if self.clicker_manager.isclicking:
            self.stop_clicking()
        else:
            self.start_clicking()

    def start_clicking(self):
        """
        Starts the clicking process using the Clicker class.
        """
        if self.clicker_manager.isclicking:
            return
        self.clicker_manager.isclicking = True
        self.clicker_manager.start_clicking()

    def stop_clicking(self):
        """
        Stops the clicking process.
        """
        if not self.clicker_manager.isclicking:
            return
        self.clicker_manager.isclicking = False
        self.clicker_manager.stop_clicking()

    def open_settings(self):
        """
        Opens the settings window for PyM
        """
        PyMClickerSettings(self.root, self.clicker_manager)
        # After settings are closed, we might need to update hotkeys
        self.root.after(100, self.update_settings_dependent_ui)

    def update_settings_dependent_ui(self):
        self.status.config(text=self._hotkey_status_text())
        # Re-register hotkeys if they changed
        if _KEYBOARD_AVAILABLE:
            keyboard.remove_all_hotkeys()
        else:
            self.root.unbind(f"<{self.clicker_manager.selected_hotkey}>")
        self.setup_hotkey()

if __name__ == "__main__":
    app = PyMClickerInterface()
    app.root.mainloop()