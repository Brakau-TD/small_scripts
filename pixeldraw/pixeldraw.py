import pygame
from pygame import mouse

pygame.init()
from palettecolors import palettecolors
from pixeldrawtools import PixelDrawTools
from userevents import UserEvents

tools = [
    pygame.image.load("eraser.png"),
    pygame.image.load("save2.png"),

]
deselected = [
    pygame.image.load("eraser.png"),
    pygame.image.load("save2.png"),

]
selected = [
    pygame.image.load("eraserselected.png")

]


class DrawCanvas():
    def __init__(self, size: tuple):
        self.size = size
        self.screen = pygame.display.set_mode((size[0], size[1]))
        self.items = []
        self.bg = pygame.image.load("grayscreen.png").convert()
        self.bg = pygame.transform.scale(self.bg, (size[0], size[1]))
        self.tools = tools
        self.selected = selected
        self.deselected = deselected
        self.pdt = PixelDrawTools()
        self.userevents = UserEvents()
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
        colors = []
        color = (0,0,0)
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
                    color = self.userevents.keydown_colors(event, color)

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
                    elif event.button == 3 and mousepos[1] > 40:
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
