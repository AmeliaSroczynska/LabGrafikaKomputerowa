import sys

from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def rectangle(x: float, y: float, a: float, b: float):
    glBegin(GL_TRIANGLES)
    glVertex2f((x-a/2), (y+b/2))
    glVertex2f((x+a/2), (y+b/2))
    glVertex2f((x+a/2), (y-b/2))
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f((x-a/2), (y+b/2))
    glVertex2f((x-a/2), (y-b/2))
    glVertex2f((x+a/2), (y-b/2))
    glEnd()

def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    rectangle(0.0, 0.0, 100.0, 50.0)        # punkt(x,y) to środek, a,b to wymiary boków

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
    # Utworzenie okna o rozmiarze 400x400 pikseli
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
