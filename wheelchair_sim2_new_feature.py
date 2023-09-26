import random
import time

class WheelchairSim2:
    def __init__(self):
        self.player_position = (0, 0)
        self.obstacles = [(2, 2), (3, 4), (1, 5)]
        self.score = 0

    def move_player(self, direction):
        if direction == "up":
            self.player_position = (self.player_position[0], self.player_position[1] + 1)
        elif direction == "down":
            self.player_position = (self.player_position[0], self.player_position[1] - 1)
        elif direction == "left":
            self.player_position = (self.player_position[0] - 1, self.player_position[1])
        elif direction == "right":
            self.player_position = (self.player_position[0] + 1, self.player_position[1])

    def check_collision(self):
        if self.player_position in self.obstacles:
            return True
        return False

    def play_game(self):
        print("Welcome to Wheelchair Sim2!")
        while True:
            print(f"Your current position is {self.player_position}")
            direction = input("Enter a direction (up/down/left/right): ")
            self.move_player(direction)
            if self.check_collision():
                print("Oops! You hit an obstacle. Game over!")
                break
            else:
                self.score += 1
                print(f"Score: {self.score}")
                time.sleep(1)

if __name__ == "__main__":
    game = WheelchairSim2()
    game.play_game()
