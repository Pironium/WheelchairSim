import random

class WheelchairSimulator2:
    def __init__(self):
        self.player_position = (0, 0)
        self.obstacles = [(1, 1), (2, 2), (3, 3)]
        self.score = 0

    def move_player(self, direction):
        if direction == 'up':
            self.player_position = (self.player_position[0], self.player_position[1] + 1)
        elif direction == 'down':
            self.player_position = (self.player_position[0], self.player_position[1] - 1)
        elif direction == 'left':
            self.player_position = (self.player_position[0] - 1, self.player_position[1])
        elif direction == 'right':
            self.player_position = (self.player_position[0] + 1, self.player_position[1])
        
        if self.player_position in self.obstacles:
            self.score -= 1
            return "You hit an obstacle!"
        else:
            self.score += 1
            return "Move successful!"

    def generate_obstacles(self):
        new_obstacle = (random.randint(0, 10), random.randint(0, 10))
        self.obstacles.append(new_obstacle)

if __name__ == "__main__":
    game = WheelchairSimulator2()
    while True:
        print("Player position:", game.player_position)
        print("Score:", game.score)
        print("Enter a direction (up/down/left/right):")
        direction = input()
        result = game.move_player(direction)
        print(result)
        game.generate_obstacles()
