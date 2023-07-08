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
        #self.bg = pygame.image.load("bgscreen.png").convert_alpha()
        self.bg = pygame.image.load("grayscreen.png").convert()
        self.bg = pygame.transform.scale(self.bg, (size[0], size[1]))
        self.tools = tools
        self.selected = selected
        self.deselected = deselected
        self.linelist = []
        self.colors = []
        self.color = (0, 0, 0)
        self.state = "pixel"
        self.pixelsize = 20
        self.pdt = PixelDrawTools(self.pixelsize, self.size, self.screen)
        self.userevents = UserEvents()
        # self.make_lowresolution()

    # def make_lowresolution(self):
    #     lr_array = []
    #     temp = []
    #     line = []
    #     for i in range(self.size[1] // 10):
    #         for y in range(self.size[0] // 10):
    #             temp.append("")
    #         line.append(temp)
    #         temp = []

    def drawcolorpalette(self):
        for i, element in enumerate(palettecolors):
            pygame.draw.rect(self.screen, element,
                             pygame.Rect((i * self.pixelsize, 0), (self.pixelsize, self.pixelsize)))

    def drawtools(self):
        for i, element in enumerate(self.tools):
            self.screen.blit(element, (i * self.pixelsize, self.pixelsize))

    def drawcanvas(self, items: list):
        self.screen.blit(self.bg, (0, 0))
        linestart, lineend, indices = [], [], []
        running = True
        while running == True:
            self.screen.blit(self.bg, (0, 0))
            mousepos = pygame.mouse.get_pos()
            pointer_rect = pygame.Rect(
                ((mousepos[0] // self.pixelsize * self.pixelsize, mousepos[1] // self.pixelsize * self.pixelsize)),
                (self.pixelsize, self.pixelsize))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.KEYDOWN:
                    self.color = self.userevents.keydown_colors(event, self.color)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and mousepos[1] < self.pixelsize:
                        self.color = palettecolors[mousepos[0] // self.pixelsize]
                    elif event.button == 1 and self.pixelsize <= mousepos[1] <= self.pixelsize * 2:
                        print("options")
                        if 0 < mousepos[0] < self.pixelsize and self.state != "erase":
                            self.state = "erase"
                            self.tools[0] = self.selected[0]

                        elif 0 < mousepos[0] < self.pixelsize and self.state == "erase":
                            self.state = "pixel"
                            self.tools[0] = self.deselected[0]
                    elif event.button == 1 and self.state == "erase":
                        try:
                            pixelindex = indices.index(((mousepos[0] // self.pixelsize) * self.pixelsize,
                                                        (mousepos[1] // self.pixelsize) * self.pixelsize))
                            self.colors.pop(pixelindex)
                            items.pop(pixelindex)
                            indices.pop(pixelindex)
                        except ValueError as e:
                            print(e)
                        try:
                            for i in self.linelist:
                                if i[0] == ((mousepos[0] // self.pixelsize) * self.pixelsize,
                                            (mousepos[1] // self.pixelsize) * self.pixelsize):
                                    self.linelist.remove(i)
                        except ValueError as e:
                            print(e)
                    elif event.button == 1 and self.state == "pixel":
                        items.append(pygame.Rect(((mousepos[0] // self.pixelsize) * self.pixelsize,
                                                  (mousepos[1] // self.pixelsize) * self.pixelsize),
                                                 (self.pixelsize, self.pixelsize)))
                        self.colors.append(self.color)
                        indices.append(((mousepos[0] // self.pixelsize) * self.pixelsize,
                                        (mousepos[1] // self.pixelsize) * self.pixelsize))
                        self.state = "pixel"
                    elif event.button == 1 and self.state == "line":
                        lineend = ((mousepos[0] // self.pixelsize) * self.pixelsize,
                                   (mousepos[1] // self.pixelsize) * self.pixelsize)
                        linecolor = self.color
                        self.linelist.append([linestart, lineend, self.color])
                        self.state = "pixel"
                    elif event.button == 3 and mousepos[1] > self.pixelsize * 2:
                        self.state = "line"
                        linestart = ((mousepos[0] // self.pixelsize) * self.pixelsize,
                                     (mousepos[1] // self.pixelsize) * self.pixelsize)

            pygame.draw.rect(self.screen, self.color, pointer_rect)
            self.pdt.draw_pixelated_lines(self.linelist)
            if self.state == "line":
                self.pdt.draw_temporary_line(linestart, mousepos)
            for i, element in enumerate(items):
                pygame.draw.rect(self.screen, self.colors[i], element)

            self.drawcolorpalette()
            self.drawtools()

            # Update the display
            pygame.display.flip()

        pygame.quit()


dc = DrawCanvas((440, 460))
dc.drawcanvas([])
