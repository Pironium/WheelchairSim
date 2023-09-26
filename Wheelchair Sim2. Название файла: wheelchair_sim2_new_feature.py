import random
import time

class WheelchairSim2:
    def __init__(self):
        self.energy = 100
        self.distance = 0
        self.obstacles = ["rock", "tree", "stairs", "puddle"]

    def move_forward(self):
        self.distance += random.randint(1, 5)
        self.energy -= random.randint(5, 15)
        print(f"Moved forward by {self.distance} meters.")

    def jump(self):
        if "stairs" in self.obstacles:
            print("Successfully jumped over the stairs!")
            self.obstacles.remove("stairs")
        else:
            print("No stairs to jump over.")

    def recharge_energy(self):
        print("Recharging energy...")
        time.sleep(3)
        self.energy = 100
        print("Energy fully recharged.")

    def encounter_obstacle(self):
        obstacle = random.choice(self.obstacles)
        print(f"Encountered a {obstacle}!")
        if obstacle == "rock":
            self.energy -= random.randint(10, 20)
        elif obstacle == "tree":
            self.energy -= random.randint(15, 25)
        elif obstacle == "stairs":
            self.jump()
        elif obstacle == "puddle":
            print("Slipped on a puddle!")
            self.distance -= random.randint(1, 5)

    def play(self):
        while self.energy > 0 and self.distance < 100:
            action = random.choice(["move_forward", "encounter_obstacle"])
            if action == "move_forward":
                self.move_forward()
            elif action == "encounter_obstacle":
                self.encounter_obstacle()
                if self.energy <= 0:
                    print("Out of energy! Game over.")
                    break
        if self.distance >= 100:
            print("Congratulations! You've completed the level.")

if __name__ == "__main__":
    game = WheelchairSim2()
    game.play()
