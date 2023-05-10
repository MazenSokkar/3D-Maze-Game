from pyrr import Vector3, vector, vector3
from math import sin, cos, radians
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

class Grenades:
    def __init__(self, cam):
        self.cam = cam
        self.x = self.cam.camera_pos[0]
        self.y = -0.5
        self.z = self.cam.camera_pos[2]
        self.direction = self.cam.throw_direction
        self.pos = Vector3([self.x,self.y,self.z])
    def draw(self):
        glPushMatrix()
        glTranslate(self.pos[0] + self.direction[0] * 0.4, -0.5, self.pos[2] + self.direction[2] * 0.4)
        glutSolidCube(0.1)
        self.pos += self.direction * 0.05
        glPopMatrix()
