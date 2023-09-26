import random
import time

class WheelchairSimulator:
    def __init__(self):
        self.position = [0, 0]
        self.obstacles = [(2, 3), (1, 5), (4, 7), (6, 2)]
        self.score = 0

    def move(self, direction):
        if direction == 'up':
            self.position[1] += 1
        elif direction == 'down':
            self.position[1] -= 1
        elif direction == 'left':
            self.position[0] -= 1
        elif direction == 'right':
            self.position[0] += 1

        self.score += 1

    def check_collision(self):
        for obstacle in self.obstacles:
            if obstacle == tuple(self.position):
                return True
        return False

    def play(self):
        while True:
            print(f"Current position: {self.position}")
            direction = random.choice(['up', 'down', 'left', 'right'])
            self.move(direction)
            if self.check_collision():
                print("Game Over! Collision detected.")
                print(f"Your score: {self.score}")
                break
            time.sleep(0.5)

if __name__ == "__main__":
    simulator = WheelchairSimulator()
    simulator.play()
