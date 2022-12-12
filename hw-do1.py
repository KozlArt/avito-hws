class Color:
    def __init__(self, r: int, g: int, b: int):
        self.color = (r, g, b)

    def __repr__(self) -> str:
        END = '\033[0'
        START = '\033[1;38;2'
        MOD = 'm'

        red_level, green_level, blue_level = self.color
        return f'{START};{red_level};{green_level};{blue_level}{MOD}●{END}{MOD}'

    def __eq__(self, another: object) -> bool:
        return self.color == another.color

    def __add__(self, another: object) -> object:
        red_level, green_level, blue_level = self.color
        red_level2, green_level2, blue_level2 = another.color
        return Color(red_level + red_level2, green_level + green_level2, blue_level + blue_level2)

    def __hash__(self) -> int:
        return hash(self.color)

    def __rmul__(self, another: float) -> object:
        cl = -256 * (1 - another)
        F = 259 * (cl + 255) /(255 * (259 - cl))
        new_colors = [F*(i - 128) + 128 for i in self.color]
        return Color(*new_colors)


