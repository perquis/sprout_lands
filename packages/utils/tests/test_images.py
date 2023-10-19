from packages.enums.Direction import Direction
from packages.utils.images import find_images_by_direction as fibd


def tests_getting_sprites():
    names = ["Basic", "Charakter", "Spritesheet"]
    directory = " ".join(names)
    filename = "_".join(names)
    root = "/".join([directory, filename])

    result = len(fibd(root, direction=Direction.UP))

    assert result == 2
