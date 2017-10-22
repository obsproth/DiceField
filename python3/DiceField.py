from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

COLOR = [None, (1, 1, 1), (1, 1, 0), (0, 0, 1), (0.5, 0.5, 1), (0, 1, 0), (1, 0, 1)]

class DiceField:
    def __init__(self, window_size, world_size):
        self.world = World(world_size)
        self.window_size = window_size
        self.rotate = 0

    def start(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(*self.window_size)
        glutInitWindowPosition(100, 100)
        glutCreateWindow('DiceField')
        glutDisplayFunc(self._glut_display)
        glutReshapeFunc(self._glut_reshape)
        glutIdleFunc(self.idle)
        #
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(self.window_size[0])/float(self.window_size[1]), 0.1, 100.0)
        #
        glutMainLoop()

    def idle(self):
        self.rotate += 1
        self.rotate %= 360
        glutPostRedisplay()

    def _glut_display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(3.0, 2.0, 4.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glRotatef(self.rotate, 0.0, 1.0, 0.0)
        self.world.render()
        glutSwapBuffers()
    
    def _glut_reshape(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)


class World:
    def __init__(self, size):
        self.size = size
        self.world = [[None] * size[1] for i in range(size[0])]
    def put(self, pos, dice):
        self.world[pos[0]][pos[1]] = dice
    def render(self):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                dice = self.world[x][y]
                if dice:
                    dice.render(x, y)


class Dice:
    def __init__(self):
        pass
    def render(self, x, y):
        glBegin(GL_QUADS)
        # top
        glColor3f(*COLOR[1])
        glVertex3f(1.0, 1.0, -1.0)   # A
        glVertex3f(-1.0, 1.0, -1.0)  # B
        glVertex3f(-1.0, 1.0, 1.0)   # C
        glVertex3f(1.0, 1.0, 1.0)    # D
        # bottom
        glColor3f(*COLOR[6])
        glVertex3f(1.0, -1.0, -1.0)  # E
        glVertex3f(-1.0, -1.0, -1.0) # F
        glVertex3f(-1.0, -1.0, 1.0)  # G
        glVertex3f(1.0, -1.0, 1.0)   # H
        # front
        glColor3f(*COLOR[2])
        glVertex3f(1.0, 1.0, 1.0)    # D
        glVertex3f(-1.0, 1.0, 1.0)   # C
        glVertex3f(-1.0, -1.0, 1.0)  # G
        glVertex3f(1.0, -1.0, 1.0)   # H
        # back
        glColor3f(*COLOR[5])
        glVertex3f(1.0, 1.0, -1.0)   # A
        glVertex3f(-1.0, 1.0, -1.0)  # B
        glVertex3f(-1.0, -1.0, -1.0) # F
        glVertex3f(1.0, -1.0, -1.0)  # E
        # right
        glColor3f(*COLOR[3])
        glVertex3f(1.0, 1.0, 1.0)    # D
        glVertex3f(1.0, 1.0, -1.0)   # A
        glVertex3f(1.0, -1.0, -1.0)  # E
        glVertex3f(1.0, -1.0, 1.0)   # H
        # left
        glColor3f(*COLOR[4])
        glVertex3f(-1.0, 1.0, 1.0)   # C
        glVertex3f(-1.0, 1.0, -1.0)  # B
        glVertex3f(-1.0, -1.0, -1.0) # F
        glVertex3f(-1.0, -1.0, 1.0)  # G
        glEnd()

def main():
    df = DiceField((300, 300), (3, 5))
    df.world.put((0, 0), Dice())
    df.start()

if __name__ == '__main__':
    main()

