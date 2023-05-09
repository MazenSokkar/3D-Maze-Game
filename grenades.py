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
        self.front = self.cam.camera_front
        self.pos = Vector3([self.x,self.y,self.z])
    def draw(self):
        glPushMatrix()
        glTranslate(self.pos.x, -0.5, self.pos.z)
        glutSolidCube(0.1)
        self.pos += self.front * 0.05
        glPopMatrix()
