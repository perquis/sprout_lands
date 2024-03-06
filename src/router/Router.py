import os
from dataclasses import dataclass

from .get_assets_path import get_assets_path

# root levet directory for assets which are necessary.
root: str = get_assets_path(os.getcwd())


@dataclass
class Router:
    music: str = f"{root}/music"
    sprites: str = f"{root}/packages/sprites_basic_pack/Characters"
