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
        self.is_clicking = False
        self.clicker = ClickerManager()

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

        # Focused-window hotkey (F8) toggle
        self.root.bind("<F8>", lambda e: self.toggle_clicking())

        # If keyboard module usable (root), start polling hotkey (assume single key like 'f8')
        self.global_hotkey = "f8"  # adapt as needed
        if _KEYBOARD_AVAILABLE:
            self._poll_global_hotkey()

    def _hotkey_status_text(self):
        if _KEYBOARD_AVAILABLE:
            return "Global hotkey (F8) active."
        if keyboard is None:
            return "keyboard lib unavailable; using window F8."
        return "keyboard lib needs root; using window F8."

    def _poll_global_hotkey(self):
        # Only if keyboard usable
        if not self.is_clicking and keyboard.is_pressed(self.global_hotkey):
            self.start_clicking()
        elif self.is_clicking and keyboard.is_pressed(self.global_hotkey):
            self.stop_clicking()
        # Re-run after 150 ms
        self.root.after(150, self._poll_global_hotkey)

    def toggle_clicking(self):
        if self.is_clicking:
            self.stop_clicking()
        else:
            self.start_clicking()

    def start_clicking(self):
        """
        Starts the clicking process using the Clicker class.
        """
        if self.is_clicking:
            return
        self.is_clicking = True
        self.switch_button.config(text="Stop Clicking")
        self.label.config(text="Clicking...")
        self.clicker.start_clicking()

    def stop_clicking(self):
        """
        Stops the clicking process.
        """
        if not self.is_clicking:
            return
        self.is_clicking = False
        self.switch_button.config(text="Start Clicking")
        self.label.config(text="Stopped.")
        self.clicker.stop_clicking()

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