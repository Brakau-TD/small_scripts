import math

class PixelDrawTools:
    def __init__(self):
        pass

    def angle_between_points(self, p1, p2):
        d1 = p2[0] - p1[0]
        d2 = p2[1] - p1[1]
        if d1 == 0:
            if d2 == 0:  # same points?
                deg = 0
            else:
                deg = 0 if p1[1] > p2[1] else 180
        elif d2 == 0:
            deg = 90 if p1[0] < p2[0] else 270
        else:
            deg = math.atan(d2 / d1) / pi * 180
            lowering = p1[1] < p2[1]
            if (lowering and deg < 0) or (not lowering and deg > 0):
                deg += 270
            else:
                deg += 90
        return deg