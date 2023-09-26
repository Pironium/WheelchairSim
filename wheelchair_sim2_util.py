import random

def generate_obstacles(num_obstacles):
    obstacles = []
    for _ in range(num_obstacles):
        obstacle_type = random.choice(["rock", "tree", "bush"])
        obstacle_position = (random.randint(0, 100), random.randint(0, 100))
        obstacles.append((obstacle_type, obstacle_position))
    return obstacles
