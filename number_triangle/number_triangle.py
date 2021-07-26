from manim import *


class PascalTriangle(VGroup):
    """ By LED Me Explain#0137 """

    def __init__(self, rows=10, colors=['#236B8E', '#83C167', '#FFFF00', '#FC6255'], height=None, width=None, **kwargs):
        VGroup.__init__(self, **kwargs)
        color_array = color_gradient(colors, rows)
        for n in range(rows):
            for k in range(n+1):
                hex = RegularPolygon(n=6, color=color_array[n], fill_opacity=0.7, stroke_width=DEFAULT_STROKE_WIDTH*6/(
                    rows+1)).rotate(PI/2).shift(DOWN*n*(1+np.sin(PI/6))+RIGHT*(n-k*2)*np.cos(PI/6))
                num = int(np.math.factorial(n) /
                          np.math.factorial(k)/np.math.factorial(n-k))
                lbl = Text(str(num)).rescale_to_fit(
                    max(hex.width, hex.height)*0.4, [0, 1]).move_to(hex)
                self.add(VGroup(hex, lbl))

        if height is not None:
            self.scale_to_fit_height(height)
        elif width is not None:
            self.scale_to_fit_width(width)
        else:
            self.scale_to_fit_height(config['frame_height']*0.9)

        self.move_to(ORIGIN)
