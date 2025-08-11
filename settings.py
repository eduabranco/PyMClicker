import tkinter as tk
import tkinter.ttk as ttk
from clicker_manager import ClickerManager

class PyMClickerSettings:
    def __init__(self, root, clicker_manager=ClickerManager()):
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

        # --- Widgets ---
        # --- Save Button ---
        def save_settings():
            # Set mouse/key first
            self.clicker_manager.set_mouse_or_key(m_or_k_var.get())
            if m_or_k_var.get() == 'm':
                self.clicker_manager.set_mouse_button(button_var.get())
            else:
                self.clicker_manager.set_keyboard_key(button_var.get())

            self.clicker_manager.set_click_type(click_type_var.get())
            self.clicker_manager.set_duration(duration_var.get())
            self.clicker_manager.set_hotkey(hotkey_var.get())
            win.destroy()

        ttk.Button(win, text="Save", command=save_settings).pack(pady=10)

        # Click Type
        ttk.Label(win, text="Click Type:").pack(pady=5)
        click_type_var = tk.StringVar(value=self.clicker_manager.selected_click_type)
        click_type_combo = ttk.Combobox(win, textvariable=click_type_var, values=["Single", "Double", "Hold"], state="readonly")
        click_type_combo.pack(pady=5)

        # Duration
        ttk.Label(win, text="Duration (seconds):").pack(pady=5)
        duration_var = tk.IntVar(value=self.clicker_manager.selected_duration)
        ttk.Entry(win, textvariable=duration_var).pack(pady=5)
        
        # Hotkey
        hotkey_var = tk.StringVar(value=self.clicker_manager.selected_hotkey)
        ttk.Label(win, text="Hotkey:").pack(pady=5)
        ttk.Entry(win, textvariable=hotkey_var).pack(pady=5)

        # Mouse or Keyboard
        ttk.Label(win, text="Mouse or Keyboard:").pack(pady=5)
        m_or_k_var = tk.StringVar(value=self.clicker_manager.m_or_k)
        m_or_k_combo = ttk.Combobox(win, textvariable=m_or_k_var, values=["m", "k"], state="readonly")
        m_or_k_combo.pack(pady=5)

        # Button/Key Entry
        button_key_label = ttk.Label(win, text="Button/Key:")
        button_key_label.pack(pady=5)
        
        button_var = tk.StringVar(value=self.clicker_manager.selected_button)
        
        mouse_button_combo = ttk.Combobox(win, textvariable=button_var, values=["left", "right", "middle"], state="readonly")
        key_entry = ttk.Entry(win, textvariable=button_var)


        # --- Logic to show/hide widgets ---
        def update_input_widget(*args):
            if m_or_k_var.get() == 'm':
                key_entry.pack_forget()
                button_key_label.config(text="Mouse Button:")
                mouse_button_combo.pack(pady=5)
                if button_var.get() not in mouse_button_combo['values']:
                    button_var.set("left")
            else: # 'k'
                mouse_button_combo.pack_forget()
                button_key_label.config(text="Key:")
                key_entry.pack(pady=5)
        
        m_or_k_var.trace_add("write", update_input_widget)
        update_input_widget() # Initial call

