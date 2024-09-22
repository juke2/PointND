import copy
import math
import numpy as np
import matplotlib.pyplot as plt
from typing import Self, Union


class DimensionalityError(Exception):
    pass


class PointND:
    """Class representing a point with n dimensions."""

    __data: list

    def __init__(self, _data: list):
        self.__data = [datapoint for datapoint in _data]

    def __str__(self) -> str:
        return f'({", ".join([str(datapoint) for datapoint in self.__data])})'

    def __add__(self, q: object) -> Self:
        data = copy.deepcopy(self.__data)
        if hasattr(q, "__len__"):
            for index in range(len(data)):
                data[index] += q[index] if index < len(q) else 0
        else:
            data = [datapoint + q for datapoint in data]
        return self.__class__(data)

    def __mul__(self, q: object) -> Self:
        data = copy.deepcopy(self.__data)
        if hasattr(q, "__len__"):
            for index in range(len(data)):
                data[index] *= q[index] if index < len(q) else 1
        else:
            data = [datapoint * q for datapoint in data]
        return self.__class__(data)

    def dotproduct(self, q: Self) -> Self:
        """Returns the dot product of this PointND object and another PointND object"""
        if not len(self.__data) == len(q):
            raise DimensionalityError("Length of PointND objects differ.")
        sum = 0
        for index, a in enumerate(self.__data):
            sum += a * q[index]
        return sum

    def distance(self, q: Self) -> Self:
        """Returns the distance between this PointND object and another PointND object"""
        if not len(self.__data) == len(q):
            raise DimensionalityError("Length of PointND objects differ.")
        sum = 0
        for index, a in enumerate(self.__data):
            sum += math.pow((a - q[index]), 2)
        return math.sqrt(sum)

    def __sub__(self, q: object) -> Self:
        data = copy.deepcopy(self.__data)
        if hasattr(q, "__len__"):
            for index in range(len(data)):
                data[index] -= q[index] if index < len(q) else 0
        else:
            data = [datapoint - q for datapoint in data]
        return self.__class__(data)

    def __iter__(self) -> Self:
        return self.__data.__iter__()

    def __len__(self) -> int:
        return len(self.__data)

    def __getitem__(self, y) -> Union[float, int, None]:
        return self.__data[y]

    def __setitem__(self, i, v) -> Self:
        self.__data[i] = v
        return self

    def __eq__(self, q: object) -> bool:
        return hasattr(q, "__len__") and [i for i in self.__iter__()] == [
            i for i in q.__iter__()
        ]

    def __ne__(self, q: object) -> bool:
        return not self.__eq__(q)

    @classmethod
    def fromString(cls, s: str) -> Self:
        return cls(
            [
                (int(number) if number.find(".") == -1 else float(number))
                for number in s[1:-1].split(", ")
            ]
        )


class Point2D(PointND):
    """Class representing a point with 2 dimensions"""

    fig = plt.figure()
    axes = fig.add_subplot()

    def __init__(self, _x: Union[int, float, list], _y: Union[int, float] = None):
        if hasattr(_x, "__len__"):
            super().__init__(_x if len(_x) == 2 else [None] * 2)
        else:
            super().__init__([_x, _y])

    def plot(self, fmt="b.", **kwargs):
        self.axes.plot(self[0], self[1], fmt, **kwargs)

    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, value: Union[float, int]):
        self[0] = value

    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, value: Union[float, int]):
        self[1] = value


class Point3D(PointND):
    """Class representing a point with 3 dimensions"""

    fig = plt.figure()
    axes = fig.add_subplot(projection="3d")

    def __init__(
        self,
        _x: Union[int, float, list],
        _y: Union[int, float] = None,
        _z: Union[int, float] = None,
    ):
        if hasattr(_x, "__len__"):
            super().__init__(_x if len(_x) == 3 else [None] * 3)
        else:
            super().__init__([_x, _y, _z])

    def plot(self, fmt="b.", **kwargs):
        self.axes.scatter(self[0], self[1], self[2], fmt, **kwargs)
        pass

    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, value: Union[float, int]):
        self[0] = value

    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, value: Union[float, int]):
        self[1] = value

    @property
    def z(self):
        return self[2]

    @z.setter
    def z(self, value: Union[float, int]):
        self[2] = value


def test_dot_product():
    point_a = PointND([1, 5.39, 6.12, 3.9, 2.3])
    point_b = PointND([-1, 9.29, 4.30, -12.34, 2])
    dot_product_numpy = np.dot(
        np.array([i for i in point_a.__iter__()]),
        np.array([i for i in point_b.__iter__()]),
    )
    dot_product_pointND = point_a.dotproduct(point_b)
    try:
        point_a.dotproduct(PointND([2]))
    except Exception as exception:
        assert type(exception) == DimensionalityError
    assert dot_product_numpy == dot_product_pointND


def test_distance():
    point_a = PointND([1, 5.39, 6.12, 3.9, 2.3])
    point_b = PointND([-1, 9.29, 4.30, -12.34, 2])
    distance_numpy = np.linalg.norm(
        np.array([i for i in point_a.__iter__()])
        - np.array([i for i in point_b.__iter__()])
    )
    distance_pointND = point_a.distance(point_b)
    try:
        point_a.distance(PointND([2]))
    except Exception as exception:
        assert type(exception) == DimensionalityError
    assert distance_numpy == distance_pointND


def test_eq_and_ne():
    assert not 2 == PointND([2])
    assert not PointND([2, 3]) == PointND([5, 4])
    assert PointND([5, 5, 4]) == PointND([5, 5, 4])
    assert PointND([5, 5, 4]) == [5, 5, 4]
    assert 2 != PointND([2])
    assert PointND([2, 3]) != PointND([5, 4])
    assert not PointND([5, 5, 4]) != PointND([5, 5, 4])
    assert not PointND([5, 5, 4]) != [5, 5, 4]


def test_basic_math():
    point_a = PointND([1, 2, 3])
    point_b = PointND([3, 2, 1])
    assert (point_b + point_a) == PointND([4, 4, 4])
    assert point_a - point_b == PointND([-2, 0, 2])
    assert point_a * point_b == PointND([3, 4, 3])


def test_str():
    point_a = PointND([3, 4, 5])
    assert str(point_a) == "(3, 4, 5)"


def test_iter():
    point_a = PointND([0, 1, 2])
    for element in point_a:
        assert element in range(0, 3)


def test_from_str():
    assert PointND.fromString("(3, 4, 5)") == PointND([3, 4, 5])
    assert PointND.fromString("(3.2, 4.33, 5.123)") == PointND([3.2, 4.33, 5.123])
    try:
        PointND.fromString("waga, ,skd  faok, ")
    except Exception as exception:
        assert type(exception) == ValueError
