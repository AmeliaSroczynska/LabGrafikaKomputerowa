import sys

from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *


# Ustawienia początkowe okna
def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)        # Przygotowanie ekranu do rysowania

    # Vertex - współrzędne wierzchołka
    # Color - kolor wierzchołka
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)    # Pierwszy wierzchołek - czerwony lewy dolny
    glVertex2f(-50.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)    # Drugi wierzchołek - niebieski górny
    glVertex2f(0.0, 50.0)

    glColor3f(0.0, 1.0, 0.0)    # Trzeci wierzchołek - zielony prawy dolny
    glVertex2f(50.0, 0.0)

    glEnd()

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
    # Zakończenie programu z kodem błędu, jeśli GLFW nie zainicjalizowało się poprawnie.
    if not glfwInit():
        sys.exit(-1)

    # Utworzenie okna o rozmiarze 400x400 pikseli
    window = glfwCreateWindow(400, 400, __file__, None, None)
    # Jeśli okno nie zostało utworzone, zakończenie programu
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
