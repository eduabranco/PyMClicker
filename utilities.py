import keyboard
class ClickerStopper():
    def __init__(self, stopper_key):
        self.stopper_key = stopper_key
        while True:
            if keyboard.is_pressed(self.stopper_key):
                if self.stopper_key.isclicking:
                    self.stopper_key.isclicking = False
                    print("Clicking stopped.")
                else:
                    print("Clicking is not in progress.")