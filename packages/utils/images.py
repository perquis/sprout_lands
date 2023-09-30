from packages import resources
from packages.enums import Direction


def find_images_by_direction(direction: Direction, range=range(1, 3)):
    filename = "Basic_Charakter_Spritesheet"
    return [
        resources.character(f"{filename}_{direction}_{index}.png")
        for index in range
    ]
