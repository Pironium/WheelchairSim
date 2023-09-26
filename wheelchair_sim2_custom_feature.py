# Wheelchair Sim2 - Custom Feature

class WheelchairSim2:
    def __init__(self):
        self.game_state = "start"

    def custom_feature(self):
        if self.game_state == "start":
            print("You have activated the custom feature in Wheelchair Sim2.")
            print("This feature allows you to teleport to a random location.")
            self.game_state = "custom_feature_active"
        elif self.game_state == "custom_feature_active":
            print("You are already using the custom feature.")
        else:
            print("You cannot use the custom feature in your current game state.")

# Usage example:
if __name__ == "__main__":
    game = WheelchairSim2()
    game.custom_feature()
