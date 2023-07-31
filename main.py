import pygame
import time

pygame.init()

FONT = pygame.font.SysFont('arial', 13, bold=True)

TILE_WIDTH = 20
TILE_HEIGHT = 20
PIXEL_SIZE = 32


WIDTH: int = TILE_WIDTH*(PIXEL_SIZE+2)
HEIGHT: int = TILE_HEIGHT*PIXEL_SIZE

screen = pygame.display.set_mode([WIDTH, HEIGHT], pygame.SRCALPHA, 32)

running = True

prev_time = time.time()

target_fps = 60

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    # pygame.draw.circle(screen, (255, 255, 255), t.pos, 10, 10)
    # pygame.draw.circle(screen, (255, 255, 255), t.foot_target, 5, 5)

    pygame.display.flip()
    curr_time = time.time()#so now we have time after processing
    diff = curr_time - prev_time#frame took this much time to process and render
    delay = max(1.0/target_fps - diff, 0)#if we finished early, wait the remaining time to desired fps, else wait 0 ms!
    # pygame.display.update()
    # init.gui_manager.update(delay+diff)
    time.sleep(delay)
    fps = 1.0/(delay + diff)#fps is based on total time ("processing" diff time + "wasted" delay time)
    prev_time = curr_time
    pygame.display.set_caption("{0}: {1:.2f}".format("game test", fps))
