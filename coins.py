from OpenGL.GL import *
from math import *
import pygame

class Coin:
    def __init__(self,x,y,z):
        self.theta = 0
        self.x = x
        self.y = y
        self.z = z
    def draw_circle(self):

        # top circle
        glBegin(GL_POLYGON)
        resolution = 36
        r = 1.7
        for ang in range(0, 360, int(360 / resolution)):  # parametric form of a circle (r*cos(theta),r*sin(theta))
            x = r * cos(ang * pi / 180)  # pi / 180 from angle to rad
            y = r * sin(ang * pi / 180)
            glTexCoord2f((x / r + 1) / 2, (y / r + 1) / 2)
            glVertex3f(x, y, 0)
        glEnd()

        # bottom circle
        glBegin(GL_POLYGON)
        resolution = 36
        for ang in range(0, 360, int(360 / resolution)):  # parametric form of a circle (r*cos(theta),r*sin(theta))
            x = r * cos(ang * pi / 180)  # pi / 180 from angle to rad
            y = r * sin(ang * pi / 180)
            glTexCoord2f((x / r + 1) / 2, (y / r + 1) / 2)
            glVertex3f(x, y, -0.2)
        glEnd()

    ################################
    # sides
    def draw_sides(self):
        resolution = 36
        r = 1.7
        glBegin(GL_QUAD_STRIP)
        for ang in range(0, 360, int(360 / resolution)):
            x = r * cos(ang * pi / 180)
            y = r * sin(ang * pi / 180)
            z = 0
            glTexCoord2f(float(ang) / 360, 1)
            glVertex3f(x, y, z)
            glTexCoord2f(float(ang) / 360, 0)
            glVertex3f(x, y, z - 0.2)
        # connect last point to first point
        glTexCoord2f((x / r + 1) / 2, (y / r + 1) / 2)
        glVertex3f(r, 0, 0)
        glTexCoord2f((x / r + 1) / 2, ((y - 0.2) / r + 1) / 2)
        glVertex3f(r, 0, -0.2)
        glEnd()

    def set_coin(self):
        glPushMatrix()
        glTranslate(self.x, self.y, self.z)  ##set coins
        glRotate(self.theta, 0, 1, 0)
        glScale(0.1, 0.1, 0.1)
        self.draw_circle()
        self.draw_sides()
        glPopMatrix()
        self.theta += 0.4

    def draw(self):
        glBindTexture(GL_TEXTURE_2D, 3)
        self.set_coin()
    def collission(self, cam):
        if cam.camera_pos[0] + 0.2 > self.x and cam.camera_pos[0] - 0.2 < self.x:
            if cam.camera_pos[2] + 0.2 > self.z and cam.camera_pos[2] - 0.2 < self.z:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('sounds/coin.mp3'))
                return True