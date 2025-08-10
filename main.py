from clicker_manager import ClickerManager
import tkinter as tk
import tkinter.ttk as ttk
import os
try:
    import keyboard  # optional, may require root
    _KEYBOARD_AVAILABLE = (os.geteuid() == 0)
except Exception:
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

        if _KEYBOARD_AVAILABLE:
            self._poll_global_hotkey()
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

        # Focused-window hotkey (selected_hotkey) toggle
        self.root.bind(f"<{self.clicker_manager.clicker.selected_hotkey}>", lambda e: self.toggle_clicking())

        # If keyboard module usable (root), start polling hotkey (assume single key like 'f8')


    def _hotkey_status_text(self):
        if _KEYBOARD_AVAILABLE:
            return f"Global hotkey ({self.clicker_manager.clicker.selected_hotkey}) active."
        if keyboard is None:
            return f"keyboard lib unavailable; using window {self.clicker_manager.clicker.selected_hotkey}."
        return f"keyboard lib needs root; using window {self.clicker_manager.clicker.selected_hotkey}."

    def _poll_global_hotkey(self):
        # Only if keyboard usable
        if not self.clicker_manager.clicker.isclicking and keyboard.is_pressed(self.clicker_manager.clicker.selected_hotkey):
            self.start_clicking()
        elif self.clicker_manager.clicker.isclicking and keyboard.is_pressed(self.clicker_manager.clicker.selected_hotkey):
            self.stop_clicking()
        # Re-run after 150 ms
        self.root.after(150, self._poll_global_hotkey)

    def toggle_clicking(self):
        if self.clicker_manager.clicker.isclicking:
            self.stop_clicking()
        else:
            self.start_clicking()

    def start_clicking(self):
        """
        Starts the clicking process using the Clicker class.
        """
        if self.clicker_manager.clicker.isclicking:
            return
        self.clicker_manager.clicker.isclicking = True
        self.switch_button.config(text="Stop Clicking")
        self.label.config(text="Clicking...")
        self.clicker_manager.start_clicking()

    def stop_clicking(self):
        """
        Stops the clicking process.
        """
        if not self.clicker_manager.clicker.isclicking:
            return
        self.clicker_manager.clicker.isclicking = False
        self.switch_button.config(text="Start Clicking")
        self.label.config(text="Stopped.")
        self.clicker_manager.stop_clicking()

    def open_settings(self):
        """
        Opens the PyMClicker's settings window.
        """
        win = tk.Toplevel(self.root)
        win.resizable(False, False)
        win.title("PyMSettings")
        win.geometry("300x200")
        ttk.Label(win, text="(Settings placeholder)").pack(pady=20)

if __name__ == "__main__":
    app = PyMClickerInterface()
    app.root.mainloop()