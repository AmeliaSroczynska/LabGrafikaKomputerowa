import sys
import time

from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

random.seed(time.time())

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def rectangle(x: float, y: float, a: float, b: float, d=0.0):
    glColor3f(random.random(), random.random(), random.random())
    glBegin(GL_TRIANGLES)
    glVertex2f((x - (d * a) / 2), (y + (d * b) / 2))
    glVertex2f((x + (d * a) / 2), (y + (d * b) / 2))
    glVertex2f((x + (d * a) / 2), (y - (d * b) / 2))
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f((x - (d * a) / 2), (y + (d * b) / 2))
    glVertex2f((x - (d * a) / 2), (y - (d * b) / 2))
    glVertex2f((x + (d * a) / 2), (y - (d * b) / 2))
    glEnd()


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    rectangle(0.0, 0.0, 100.0, 50.0, 0.5)

    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio, 1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0, 1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)

    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
