import random

class WheelchairSimulator:
    def __init__(self):
        self.position_x = 0
        self.position_y = 0

    def move_forward(self, distance):
        self.position_x += distance

    def move_backward(self, distance):
        self.position_x -= distance

    def turn_left(self, angle):
        self.position_y -= angle

    def turn_right(self, angle):
        self.position_y += angle

    def random_movement(self):
        movement_type = random.choice(["forward", "backward", "left", "right"])
        if movement_type == "forward":
            self.move_forward(random.uniform(0.1, 1.0))
        elif movement_type == "backward":
            self.move_backward(random.uniform(0.1, 1.0))
        elif movement_type == "left":
            self.turn_left(random.uniform(0.1, 30.0))
        elif movement_type == "right":
            self.turn_right(random.uniform(0.1, 30.0))

if __name__ == "__main__":
    simulator = WheelchairSimulator()

    for _ in range(10):
        simulator.random_movement()

    print(f"Final position: X = {simulator.position_x}, Y = {simulator.position_y}")
