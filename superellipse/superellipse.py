from manim import *
import numpy as np


class Superellipse(VMobject):
    """ Superellipse, aka Lamé curve, an ellipse generalization.

    n=2 is a circle
    n>2 looks like a rounded rectangle
    n=4 is a squircle
    """

    def __init__(self, n=5, a=1, b=None, num=30, **kwargs):
        self.exponent = 2 / n
        self.a = a
        self.b = b
        self.num = num
        super().__init__(**kwargs)

    def generate_points(self):
        """Uses the parametric formula given in https://en.wikipedia.org/wiki/Superellipse"""
        t = np.linspace(0, np.pi / 2, self.num, endpoint=False)
        x = self.a * np.cos(t) ** self.exponent
        y = self.b * np.sin(t) ** self.exponent
        # stacks coordinates in a careful clockwise order
        vertices = np.stack(
            [
                np.concatenate([x, -x[::-1], -x, x[::-1]]),
                np.concatenate([y, y[::-1], -y, -y[::-1]]),
                np.zeros(4 * self.num),
            ],
            axis=-1,
        )
        # set_points_smoothly had some weird artifacts
        self.set_points_as_corners(vertices)
