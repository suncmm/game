import pygame




def main():
    pygame.init()
    pygame.display.set_caption('Revolution of Godding Human - version1.0')
    win = pygame.display.set_mode((1200, 700))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        '''
        Fill the backgroud with white and draw a solid circle
        win.fill((250,250,250))
        pygame.draw.circle(win, (0, 0, 250), (250, 250), 75)    #(1, 2, 3) is RGB,(x, y) is O and 75 is R
        pygame.display.flip()
        '''
    
    pygame.quit()

main()