import pygame

class Object:
    # screenWidth = 0
    # screenHeight = 0

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
        self.x += self.xSpeed
        self.y += self.ySpeed
        if self.x <= 0:
            self.x = 0
        elif self.x >= self.screenWidth - self.imageWidth:
            self.x = self.screenWidth - self.imageWidth
        
        if self.y <= 0:
            self.y = 0
        elif self.y >= self.screenHeight - self.imageHeight:
            self.y = self.screenHeight - self.imageHeight