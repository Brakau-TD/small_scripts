import pygame


class PixelDrawTools:
    def __init__(self, pixel_size: int, screen_size: tuple, screen: pygame.Surface):
        self.pixelsize = pixel_size
        self.screensize = screen_size
        self.screen = screen

        pass

    def draw_pixelated_lines(self, lineslist: list):
        lp = None
        for line in lineslist:
            (x1, y1), (x2, y2), color = line
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            sx = -1 if x1 > x2 else 1
            sy = -1 if y1 > y2 else 1
            err = dx - dy
            line_pixels = []  # Store the pixels of the line

            while x1 != x2 or y1 != y2:
                line_pixels.append(((x1//self.pixelsize)*self.pixelsize, (y1//self.pixelsize)*self.pixelsize))
                e2 = 2 * err
                if e2 > -dy:
                    err -= dy
                    x1 += sx
                if e2 < dx:
                    err += dx
                    y1 += sy
            line_pixels.append((x2, y2))
            line_pixels = list(set(line_pixels))
            lp = self.remove_stacked_pixels(line_pixels.copy())
            for pixel in lp:
                pygame.draw.rect(self.screen, color, ((pixel[0]//self.pixelsize)*self.pixelsize,
                                                      (pixel[1]//self.pixelsize)*self.pixelsize,
                                                      self.pixelsize,
                                                      self.pixelsize))
        print(list(set(lp)))


    def remove_stacked_pixels(self, line_pixels: list):
        for i,pixel in enumerate(line_pixels):
            if i == 0:
                continue
            if pixel[0] == line_pixels[i-1][0] or pixel[1] == line_pixels[i-1][1]:
                line_pixels.pop(i-1)
        return line_pixels


        # for line in lineslist:
        #     start_pos, end_pos = line[0], line[1]
        #     color = line[2]
        #     x1, y1 = start_pos
        #     x2, y2 = end_pos
        #
        #     dx = abs(x2 - x1)
        #     dy = abs(y2 - y1)
        #     sx = 1 if x1 < x2 else -1
        #     sy = 1 if y1 < y2 else -1
        #
        #     err = dx - dy
        #
        #     while x1 != x2 or y1 != y2:
        #         pygame.draw.rect(self.screen, color, ((x1//self.pixelsize)*self.pixelsize,
        #                                               (y1//self.pixelsize)*self.pixelsize,
        #                                               self.pixelsize,
        #                                               self.pixelsize))
        #         e2 = 2 * err
        #         if e2 > -dy:
        #             err -= dy
        #             x1 += sx
        #         if e2 < dx:
        #             err += dx
        #             y1 += sy

    def draw_temporary_line(self, linestart, lineend):
        start_pos, end_pos = linestart, lineend
        color = (211, 211, 211)
        x1, y1 = start_pos
        x2, y2 = end_pos

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1

        err = dx - dy

        while x1 != x2 or y1 != y2:
            pygame.draw.rect(self.screen, color, ((x1 // self.pixelsize) * self.pixelsize,
                                                  (y1 // self.pixelsize) * self.pixelsize,
                                                  self.pixelsize,
                                                  self.pixelsize))
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy
