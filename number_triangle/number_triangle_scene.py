from manim import *
from number_triangle import PascalTriangle
# from numpy import np


class PascalScene(Scene):
    def construct(self):
        self.add(PascalTriangle(10))
