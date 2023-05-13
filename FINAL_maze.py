from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from cube import Cube
from image_to_array import image_to_array
from texture import Texture
from pygame import mixer
from camera import Camera
from coins import *
from monster import *
from player import *




cam = Camera()
# Size of cubes used to create wall segments.
cubesize = 2
coins_result = 0
map = []




def initGL(Width, Height):
    glClearColor(0.0, 0.1, 0.26, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, float(Width) / float(Height), 0.1, 100)
    glMatrixMode(GL_MODELVIEW)


def check_collisions(cam, coins, monsters):
    global coins_result, life_result

    # check collision with coins
    for coin in coins:
        if coin.collission(cam):
            coins_result += 100
            coins.remove(coin)
           # pygame.mixer.Channel(1).play(pygame.mixer.Sound('sounds/coin.mp3'))

    if (coins_result >= 500 and cam.camera_pos[0] >= 21 and cam.camera_pos[2] >= 15):
        cam.flag = "win"
    elif (coins_result < 500 and cam.camera_pos[0] >= 21 and cam.camera_pos[2] >= 15):
        cam.flag = "End"

    for monster in monsters:
        # check collision with monster
        if monster.collission_1(cam):
            while (coins_result > 0):
                coins_result -= 100
                monsters.remove(monster)
                #pygame.mixer.Channel(1).play(
                #    pygame.mixer.Sound('sounds/hit.ogg'))
                break
            if (coins_result <= 0):
                cam.flag = "End"
                return False
            else:
                return True
    return coins_result


monsters = [Monster(9, 2, 90), Monster(2, 5, 0), Monster(14, 2, 5), Monster(18, 2, 90), Monster(
    18, 16, 5), Monster(20, 18, 90), Monster(15, 18, 90), Monster(10, 18, 90), Monster(6, 16, 5)]
coins = [Coin(1, -0.1, 2), Coin(4, -0.1, 6), Coin(4, -0.1, 2), Coin(10, -0.1, 5), Coin(14, -0.1, 5), Coin(12, -0.1, 6), Coin(18, -0.1, 5), Coin(18, -0.1, 8), Coin(18, -0.1, 10), Coin(18, -
                                                                                                                                                                                       0.1, 12), Coin(18, -0.1, 18), Coin(14, -0.1, 18), Coin(10, -0.1, 16), Coin(10, -0.1, 14), Coin(8, -0.1, 14), Coin(2, -0.1, 18), Coin(2, -0.1, 16), Coin(2, -0.1, 14), Coin(2, -0.1, 12)]


def drawScene():
    global camerapos, cam, coins_result
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    locations = []
    cam.setup_camera()
    cube = Cube()

    for grenad in cam.grenades:

        check = grenad.draw(monsters, cam.grenades)
        if check:
            coins_result -= 50
        if (coins_result <= 0):
            cam.flag = "End"

    check_collisions(cam, coins, monsters)
    # Draw monsters
    for monster in monsters:
        monster.draw()
    # Draw Coins
    for coin in coins:
        coin.draw()
        draw_text_3d_wrapper("Collected coins : " +
                             str(coins_result), -0.9, .8)
    # Draw Player
    player(cam)
# ============================================================================

    # Build the maze like a printer; back to front, left to right.
    row_count = 0
    column_count = 0

    wall_x = 0.0
    wall_z = 0.0

    for i in map:

        wall_z = (row_count * (cubesize * 1))

        for j in i:

            # 1 = cube, 0 = empty space.
            if (j == 1):
                glPushMatrix()
                cube.drawcube(2, 1.0)
                wall_x = (column_count * (cubesize * 1))
                locations.append([wall_x, wall_z])
                glPopMatrix()
            else:
                glPushMatrix()
                glTranslate(0, -1, 0)
                glScale(1, 0.1, 1)
                cube.drawcube(1, -1.0)
                glPopMatrix()
            # Move from left to right one cube size.
            glTranslatef(cubesize, 0.0, 0.0)

            column_count += 1

        # Reset position before starting next row, while moving
        # one cube size towards the camera.
        glTranslatef(((cubesize * column_count) * -1), 0.0, cubesize)

        row_count += 1
        # Reset the column count; this is a new row.
        column_count = 0
        cam.locations = locations

    glutSwapBuffers()


# ============================================================================





#################################################################################

def draw_win_or_lose():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    if cam.flag == "play":
        drawScene()

    elif cam.flag == "End":
        glMatrixMode(GL_MODELVIEW)
        gluLookAt(0, 0, 0,
                  0, 0, -1,
                  0, 1, 0)

        glTranslate(0, 0, -2)
        glBindTexture(GL_TEXTURE_2D, 20)
        glBegin(GL_POLYGON)
        glTexCoord2f(0, 0)
        glVertex2d(-2, -2)
        glTexCoord2f(1, 0)
        glVertex2d(2, -2)
        glTexCoord2f(1, 1)
        glVertex2d(2, 2)
        glTexCoord2f(0, 1)
        glVertex2d(-2, 2)
        glEnd()
        glutSwapBuffers()

    elif cam.flag == "win":
        glMatrixMode(GL_MODELVIEW)
        gluLookAt(0, 0, 0,
                  0, 0, -1,
                  0, 1, 0)

        glTranslate(0, 0, -2)
        glBindTexture(GL_TEXTURE_2D, 19)
        glBegin(GL_POLYGON)
        glTexCoord2f(0, 0)
        glVertex2d(-2, -2)
        glTexCoord2f(1, 0)
        glVertex2d(2, -2)
        glTexCoord2f(1, 1)
        glVertex2d(2, 2)
        glTexCoord2f(0, 1)
        glVertex2d(-2, 2)
        glEnd()
        glutSwapBuffers()


    elif cam.flag == "start":
        glMatrixMode(GL_MODELVIEW)
        gluLookAt(0, 0, 0,
                  0, 0, -1,
                  0, 1, 0)

        glTranslate(0, 0, -2)
        glBindTexture(GL_TEXTURE_2D, 21)
        glBegin(GL_POLYGON)
        glTexCoord2f(0, 0)
        glVertex2d(-2, -2)
        glTexCoord2f(1, 0)
        glVertex2d(2, -2)
        glTexCoord2f(1, 1)
        glVertex2d(2, 2)
        glTexCoord2f(0, 1)
        glVertex2d(-2, 2)
        glEnd()

        glutSwapBuffers()


def main():

    global map, cam
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(0, 0)

    window = glutCreateWindow('Experimental Maze')
    # Generate map.
    generator = image_to_array()
    map = generator.generateMap("textures/maze_12.png")
    #glutDisplayFunc(draw)
    glutDisplayFunc(draw_win_or_lose)
    glutIdleFunc(draw_win_or_lose)
    Texture().load_textures()
    initGL(15, 15)
    glutPassiveMotionFunc(cam.mouse_look_clb)
    glutKeyboardFunc(cam.keyboard)
    glutKeyboardUpFunc(cam.throw)
    glutSetCursor(GLUT_CURSOR_NONE)
    glutMouseFunc(cam.activeMouse)
    mixer.init()
    mixer.music.set_volume(0.2)
    mixer.music.load('sounds/background2.ogg')
    mixer.music.play(-1)
    glutMainLoop()


if __name__ == "__main__":

    main()
