import pygame

from packages import models, resources
from packages.enums import Direction, Gender
from packages.models import Player


class Game:
    def __init__(self) -> None:
        pygame.init()
        device = models.Device()
        resolution = pygame.display.Info()

        self.start = True
        self.clock = pygame.time.Clock()
        self.display = resolution.current_w, resolution.current_h
        self.screen = pygame.display.set_mode(self.display, pygame.RESIZABLE)
        self.refresh_rate = device.get_refresh_rate()
        self.current_direction = Direction.DOWN
        self.delta_time = 0.0
        self.speed = 225

        self.player_pos = pygame.Vector2(
            self.screen.get_width() / 2, self.screen.get_height() / 2)

    def run(self):
        pygame.mouse.set_visible(False)
        resources.music("village_vibe.mp3")
        self.toggle_fullscreen()

        sprites = pygame.sprite.Group()  # type: ignore

        player = Player("PerQuis", Gender.MALE)
        sprites.add(player)

        while self.start:
            for event in pygame.event.get():
                # close the window by clicking the X button
                if event.type == pygame.QUIT:
                    self.start = False

                if event.type == pygame.KEYUP and event.key == pygame.K_F11:
                    self.toggle_fullscreen()

            # get the pressed key
            keys = pygame.key.get_pressed()

            if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_s] or keys[pygame.K_DOWN] or keys[pygame.K_a] or keys[
                    pygame.K_LEFT] or keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                player.toggle_move(True)
            else:
                player.toggle_move(False)

            # move the player
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.current_direction = Direction.UP
                self.player_pos.y -= self.speed * self.delta_time
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.current_direction = Direction.DOWN
                self.player_pos.y += self.speed * self.delta_time
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.current_direction = Direction.LEFT
                self.player_pos.x -= self.speed * self.delta_time
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.current_direction = Direction.RIGHT
                self.player_pos.x += self.speed * self.delta_time

            if keys[pygame.K_ESCAPE]:
                self.start = False

            self.screen.fill("black")
            sprites.draw(self.screen)
            # update the player position and animation speed
            sprites.update(self.player_pos, 0.25, self.current_direction)

            pygame.display.update()
            self.delta_time = self.clock.tick(self.refresh_rate) / 1000

        pygame.quit()

    def toggle_fullscreen(self):
        """Toggle fullscreen mode."""
        pygame.display.toggle_fullscreen()
