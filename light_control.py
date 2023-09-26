# light_control.py

import time

class LightController:
    def __init__(self):
        self.light_intensity = 0

    def increase_intensity(self, increment):
        self.light_intensity += increment

    def decrease_intensity(self, decrement):
        self.light_intensity -= decrement

    def set_intensity(self, intensity):
        self.light_intensity = intensity

    def simulate_day_night_cycle(self):
        while True:
            for _ in range(24):
                for _ in range(60):
                    for _ in range(60):
                        # Simulate daylight by gradually increasing light intensity
                        for i in range(10):
                            self.increase_intensity(10)
                            time.sleep(1)
                        # Simulate night by gradually decreasing light intensity
                        for i in range(10):
                            self.decrease_intensity(10)
                            time.sleep(1)

if __name__ == "__main__":
    controller = LightController()
    controller.simulate_day_night_cycle()
