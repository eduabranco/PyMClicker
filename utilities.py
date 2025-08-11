import keyboard
class ClickerToogler():
    def __init__(self, stopper_key):
        self.stopper_key = stopper_key
        while True:
            if keyboard.is_pressed(self.stopper_key) and self.stopper_key:
                self.stopper_key = False
                print("Clicking stopped.")
            else:
                self.stopper_key = True
                print("Clicking is in progress.")