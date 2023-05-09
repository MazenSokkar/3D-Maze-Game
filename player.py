from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import pygame


def player(cam):
    glPushMatrix()
    glTranslate(cam.camera_pos[0], -0.4, cam.camera_pos[2])
    glRotate(cam.angle, 0, 1, 0)
    glScale(0.1, 0.1, 0.1)

    glBindTexture(GL_TEXTURE_2D, 5)

    glBegin(GL_QUADS)

    # Front Face

    glColor3f(1.0, 1.0, 1.0)  # Red
    glTexCoord2f(0.0, 0.0)

    glVertex3f(-1, 2, 0.5)  # Bottom Left Of The Texture and Quad
    glTexCoord2f(1.0, 0.0)

    glVertex3f(1, 2, 0.5)  # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0)

    glVertex3f(1, 4, 0.5)  # Top Right Of The Texture and Quad
    glTexCoord2f(0.0, 1.0)

    glVertex3f(-1, 4, 0.5)  # Top Left Of The Texture and Quad
    glEnd()

    glBindTexture(GL_TEXTURE_2D, 6)

    glBegin(GL_QUADS)

    # Back Face
    glColor3f(1.0, 1.0, 1.0)  # Green
    glTexCoord2f(0.0, 0.0)

    glVertex3f(-1, 2, -0.5)  # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 0.0)

    glVertex3f(-1, 4, -0.5)  # Top Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0)

    glVertex3f(1, 4, -0.5)  # Top Left Of The Texture and Quad
    glTexCoord2f(0.0, 1.0)

    glVertex3f(1, 2, -0.5)  # Bottom Left Of The Texture and Quad
    glEnd()

    glBegin(GL_QUADS)
    # Top Face
    glColor3f(1.0, 1.0, 1.0)  # Blue

    glVertex3f(-1, 4, -0.5)  # Top Left Of The Texture and Quad
    glVertex3f(-1, 4, 0.5)  # Bottom Left Of The Texture and Quad
    glVertex3f(1, 4, 0.5)  # Bottom Right Of The Texture and Quad
    glVertex3f(1, 4, -0.5)  # Top Right Of The Texture and Quad

    # Bottom Face
    glColor3f(1.0, 1.0, 1.0)  # Yellow
    glVertex3f(-1, 2, -0.5)  # Top Right Of The Texture and Quad
    glVertex3f(1, 2, -0.5)  # Top Left Of The Texture and Quad
    glVertex3f(1, 2, 0.5)  # Bottom Left Of The Texture and Quad
    glVertex3f(-1, 2, 0.5)  # Bottom Right Of The Texture and Quad
    glEnd()
    glBindTexture(GL_TEXTURE_2D, 7)
    glBegin(GL_QUADS)

    # Right face
    glColor3f(1.0, 1.0, 1.0)  # Magenta
    glTexCoord2f(0.0, 0.0)

    glVertex3f(1, 2, -0.5)  # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 0.0)

    glVertex3f(1, 2, 0.5)  # Top Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0)

    glVertex3f(1, 4, 0.5)  # Top Left Of The Texture and Quad
    glTexCoord2f(0.0, 1.0)

    glVertex3f(1, 4, -0.5)  # Bottom Left Of The Texture and Quad
    glEnd()
    glBindTexture(GL_TEXTURE_2D, 8)
    glBegin(GL_QUADS)
    # Left Face
    glColor3f(1.0, 1.0, 1.0)  # Cyan
    glTexCoord2f(0.0, 0.0)

    glVertex3f(-1, 2, -0.5)  # Bottom Left Of The Texture and Quad
    glTexCoord2f(1.0, 0.0)

    glVertex3f(-1, 2, 0.5)  # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0)

    glVertex3f(-1, 4, 0.5)  # Top Right Of The Texture and Quad
    glTexCoord2f(0.0, 1.0)

    glVertex3f(-1, 4, -0.5)  # Top Left Of The Texture and Quad
    glEnd()

    #####################body
    #########################################################
    glBindTexture(GL_TEXTURE_2D, 9)
    glBegin(GL_QUADS)
    # Front body
    glColor3f(1.0, 1.0, 1.0)  # Red
    glTexCoord2f(0.0, 0.0)

    glVertex3f(-2, -2, 0.5)  # Bottom Left Of The Texture and Quad
    glTexCoord2f(1.0, 0.0)

    glVertex3f(2, -2, 0.5)  # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0)

    glVertex3f(2, 2, 0.5)  # Top Right Of The Texture and Quad
    glTexCoord2f(0.0, 1.0)

    glVertex3f(-2, 2, 0.5)  # Top Left Of The Texture and Quad
    glEnd()
    glBindTexture(GL_TEXTURE_2D, 10)
    glBegin(GL_QUADS)
    # Back body
    glColor3f(1.0, 1.0, 1.0)  # Green
    glTexCoord2f(0.0, 0.0)

    glVertex3f(-2, -2, -0.5)  # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 0.0)

    glVertex3f(2, -2, -0.5)  # Top Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0)

    glVertex3f(2, 2, -0.5)  # Top Left Of The Texture and Quad
    glTexCoord2f(0.0, 1.0)

    glVertex3f(-2, 2, -0.5)  # Bottom Left Of The Texture and Quad
    glEnd()

    glBegin(GL_QUADS)
    # Top body
    glColor3f(1.0, 1.0, 1.0)  # Blue
    glVertex3f(-2, 2, -0.5)  # Top Left Of The Texture and Quad
    glVertex3f(-2, 2, 0.5)  # Bottom Left Of The Texture and Quad
    glVertex3f(2, 2, 0.5)  # Bottom Right Of The Texture and Quad
    glVertex3f(2, 2, -0.5)  # Top Right Of The Texture and Quad
    glEnd()

    glBegin(GL_QUADS)
    # Bottom body
    glColor3f(1.0, 1.0, 1.0)  # Yellow
    glVertex3f(-2, -2, -0.5)  # Top Right Of The Texture and Quad
    glVertex3f(2, -2, -0.5)  # Top Left Of The Texture and Quad
    glVertex3f(2, -2, 0.5)  # Bottom Left Of The Texture and Quad
    glVertex3f(-2, -2, 0.5)  # Bottom Right Of The Texture and Quad
    glEnd()

    glBindTexture(GL_TEXTURE_2D, 11)
    glBegin(GL_QUADS)
    # Right body
    glColor3f(1.0, 1.0, 1.0)  # Magenta
    glTexCoord2f(0.0, 0.0)

    glVertex3f(2, -2, 0.5)  # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 0.0)

    glVertex3f(2, -2, -0.5)  # Top Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0)

    glVertex3f(2, 2, -0.5)  # Top Left Of The Texture and Quad
    glTexCoord2f(0.0, 1.0)

    glVertex3f(2, 2, 0.5)  # Bottom Left Of The Texture and Quad
    glEnd()

    glBindTexture(GL_TEXTURE_2D, 12)
    glBegin(GL_QUADS)
    # Left body
    glColor3f(1.0, 1.0, 1.0)  # Cyan
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2, -2, -0.5)  # Bottom Left Of The Texture and Quad
    glTexCoord2f(1.0, 0.0)

    glVertex3f(-2, -2, 0.5)  # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-2, 2, 0.5)  # Top Right Of The Texture and Quad
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2, 2, -0.5)  # Top Left Of The Texture and Quad
    glEnd()

    glBindTexture(GL_TEXTURE_2D, 13)
    glBegin(GL_QUADS)
    ###############right leg
    # Front body
    glColor3f(1.0, 1.0, 1.0)  # Red
    glTexCoord2f(0.0, 0.0)

    glVertex3f(0, -5, 0.5)  # Bottom Left Of The Texture and Quad
    glTexCoord2f(1.0, 0.0)

    glVertex3f(1, -5, 0.5)  # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0)

    glVertex3f(1, -2, 0.5)  # Top Right Of The Texture and Quad
    glTexCoord2f(0.0, 1.0)

    glVertex3f(0, -2, 0.5)  # Top Left Of The Texture and Quad
    glEnd()

    glBindTexture(GL_TEXTURE_2D, 14)
    glBegin(GL_QUADS)
    # Back body
    glColor3f(1.0, 1.0, 1.0)  # Green
    glTexCoord2f(0.0, 0.0)
    glVertex3f(0, -5, -0.5)  # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1, -5, -0.5)  # Top Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1, -2, -0.5)  # Top Left Of The Texture and Quad
    glTexCoord2f(0.0, 1.0)
    glVertex3f(0, -2, -0.5)  # Bottom Left Of The Texture and Quad
    glEnd()

    glBindTexture(GL_TEXTURE_2D, 15)
    glBegin(GL_QUADS)
    # Top leg
    glColor3f(1.0, 1.0, 1.0)  # Cyan

    glVertex(0, -2, 0.5)
    glVertex(1, -2, 0.5)
    glVertex(1, -2, -0.5)
    glVertex(0, -2, -0.5)
    glEnd()
    glBegin(GL_QUADS)
    # button leg
    glVertex(0, -5, 0.5)
    glVertex(1, -5, 0.5)
    glVertex(1, -5, -0.5)
    glVertex(0, -5, -0.5)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, 15)
    glBegin(GL_QUADS)

    # right leg
    glTexCoord2f(0.0, 0.0)

    glVertex(1, -5, 0.5)
    glTexCoord2f(1.0, 0.0)

    glVertex(1, -5, -0.5)
    glTexCoord2f(1.0, 1.0)

    glVertex(1, -2, -0.5)
    glTexCoord2f(0.0, 1.0)

    glVertex(1, -2, 0.5)
    glEnd()
    glBegin(GL_QUADS)

    # left leg
    glTexCoord2f(0.0, 0.0)

    glVertex(0, -5, 0.5)
    glVertex(0, -5, -0.5)
    glVertex(0, -2, -0.5)
    glVertex(0, -2, 0.5)

    glEnd()

    ###################left leg
    # rihgt side
    glBegin(GL_QUADS)
    glVertex(0, -2, 0.5)
    glVertex(0, -2, -0.5)
    glVertex(0, -5, -0.5)
    glVertex(0, -5, 0.5)
    glEnd()
    glBindTexture(GL_TEXTURE_2D, 16)

    # left side
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex(-1, -2, 0.5)
    glTexCoord2f(1.0, 0.0)

    glVertex(-1, -2, -0.5)
    glTexCoord2f(1.0, 1.0)

    glVertex(-1, -5, -0.5)
    glTexCoord2f(0.0, 1.0)

    glVertex(-1, -5, 0.5)
    glEnd()
    glBegin(GL_QUADS)

    # top
    glVertex(-1, -2, 0.5)
    glVertex(-1, -2, -0.5)
    glVertex(0, -2, -0.5)
    glVertex(0, -2, 0.5)
    # button
    glVertex(-1, -5, 0.5)
    glVertex(-1, -5, -0.5)
    glVertex(0, -5, -0.5)
    glVertex(0, -5, 0.5)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, 13)
    glBegin(GL_QUADS)

    # front
    glTexCoord2f(0.0, 0.0)

    glVertex(-1, -2, 0.5)
    glTexCoord2f(1.0, 0.0)

    glVertex(0, -2, 0.5)
    glTexCoord2f(1.0, 1.0)

    glVertex(0, -5, 0.5)
    glTexCoord2f(0.0, 1.0)

    glVertex(-1, -5, 0.5)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, 14)
    glBegin(GL_QUADS)
    # back
    glTexCoord2f(0.0, 0.0)

    glVertex(-1, -2, -0.5)
    glTexCoord2f(1.0, 0.0)

    glVertex(0, -2, -0.5)
    glTexCoord2f(1.0, 1.0)

    glVertex(0, -5, -0.5)
    glTexCoord2f(0.0, 1.0)

    glVertex(-1, -5, -0.5)

    glEnd()

    glPopMatrix()