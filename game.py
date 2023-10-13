import pygame

from packages import models, resources
from packages.enums import Direction, Gender
from packages.models import Player

# 🔧 SETUP 🔧
pygame.init()

# watch out for the refresh rate
clock = pygame.time.Clock()
# current resolution
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
# this module is responsible for the refresh rate
device = models.Device()

# toggle fullscreen
pygame.display.toggle_fullscreen()
# turn on the music
resources.music("village_vibe.mp3")

# return the current position of the mouse
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
running = True
dt = 0.0

# disable the mouse cursor
pygame.mouse.set_visible(False)

sprites = pygame.sprite.Group()  # type: ignore
player = Player("PerQuis", Gender.MALE)

# add the player to the group
sprites.add(player)
# default speed
speed = 225

current_direction = Direction.DOWN

# 🎮 GAME 🎮
while running:
    for event in pygame.event.get():
        # close the window by clicking the X button
        if event.type == pygame.QUIT:
            running = False

    # get the pressed key
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_s] or keys[pygame.K_DOWN] or keys[pygame.K_a] or keys[
            pygame.K_LEFT] or keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.toggle_move(True)
    else:
        player.toggle_move(False)

    # move the player
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        current_direction = Direction.UP
        player_pos.y -= speed * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        current_direction = Direction.DOWN
        player_pos.y += speed * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        current_direction = Direction.LEFT
        player_pos.x -= speed * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        current_direction = Direction.RIGHT
        player_pos.x += speed * dt

    if keys[pygame.K_ESCAPE]:
        running = False

    screen.fill("black")
    sprites.draw(screen)
    # update the player position and animation speed
    sprites.update(player_pos, 0.25, current_direction)

    pygame.display.update()
    dt = clock.tick(device.get_refresh_rate()) / 1000

pygame.quit()
