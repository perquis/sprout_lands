import pygame

from packages.enums import Direction, Gender
from packages.main.Game.Settings import Settings
from packages.models import Player


class Game(Settings):
    def __init__(self) -> None:
        super().__init__()

    def run(self):
        self.toggle_fullscreen()
        self.mouse_visible(False)
        self.load_music("village_vibe.mp3")

        sprites = pygame.sprite.Group()  # type: ignore
        player = Player("PerQuis", Gender.MALE)
        sprites.add(player)

        while self.start:
            if any(self.all_direction_keys):
                player.toggle_move(True)
            else:
                player.toggle_move(False)

            if any(self.direction_up_keys):
                self.current_direction = Direction.UP
                self.player_pos.y -= self.speed * self.delta_time
            if any(self.direction_down_keys):
                self.current_direction = Direction.DOWN
                self.player_pos.y += self.speed * self.delta_time
            if any(self.direction_left_keys):
                self.current_direction = Direction.LEFT
                self.player_pos.x -= self.speed * self.delta_time
            if any(self.direction_right_keys):
                self.current_direction = Direction.RIGHT
                self.player_pos.x += self.speed * self.delta_time

            if self.keys[pygame.K_ESCAPE]:
                self.exit()

            self.screen.fill("black")
            sprites.draw(self.screen)
            # update the player position and animation speed
            sprites.update(self.player_pos, 0.25, self.current_direction)

            self.update()
            self.handle_events()

        pygame.quit()
