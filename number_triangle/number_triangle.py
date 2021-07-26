from manim import *
from typing import Callable


class NumberTriangle(VGroup):
    """
    In a triangle, displays the result of a function called as f(n,k) for all 0 ≤ k ≤ n ≤ rows
    """

    def __init__(self, func: Callable[[int, int], str], rows=5,
                 colors=['#236B8E', '#83C167', '#FFFF00', '#FC6255'], height=None, width=None, **kwargs):
        VGroup.__init__(self, **kwargs)
        color_array = color_gradient(colors, rows)
        for n in range(rows):
            for k in range(n+1):
                hex = RegularPolygon(n=6, color=color_array[n], fill_opacity=0.7,
                                     stroke_width=DEFAULT_STROKE_WIDTH*6/(rows+1))
                hex.rotate(PI/2).shift(DOWN*n*(1+np.sin(PI/6)) +
                                       RIGHT*(n-k*2)*np.cos(PI/6))
                label = Text(func(n, k)).rescale_to_fit(
                    max(hex.width, hex.height)*0.4, [0, 1]).move_to(hex)
                self.add(VGroup(hex, label))

        if height is not None:
            self.scale_to_fit_height(height)
        elif width is not None:
            self.scale_to_fit_width(width)
        else:
            self.scale_to_fit_height(config['frame_height']*0.9)

        self.move_to(ORIGIN)


def binom(n, k):
    # Simple implementation through factorials
    return str(int(
        np.math.factorial(n) /
        (np.math.factorial(k) * np.math.factorial(n-k))
    ))


class PascalTriangle(NumberTriangle):
    """
    Displays Pascal's triangle of binomial coefficients (https://oeis.org/A007318).
    Each cell is the sum of the two above it.
    """

    def __init__(self, rows=5, **kwargs):
        NumberTriangle.__init__(self, binom, rows, **kwargs)
