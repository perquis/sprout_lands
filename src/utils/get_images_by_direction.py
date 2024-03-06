from src import resources

from ..enums import Direction


def get_images_by_direction(filename: str, direction: Direction, range=range(1, 3)):
    return [
        resources.character(f"{filename}_{direction}_{index}.png")
        for index in range
    ]
