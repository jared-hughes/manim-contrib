from superellipse import Superellipse
from manim import *


class SuperellipseScene(Scene):
    def construct(self):
        self.add(Superellipse(5, 2, 2, fill_color=GRAY,
                              fill_opacity=0.5).move_to(3*LEFT))
        side_ellipses = [
            Superellipse(2**(n/2), 2, 2)
            for n in range(-4, 6)
        ]
        self.add(VGroup(*side_ellipses).move_to(3*RIGHT))
