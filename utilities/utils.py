import os

class Utils():
    # Screenshot function
    def take_screenshot(self, name):
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        self.driver.save_screenshot(f"screenshots/{name}.png")