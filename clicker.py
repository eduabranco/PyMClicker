class Clicker:
    def __init__(self):
        """
        Initializes the Clicker class.
        Sets up the clicker with a default button and duration.
        """
        self.selected_button = "left"  # Default button
        self.selected_hotkey = "F8"  # Default hotkey
        self.selected_click_type = "Single"  # Default click type
        self.selected_duration = 5  # Default duration in seconds
        self.isclicking = False  # Flag to track if clicking is in progress
        self.m_or_k = "m"  # Default to mouse click

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
            "m_or_k": self.m_or_k
        }