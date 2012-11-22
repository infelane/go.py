class Canvas(object):
    EMPTY = None

    class CanvasError(Exception):
        pass

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._reset()

    def _reset(self, value=None):
        value = value or self.EMPTY

        self._canvas = [
            [value for i in range(self._width)]
            for j in range(self._height)
        ]

    def _check_coords(self, x, y):
        if (
            x < 1 or
            x > self._width or
            y < 1 or
            y > self._height
        ):
            raise self.CanvasError('Coordinates ({x}, {y}) are not within canvas dimensions {w}x{h}'.format(
                x=x, y=y, w=self._width, h=self._height
            ))

    def set(self, x, y, value):
        self._check_coords(x, y)
        self._canvas[y - 1][x - 1] = value

    def get(self, x, y):
        self._check_coords(x, y)
        return self._canvas[y - 1][x - 1]

    def __eq__(self, other):
        return self._canvas == other._canvas
