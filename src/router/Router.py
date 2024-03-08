import os
from dataclasses import dataclass


class Router:
    def __init__(self):
        self.music: str = f"{self.get_assets_path()}/music"
        self.sprites: str = f"{self.get_assets_path()}/packages/sprites_basic_pack/Characters"
        self.icons: str = f"{self.get_assets_path()}/icons"

    def get_assets_path(start_path):
        for root, dirs, files in os.walk(os.getcwd()):
            if "assets" in dirs:
                return os.path.join(root, "assets")

        return None
