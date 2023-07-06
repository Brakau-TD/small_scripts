import pygame
from pygame import mouse

pygame.init()
from palettecolors import palettecolors

tools = [
    pygame.image.load("eraser.png"),
    pygame.image.load("save2.png"),

]
deselected = [
    pygame.image.load("eraser.png"),
    pygame.image.load("save2.png"),

]
selected =[
    pygame.image.load("eraserselected.png")

]


class DrawCanvas():
    def __init__(self, size: tuple):
        self.size = size
        self.screen = pygame.display.set_mode((size[0], size[1]))
        self.items = []
        # resize the background image to match the screen size of 440,460
        self.bg = pygame.image.load("grayscreen.png").convert()
        self.bg = pygame.transform.scale(self.bg, (size[0], size[1]))
        self.tools = tools
        self.selected = selected
        self.deselected = deselected
        self.make_lowresolution()

    def make_lowresolution(self):
        lr_array = []
        temp = []
        line = []
        for i in range(self.size[1] // 10):
            for y in range(self.size[0] // 10):
                temp.append("")
            line.append(temp)
            temp = []

    def drawcolorpalette(self):
        for i, element in enumerate(palettecolors):
            pygame.draw.rect(self.screen, element, pygame.Rect((i * 20, 0), (20, 20)))

    def drawtools(self):
        for i, element in enumerate(self.tools):
            self.screen.blit(element, (i * 20, 20))

    def drawcanvas(self, items: list):
        self.screen.blit(self.bg, (0, 0))
        # pointer_rect = pygame.Rect(pygame.mouse.get_pos(), (20, 20))
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        BLACK = (0, 0, 0)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        ORANGE = (255, 197, 82)
        colors = []
        color = BLACK
        linestart = []
        lineend = []
        linelist = []
        state = "pixel"
        indices = []
        running = True
        while running == True:
            self.screen.blit(self.bg, (0, 0))
            mousepos = pygame.mouse.get_pos()
            pointer_rect = pygame.Rect(((mousepos[0] // 20 * 20, mousepos[1] // 20 * 20)), (20, 20))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        color = BLUE
                    elif event.key == pygame.K_w:
                        color = WHITE
                    elif event.key == pygame.K_s:
                        color = BLACK
                    elif event.key == pygame.K_r:
                        color = RED
                    elif event.key == pygame.K_g:
                        color = GREEN
                    elif event.key == pygame.K_o:
                        color = ORANGE

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and mousepos[1] < 20:
                        color = palettecolors[mousepos[0] // 20]
                    elif event.button == 1 and 20 <= mousepos[1] <= 40:
                        print("options")
                        if 0 < mousepos[0] < 20 and state != "erase":
                            state = "erase"
                            self.tools[0] = self.selected[0]

                        elif 0 < mousepos[0] < 20 and state == "erase":
                            state = "pixel"
                            self.tools[0] = self.deselected[0]
                    elif event.button == 1 and state == "erase":
                        try:
                            pixelindex = indices.index(((mousepos[0] // 20) * 20, (mousepos[1] // 20) * 20))
                            colors.pop(pixelindex)
                            items.pop(pixelindex)
                            indices.pop(pixelindex)
                        except ValueError as e:
                            print(e)
                    elif event.button == 1 and state == "pixel":
                        items.append(pygame.Rect(((mousepos[0] // 20) * 20, (mousepos[1] // 20) * 20), (20, 20)))
                        colors.append(color)
                        indices.append(((mousepos[0] // 20) * 20, (mousepos[1] // 20) * 20))
                        state = "pixel"
                    elif event.button == 1 and state == "line":
                        lineend = ((mousepos[0] // 20) * 20, (mousepos[1] // 20) * 20)
                        linecolor = color
                        linelist.append([linestart, lineend, color])
                        state = "pixel"


                    elif event.button == 3 and mousepos[1]>40:
                        state = "line"
                        linestart = ((mousepos[0] // 20) * 20, (mousepos[1] // 20) * 20)

            pygame.draw.rect(self.screen, color, pointer_rect)
            # pygame.draw.rect(self.screen,WHITE,(mousepos[0],mousepos[1],50,50))
            for i, element in enumerate(items):
                pygame.draw.rect(self.screen, colors[i], element)

            for i, line in enumerate(linelist):
                pygame.draw.line(self.screen, line[2], line[0], line[1], 20)
            self.drawcolorpalette()
            self.drawtools()

            # Update the display
            pygame.display.flip()

        pygame.quit()


dc = DrawCanvas((440, 460))
dc.drawcanvas([])
