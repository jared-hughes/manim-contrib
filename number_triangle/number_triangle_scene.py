from manim import *
from number_triangle import PascalTriangle, NumberTriangle
# from numpy import np


class PascalScene(Scene):
    def construct(self):
        self.add(PascalTriangle(10))


class NumberScene(Scene):
    def construct(self):
        self.add(NumberTriangle(lambda n, k: str((n+k) % 4), 10))
