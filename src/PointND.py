import copy
from typing import Self, Union


class PointND:
    """Class representing a point with n dimensions."""

    data: list

    def __init__(self, _data: list):
        self.data = [datapoint for datapoint in _data]

    def __str__(self) -> str:
        return f'({", ".join(str(datapoint) for datapoint in self.data)})'

    def __add__(self, q: object) -> Self:
        data = copy.deepcopy(self.data)
        if hasattr(q, "__len__"):
            for index in range(len(data)):
                data[index] += q[index] if index < len(q) else 0
        else:
            data = [datapoint + q for datapoint in data]
        return PointND(data)

    def __mul__(self, q: object) -> Self:
        data = copy.deepcopy(self.data)
        if hasattr(q, "__len__"):
            for index in range(len(data)):
                data[index] *= q[index] if index < len(q) else 1
        else:
            data = [datapoint * q for datapoint in data]
        return PointND(data)

    def dotproduct(self, q: Self) -> Self:
        """Returns the dot product of this PointND object and another PointND object"""
        pass

    def distance(self, q: Self) -> Self:
        """Returns the distance between this PointND object and another PointND object"""
        pass

    def __sub__(self, q: object) -> Self:
        data = copy.deepcopy(self.data)
        if hasattr(q, "__len__"):
            for index in range(len(data)):
                data[index] += q[index] if index < len(q) else 0
        else:
            data = [datapoint - q for datapoint in data]
        return PointND(data)

    def __iter__(self):
        pass

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, y) -> Union[float, int, None]:
        """
        Attempts to return the desired index from the internal array representing each dimension.
        Guards against bad input, so instead of accessing an invalid index it will return null.
        """
        if y < len(self.data):
            return self.data[y]
        return None

    @staticmethod
    def fromString(s: str) -> Self:
        pass


class Point2D(PointND):
    """Class representing a point with 2 dimensions"""

    def __init__(self, _x: int, _y: int):
        super().__init__([_x, _y])

    def plot(self, **kwargs):
        pass


class Point3D(PointND):
    """Class representing a point with 3 dimensions"""

    def __init__(self, _x, _y, _z):
        super().__init__([_x, _y, _z])
