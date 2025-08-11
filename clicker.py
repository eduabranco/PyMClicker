class Clicker:
    def __init__(self,selected_button="left", selected_hotkey="F8", selected_click_type="Single", selected_duration=5, m_or_k="m"):
        """
        Initializes the Clicker class.
        Sets up the clicker with a default button and duration.
        """
        self.selected_button = selected_button  # Default button
        self.selected_hotkey = selected_hotkey  # Default hotkey
        self.selected_click_type = selected_click_type  # Default click type
        self.selected_duration = selected_duration  # Default duration in seconds
        self.m_or_k = m_or_k  # Default to mouse click
        self.isclicking = False  # Flag to track if clicking is in progress


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