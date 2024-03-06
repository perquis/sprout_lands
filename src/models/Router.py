from dataclasses import dataclass

# root levet directory for assets which are necessary.
root: str = "src/assets"


@dataclass
class Router:
    music: str = f"{root}/music"
    characters: str = f"{root}/sprites_basic_pack/Characters"
