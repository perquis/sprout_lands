import pygame

from packages.enums import Direction, Gender
from packages.main.Game.Settings import Settings
from packages.models import Player


class Game(Settings):
    """🎮 The game. 🎮"""

    def __init__(self) -> None:
        super().__init__()

    def run(self):
        """Run the game."""
        self.toggle_fullscreen()
        self.mouse_visible(False)
        self.load_music("village_vibe.mp3")

        pos = pygame.Vector2(self.screen.get_width() / 2,
                             self.screen.get_height() / 2)

        sprites = pygame.sprite.Group()
        player = Player("PerQuis", Gender.MALE, pos)
        sprites.add(player)

        while self.start:
            if any(self.all_direction_keys):
                player.toggle_move(True)
            else:
                player.toggle_move(False)

            diff = self.speed * self.delta_time

            if any(self.direction_up_keys):
                player.current_direction = Direction.UP
                player.player_pos.y -= diff
            if any(self.direction_down_keys):
                player.current_direction = Direction.DOWN
                player.player_pos.y += diff
            if any(self.direction_left_keys):
                player.current_direction = Direction.LEFT
                player.player_pos.x -= diff
            if any(self.direction_right_keys):
                player.current_direction = Direction.RIGHT
                player.player_pos.x += diff

            self.screen.fill("black")

            # update the player position and animation speed
            sprites.update(player.player_pos, 0.25)
            sprites.draw(self.screen)

            self.update()
            self.handle_events()

        pygame.quit()
