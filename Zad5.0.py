import sys

from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def triangle(x: float, y: float, size: float):
    h = size * (3 ** 0.5) / 2             # wysokość trójkąta

    glBegin(GL_TRIANGLES)
    glVertex2f(x, y + 2 * h / 3)          # wierzchołek górny
    glVertex2f(x - size / 2, y - h / 3)   # lewy dolny
    glVertex2f(x + size / 2, y - h / 3)   # prawy dolny

    glEnd()


def sierpinski(x: float, y: float, size: float, depth: int):
    if depth == 0:
        triangle(x, y, size)
    else:
        new_size = size / 2
        h_new = new_size * (3 ** 0.5) / 2

        sierpinski(x - new_size / 2, y - h_new / 3, new_size, depth - 1)    # lewy dolny trójkąt
        sierpinski(x + new_size / 2, y - h_new / 3, new_size, depth - 1)    # prawy dolny trójkąt
        sierpinski(x, y + 2 * h_new / 3, new_size, depth - 1)               # górny trójkąt
        # skipujemy środkowy trójkąt


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    sierpinski(0.0, 0.0, 300.0, 3)

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
        glOrtho(-200.0, 200.0, -200.0 / aspect_ratio, 200.0 / aspect_ratio, 1.0, -1.0)
    else:
        glOrtho(-200.0 * aspect_ratio, 200.0 * aspect_ratio, -200.0, 200.0, 1.0, -1.0)

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
