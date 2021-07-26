from manim import *

#####################################
# Mobject created by LED Me Explain #
#####################################
# https://www.tiktok.com/@ledmeexplain
# https://github.com/LedMeExplain
# https://twitter.com/LEDMeExplain
# https://www.youtube.com/channel/UCD_uHRFNcycLyFDtHSOgMOA
# https://www.facebook.com/ledmeexplain
# https://www.instagram.com/ledmeexplain/


class PascalTriangle(VGroup):
    def __init__(
        self,
        rows=6,
        colors=['#236B8E', '#83C167', '#FFFF00', '#FC6255'],
        height=None,
        width=None
    ):

        super().__init__()

        if rows < 1:
            self.rows = 1
        else:
            self.rows = rows
            # Creates a list of rows-elements using the given colors
            self.colors = color_gradient(colors, rows)

        # Each element of the triangle is created using a regular hexagon rotated PI/2
        for n in range(self.rows):
            for k in range(n+1):
                hex = RegularPolygon(n=6, color=self.colors[n], fill_opacity=0.7,
                                     stroke_width=DEFAULT_STROKE_WIDTH*7/(self.rows+1))
                hex.rotate(PI/2).shift(DOWN*n*(1+np.sin(PI/6)) +
                                       RIGHT*(n-k*2)*np.cos(PI/6))
                num = self.coeff(n, k)
                lbl = Text(str(num)).rescale_to_fit(
                    max(hex.width, hex.height)*0.4, [0, 1]).move_to(hex)
                self.add(VGroup(hex, lbl))

        # If width and height are both None the PascalTriangle is scaled to fit in the screen
        if width is not None:
            self.width = width
        elif height is not None:
            self.height = height
        else:
            if config['frame_width'] > config['frame_height']:
                self.height = config['frame_height']*0.9
            else:
                self.width = config['frame_width']*0.9

        # Moves the whole VGroup to the ORIGIN
        self.move_to(ORIGIN)

    def coeff(self, n, k):
        # Pascal Triangle n,k coefficient: nCk
        return int(np.math.factorial(n)/np.math.factorial(k)/np.math.factorial(n-k))
