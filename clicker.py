class Clicker:
    def __init__(self):
        """
        Initializes the Clicker class.
        Sets up the clicker with a default button and duration.
        """
        self.selected_button = ["left"]  # Default button
        self.selected_hotkey = ["Scroll_Lock"]  # Default hotkey
        self.selected_click_type = "Single"  # Default click type
        self.selected_duration = 0.1  # Default duration in seconds
        self.isclicking = False  # Flag to track if clicking is in progress
        self.b_or_k = "b"  # Default to button click

    def get_clicker_info(self):
        """
        Returns the current information of the clicker.
        :return: A dictionary containing the current button, hotkey, click type, duration, and clicking status.
        """
        return {
            "button": self.selected_button,
            "hotkey": self.selected_hotkey,
            "click_type": self.selected_click_type,
            "duration": self.selected_duration,
            "isclicking": self.isclicking,
            "b_or_k": self.b_or_k
        }