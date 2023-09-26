from pygame import mixer

from packages.models import router


def music(filename: str):
    """
    This function load a music from 
    assets/music.
    """
    mixer.init()
    music = mixer.music

    music.load(f"{router.music}/{filename}")
    music.play()
