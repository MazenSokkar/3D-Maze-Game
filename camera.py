from pyrr import Vector3, vector, vector3
from math import sin, cos, radians
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from grenades import *

class Camera:
    def __init__(self, width = 900, height = 800):
        self.locations = []
        self.camera_pos = Vector3([0.0, 0.0, 2.0])
        self.camera_front = Vector3([1.0, 0.0, 0.0])
        self.camera_right = Vector3([1.0, 0.0, 0.0])
        self.throw_direction = self.camera_front
        self.mouse_sensitivity = 0.45
        self.jaw = 0
        self.head_jaw = 0
        self.pitch = 0
        self.throw_avillable = True
        self.WIDTH, self.HEIGHT = width, height
        self.lastX, self.lastY = 0, 0
        self.look_up = False
        self.last_pos = self.jaw
        self.angle = 90
        self.head_angle = 0
        self.step = 0.0
        self.forward = False
        self.mouseAvaillabe = False
        self.flag = "start"
        self.grenades = []
    def process_mouse_movement(self, xoffset, yoffset, constrain_pitch=True):
        if constrain_pitch:
            if self.pitch > 80:
                self.pitch = 80
            if self.pitch < -30:
                self.pitch = -30
        self.jaw += xoffset
        self.pitch -= yoffset


        front = Vector3([0.0, 0.0, 0.0])
        front.x = cos(radians(self.jaw)) * cos(radians(self.pitch))
        front.y = sin(radians(self.pitch))
        front.z = sin(radians(self.jaw)) * cos(radians(self.pitch))

        self.camera_front = front
        self.camera_right = vector3.cross(self.camera_front, Vector3([0.0, 1.0, 0.0]))


    # Camera method for the WASD movement
    def collission(self,new_pos):
        location = [new_pos[0], new_pos[2]]
        for X in self.locations:
            if X[0] - 1.15 < location[0] and X[0] + 1.15 > location[0]:
                if X[1] - 1.15 < location[1] and X[1] + 1.15 > location[1]:
                    return True
        return False

    def process_keyboard(self, direction, velocity):
        if direction == "FORWARD":
            new_pos = self.camera_pos + self.camera_front * velocity
            self.step = self.step + (0.1 if self.forward else -.1)

            if not self.collission(new_pos):
                self.camera_pos += self.camera_front * velocity
            self.angle = - self.jaw + 90
            self.throw_direction = self.camera_front
        if direction == "BACKWARD":
            new_pos = self.camera_pos - self.camera_front * velocity
            self.step = self.step + (0.1 if self.forward else -.1)

            if not self.collission(new_pos):
                self.camera_pos -= self.camera_front * velocity
            self.angle = -self.jaw - 90
            self.throw_direction = -self.camera_front
        if direction == "LEFT":
            new_pos = self.camera_pos - self.camera_right * velocity
            self.step = self.step + (0.1 if self.forward else -.1)

            if not self.collission(new_pos):
                self.camera_pos -= self.camera_right * velocity
            self.angle = -self.jaw + 180
            self.throw_direction = -self.camera_right
        if direction == "RIGHT":
            new_pos = self.camera_pos + self.camera_right * velocity
            self.step = self.step + (0.1 if self.forward else -.1)

            if not self.collission(new_pos):
                self.camera_pos += self.camera_right * velocity
            self.angle = -self.jaw + 180 + 180
            self.throw_direction = self.camera_right

        if self.step >= 0.7:
            self.forward = False
        if self.step <= -0.7:
            self.forward = True

    def fix_cursor_out(self):
        self.lastX = int(self.WIDTH / 2)
        self.lastY = int(self.HEIGHT / 2)
        glutWarpPointer(self.lastX, self.lastY)

    def mouse_look_clb(self, xpos, ypos):
        if self.mouseAvaillabe == False:
            if self.lastX == 0 and self.lastY == 0:
                self.lastX = int(self.WIDTH / 2)
                self.lastY = int(self.HEIGHT / 2)
                glutWarpPointer(self.lastX, self.lastY)

            xoffset = xpos - self.lastX
            yoffset = self.lastY - ypos

            self.lastX = xpos
            self.lastY = ypos
            self.process_mouse_movement(xoffset, yoffset)
            self.fix_cursor_out()
    def throw(self, key, x, y):
        if key == b' ':
            self.throw_avillable = True
    def keyboard(self, key, x, y):
        global grenades
        if key == b'w':
            self.process_keyboard("FORWARD", 0.1)
        if key == b'd':
            self.process_keyboard("RIGHT", 0.1)
        if key == b'a':
            self.process_keyboard("LEFT", 0.1)
        if key == b's':
            self.process_keyboard("BACKWARD", 0.1)
        if key == b'h':
            self.look_up = not self.look_up
        if key == b' ':
            if self.throw_avillable == True:
                self.grenades.append(Grenades(self))
                self.throw_avillable = False
        if key ==b'p':
            self.flag ="play"
        if key == b'q':
            os._exit(0)
        if key == b'\x1b':
            glutSetCursor(GLUT_CURSOR_LEFT_ARROW)
            self.mouseAvaillabe = True

        print(key)

    def setup_camera(self):
        if self.look_up == True:
            gluLookAt(1, 10, 1,
                      6, 0, 6,
                      0, 1, 0)
        else:
            gluLookAt(self.camera_pos[0] - self.camera_front[0], self.camera_front[1], self.camera_pos[2] - self.camera_front[2],
                      self.camera_pos[0] -.03, -0.2,self.camera_pos[2] -.03,
                      0, 1, 0)
    def activeMouse(self,button, state, x, y):
        glutSetCursor(GLUT_CURSOR_NONE)
        self.lastX = int(self.WIDTH / 2)
        self.lastY = int(self.HEIGHT / 2)
        glutWarpPointer(self.lastX, self.lastY)
        self.mouseAvaillabe = False