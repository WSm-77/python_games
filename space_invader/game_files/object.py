import pygame

class Object:
    speedFactor = 1

    def __init__(self, x=0, y=0, xSpeed=0, ySpeed=0, image=None, imageWidth=0, imageHeight=0,  \
                 screenWidth=0, screenHeight=0) -> None:
        self.x = x
        self.y = y
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.image = image
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

    def update(self):
        pass