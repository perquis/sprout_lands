from pygame import mixer


def music(filename: str):
    """Load music from the root directory."""
    mixer.init()
    music = mixer.music

    music.load(f"assets/music/{filename}")
    music.play()
