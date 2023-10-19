from pygame import image

from packages.models.Router import Router

router = Router()


def character(filename: str):
    """
    This function load an image from
    assets/sprites_basic_pack/Characters
    and return image as rectangle model.
    """
    char_img = image.load(f"{router.characters}/{filename}")
    return char_img
