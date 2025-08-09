from clicker_manager import ClickerManager as Clicker
import tkinter as tk
import tkinter.ttk as ttk

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
        
        # Create a label
        self.label = ttk.Label(self.root, text="Welcome to PyMClicker!")
        self.label.pack(pady=20)

        # Create a button to start clicking
        self.switch_button = ttk.Button(self.root, text="Start Clicking", command=self.start_clicking)
        self.switch_button.pack(pady=10)

        # Create a button to open settings
        self.settings_button = ttk.Button(self.root, text="Settings", command=self.open_settings)
        self.settings_button.pack(pady=10)

    def start_clicking(self):
        """
        Starts the clicking process using the Clicker class.
        """
        #clicker_instance = Clicker()
        #clicker_instance.click()
        if self.is_clicking==False:
            self.is_clicking = True
            self.switch_button.config(text="Stop Clicking", command=self.stop_clicking)

    def stop_clicking(self):
        """
        Stops the clicking process.
        """
        if self.is_clicking==True:
            self.is_clicking = False
            self.switch_button.config(text="Start Clicking", command=self.start_clicking)

    
    def open_settings(self):
        """
        Opens the PyMClicker's settings window.
        """
        self.settings_window = tk.Toplevel(self.root)
        self.settings_window.resizable(False, False)
        self.settings_window.title("PyMSettings")
        self.settings_window.geometry("300x200")
        ttk.Label(self.settings_window, text="Define whether it should be a mouse button, keyboard key or set of keys.", wraplength=250).pack(pady=10)
        clicker_settings = {
            1: "mouse",
            2: "key",
            3: "set of keys"
        }
        for value, text in clicker_settings.items():
            clicker_settings = ttk.Radiobutton(self.settings_window, text=text, value=value)
            clicker_settings.pack(anchor=tk.W, padx=20)
        clicker_settings.pack()

if __name__ == "__main__":
    root = PyMClickerInterface()
    root.root.mainloop()