import sys
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (222, 178, 0)
PINK = (225, 96, 253)
BLUE = (0, 0, 255)
LIGHTORANGE = (255, 176, 56)
INTERMEDIARYORANGE = (255, 154, 0) 
LIGHTBLUE = (60, 170, 255)
DARKBLUE = (0, 101, 178)
BEIGE = (178, 168, 152)

WIDTH = 950
HEIGHT = 650
SCREEN_SIZE = (WIDTH, HEIGHT)

def text_block(background, message, color, size, coordinate_x, coordinate_y):
    """
    Create block of text.
    """

    font = pygame.font.SysFont(None, size)
    text = font.render(message, True, color)
    background.blit(text, [coordinate_x, coordinate_y])


class Point():
    """
    Class to each point.
    """

    def __init__(self, pos, color):
        self.pos = pos
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.color = color

    def render(self, background):
        """
        Render points on the screen.
        """
    
        pygame.draw.circle(background, self.color, self.pos, 8)


class Algorithm():
    """
    Class to Algorithm Closest Pair of Points.
    """

    def __init__(self):
        self.points = []

    def append_point(self, point):
        """
        Append created point to list of points.
        """
        self.points.append(point)

    def render(self, background):
        """
        Render list of points created.
        """
        for point in self.points:
            point.render(background)


class Game():
    """
    Class to manage the game.
    """

    def __init__(self):
        try:
            pygame.init()
        except:
            print('The pygame module did not start successfully')

        self.start = False
        self.exit = False

    def load(self):
        """
        Load necessary elements.
        """
        self.background = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Closest Pair of Points')

        self.algorithm = Algorithm()

    def initial_game(self):
        """
        Render home screen of program.
        """
        self.background.fill(DARKBLUE)
        pygame.draw.rect(self.background, BEIGE, [60, 60, 820, 520])
        pygame.draw.rect(self.background, LIGHTBLUE, [60, 120, 820, 400])
        pygame.draw.rect(self.background, BLACK, [130, 170, 680, 320])
        pygame.draw.rect(self.background, DARKBLUE, [130, 170, 680, 80])

        text_block(self.background, "CLOSEST PAIR OF POINTS", LIGHTORANGE, 50, 250, 195)
        text_block(self.background, "PRESS (S) TO START", INTERMEDIARYORANGE, 50, 290, 320)
        text_block(self.background, "PRESS (ESC) TO CLOSE", INTERMEDIARYORANGE, 50, 270, 360)

    def render(self):
        """
        Render elements on the screen.
        """
        self.background.fill(BLACK)

        self.algorithm.render(self.background)

        text_block(self.background, "CLICK TO CREATE POINTS", WHITE, 20, 380, 10)
        text_block(self.background, "PRESS (R) TO RETRY", WHITE, 20, 80, 630)
        text_block(self.background, "PRESS (C) TO RUN ALGORITHM", WHITE, 20, 380, 630)
        text_block(self.background, "PRESS (ESC) TO CLOSE", WHITE, 20, 700, 630)

        pygame.display.update()

    def run(self):
        """
        Method with loop to run game.
        """

        self.load()

        while not self.start:

            self.initial_game()

            if pygame.event.get(pygame.QUIT) or pygame.key.get_pressed()[
                    pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit(0)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.start = True
                    self.background.fill(BLACK)

            pygame.display.update()

        while not self.exit:
            if pygame.event.get(pygame.QUIT) or pygame.key.get_pressed()[
                    pygame.K_ESCAPE]:
                self.exit = True
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.start = False
                        self.run()
                    # if event.key == pygame.K_c:
                        # RUN ALGORITHM CLOSEST PAIR OF POINTS
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    point = Point(pos, RED)
                    self.algorithm.append_point(point)
            self.render()

        pygame.quit()
        sys.exit(0)

def main():
    """
    Main method.
    """

    mygame = Game()
    mygame.run()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interruption')
