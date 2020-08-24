import pygame, sys

#general setup
pygame.init()
screen = pygame.display.set_mode((200, 100))
clock = pygame.time.Clock()

#fonts
font = pygame.font.Font(None, 54)
font_color = pygame.Color('springgreen')

#time
passed_time = 0
timer_started = False

while True:
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                timer_started = not timer_started
                if timer_started:
                    start_time = pygame.time.get_ticks()

    #more time
    if timer_started:
        passed_time = pygame.time.get_ticks() - start_time

    #visuals        
    screen.fill((30, 30, 30))
    text = font.render(str(passed_time/1000), True, font_color)
    screen.blit(text, (50, 25))
    
    #updating the window
    pygame.display.flip()
    clock.tick(30)
