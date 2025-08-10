import tkinter as tk
import tkinter.ttk as ttk
from clicker import Clicker
class PyMClickerSettings:
    def __init__(self, root, clicker_manager):
        self.root = root
        self.clicker_manager = clicker_manager
        self.open_settings()

    def open_settings(self):
        """
        Opens the PyMClicker's settings window.
        """
        win = tk.Toplevel(self.root)
        win.resizable(False, False)
        win.title("PyMSettings")
        win.geometry("300x400")
        ttk.Label(win, text="(Settings placeholder)").pack(pady=20)
        # Example setting: Mouse or Keyboard
        ttk.Label(win, text="Mouse or Keyboard:").pack(pady=5)
        m_or_k_var = tk.StringVar(value=self.clicker_manager.clicker.m_or_k)
        ttk.Combobox(win, textvariable=m_or_k_var, values=["m", "k"]).pack(pady=5)

        if self.clicker_manager.clicker.m_or_k == 'm':
            ttk.Label(win, text="Mouse Button:").pack(pady=5)
            mouse_button_var = tk.StringVar(value=self.clicker_manager.clicker.selected_button)
            ttk.Combobox(win, textvariable=mouse_button_var, values=["left", "right", "middle"]).pack(pady=5)
        elif self.clicker_manager.clicker.m_or_k == 'k':
            ttk.Label(win, text="Key_set:").pack(pady=5)
            key_var = tk.StringVar(value=self.clicker_manager.clicker.selected_button)
            ttk.Entry(win, textvariable=key_var).pack(pady=5)

        # Example setting: Change click type
        ttk.Label(win, text="Click Type:").pack(pady=5)
        click_type_var = tk.StringVar(value=self.clicker_manager.clicker.selected_click_type)
        ttk.Combobox(win, textvariable=click_type_var, values=["Single", "Double"]).pack(pady=5)
        # Example setting: Change duration
        ttk.Label(win, text="Duration (seconds):").pack(pady=5)
        duration_var = tk.IntVar(value=self.clicker_manager.clicker.selected_duration)
        ttk.Entry(win, textvariable=duration_var).pack(pady=5)
        def save_settings():
            self.clicker_manager.set_mouse_button(mouse_button_var.get())
            self.clicker_manager.set_click_type(click_type_var.get())
            self.clicker_manager.set_duration(duration_var.get())
            win.destroy()
        ttk.Button(win, text="Save", command=save_settings).pack(pady=10)