import pygame

class Object:
    def __init__(self, x=0, y=0, xSpeed=0, ySpeed=0, image=None, imageWidth=None, imageHeight=None) -> None:
        self.x = x
        self.y = y
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.image = image
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight

    def update(self):
        pass