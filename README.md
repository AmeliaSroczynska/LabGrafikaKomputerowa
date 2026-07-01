# Laboratoria z Grafiki Komputerowej

Repozytorium zawiera projekty z przedmiotu *Grafika Komputerowa* realizowane w języku **Python** (PyOpenGL, GLFW, GLM). Kody ilustrują techniki renderowania.

---

## Struktura projektów

### 🔹 Lab 2 - Geometria i obiekty 3D
Generowanie trójwymiarowego modelu jajka na podstawie równań parametrycznych.
* **Zad3.0.py**: Wizualizacja modelu jako chmury punktów (`GL_POINTS`).
* **Zad3.5.py**: Wizualizacja w trybie siatki krawędziowej (wireframe, `GL_LINES`).
* **Zad4.0.py**: Renderowanie powierzchni z kolorowych trójkątów (`GL_TRIANGLES`) z losowymi barwami wierzchołków.

### 🔹 Lab 3 - Fraktale 2D i rekurencja
Wykorzystanie algorytmów rekurencyjnych do rysowania obiektów fraktalnych w 2D.
* **Zad4.5.py**: Dywan Sierpińskiego (rekurencyjny podział kwadratu na bazie `GL_TRIANGLES`).
* **Zad5.0.py**: Trójkąt Sierpińskiego (rekurencyjne wycinanie środków trójkątów równobocznych).

### 🔹 Lab 4 - Wirtualna kamera i interakcja
Obsługa myszy do sterowania widokiem i manipulacji sceną 3D.
* **Lab3.0.py**: Rotacja obiektu testowego (`glRotatef`) lewym przyciskiem myszy (kąty `theta`, `phi`).
* **Lab3.5.py**: Dodanie skalowania sceny (`glScalef`) prawym przyciskiem myszy (przybliżanie/oddalanie).
* **Lab4.0.py**: Implementacja kamery sferycznej – ruch myszy zmienia pozycję obserwatora w `gluLookAt`.

### 🔹 Lab 5 - Fizyczny model oświetlenia
Zastosowanie modeli cieniowania (Gouraud/Phong) oraz definicja właściwości materiałów i źródeł światła.
* **Zad3.0.py**: Scena ze sferą, dwoma kolorowymi źródłami światła i parametrami ich tłumienia (atenuacji).
* **Zad3.5.py**: Interaktywna zmiana składowych światła (*Ambient*, *Diffuse*, *Specular*) za pomocą klawiatury.
* **Zad4.0.py**: Animowane źródło światła krążące wokół obiektu, sterowane ruchem myszy na sferze.

### 🔹 Lab 6 - Teksturowanie powierzchni
Nakładanie obrazów bitowych na geometrię 3D oraz konfiguracja filtrowania.
* **Zad3.0.py**: Ładowanie pliku tekstury przy użyciu biblioteki Pillow i mapowanie go na proste obiekty.
* **Zad3.5.py**: Przełączanie filtrów tekstury (`GL_NEAREST` / `GL_LINEAR`) oraz ukrywanie elementów klawiszem `SPACE`.
* **Zad4.0.py**: Przykłady multiteksturowania lub mieszania tekstury z oświetleniem materiału.
* **Zasoby**: Pliki graficzne `tekstura.tga` i `tekstura2.tga`.

### 🔹 Lab 7 - Nowoczesny potok OpenGL 
Przejście na nowoczesny potok programowalny Core Profile 3.3+.
* **Zad3.0.py**: Renderowanie sześcianu 3D przy użyciu własnych shaderów (GLSL), buforów VBO/VAO oraz biblioteki PyGLM do operacji na macierzach transformacji.

---

## 🛠️ Wymagania i uruchomienie
```bash
pip install numpy glfw PyOpenGL PyOpenGL_accelerate Pillow PyGLM
```
Uruchomienie dowolnego programu sprowadza się do wykonania skryptu w terminalu:
```bash
python Zad3.0.py
```
