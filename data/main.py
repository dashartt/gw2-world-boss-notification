import json

def load_world_boss_data():
    with open('data/world_boss.json', 'r') as file:
        world_boss_data = json.load(file)

    return world_boss_data