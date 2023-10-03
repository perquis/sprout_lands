from packages import resources, models
import pygame

pygame.init()

clock = pygame.time.Clock()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
device = models.Device()

pygame.display.toggle_fullscreen()
resources.music("village_vibe.mp3")

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
running = True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
    if keys[pygame.K_ESCAPE]:
        running = False

    # Drawing
    screen.fill("black")
    pygame.draw.circle(screen, "red", player_pos, 40)

    pygame.display.update()
    dt = clock.tick(device.get_refresh_rate()) / 1000  # type: ignore

pygame.quit()
