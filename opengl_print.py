from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

class OpenGlPrinter:

    def __init__(self, matrix, max_it = 99, mode='automatic'):
        self.key_flag = 0
        self.matrix = matrix

        mt = self.matrix.matrix
        self.columns = len(mt[0])
        self.rows = len(mt)
        mutliply_factor = 8
        self.width = self.columns * mutliply_factor
        self.height = self.rows * mutliply_factor
        self.it = 0
        self.max_it = max_it
        self.mode = mode

    def display(self):
        glClearColor(0.0,0.0,0.0,0.0)
        glClear(GL_COLOR_BUFFER_BIT)

        blue = (0, 0, 0.8)
        white = (1, 1, 1)
        mt = self.matrix.matrix
        for j in range(self.rows):
            for i in range(self.columns):
                color = white
                c = mt[j][i]
                if c == 'X':
                    color = blue
                glColor3f(*color)
                glBegin(GL_QUADS)
                j = self.rows - j - 1

                glVertex2i(i*self.width//self.columns,j*self.height//self.rows)
                glVertex2i((i+1)*self.width//self.columns,j*self.height//self.rows)
                glVertex2i((i+1)*self.width//self.columns,(j+1)*self.height//self.rows)
                glVertex2i(i*self.width//self.columns,(j+1)*self.height//self.rows)

                glEnd()

        glutSwapBuffers()
        if self.mode == 'automatic':
            glutTimerFunc(100, lambda x: self.forward_matrix(), None)


    def keyboard(self, c,x,y):
        self.forward_matrix()
    
    def forward_matrix(self):
        self.it += 1
        if self.it >= self.max_it:
            glutLeaveMainLoop()
            return
        self.matrix = self.matrix.forwards()
        glutPostRedisplay()

    def main(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

        glutInitWindowPosition(25, 25)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow("Conway Game of Life")

        glutDisplayFunc(self.display)
        glutKeyboardFunc(self.keyboard)

        glMatrixMode(GL_PROJECTION)
        gluOrtho2D(0,self.width-1,0,self.height-1)

        glutMainLoop()

