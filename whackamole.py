import pygame
import random




def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x_sub = 0
        y_sub = 0

        def draw_grid():
            for row in range(1, 640):
                pygame.draw.line(
                    screen,
                    "black",
                    (0, row * 32),
                    (640, row * 32),
                    1

                )

            for col in range(1,512):
                pygame.draw.line(
                    screen,
                    "black",
                    (col * 32, 0),
                    (col*32, 512),
                    1

                )
        # def mark_square(board,row,col,mole):
        #     board = screen

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = x//32
                    col = y//32
                    position = (row,col)
                    if position == (x_sub,y_sub):
                        x_sub = random.randrange(0,20)
                        y_sub = random.randrange(0, 16)


            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(x_sub*32, y_sub*32)))
            draw_grid()
            pygame.display.flip()
            clock.tick(60)







    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
