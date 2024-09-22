from src.PointND import Point2D, Point3D, DimensionalityError
from typing import Union
from wand.sequence import Sequence
from wand.image import Image
import random
import math


def iterate_sierpinski_chaos_game_2d(
    v1: Point2D, v2: Point2D, v3: Point2D, iterations: int, output: bool = False
):
    if output and iterations > 100:
        iterations = (
            100
            # lock iterations to fixed point
            # so wand can still make a gif out of it
            # if we are making a gif
        )
    if v1.__class__ != v2.__class__ or v2.__class__ != v3.__class__:
        raise DimensionalityError
    with Image(width=640, height=480) as wand:
        rand_vertex_1 = [v1, v2, v3][random.randrange(0, 3)]
        rand_vertex_2 = [v1, v2, v3][random.randrange(0, 3)]
        start_point_dimensions = []
        for dimension in range(len(v1)):
            start_point_dimensions.append(
                (rand_vertex_1[dimension] + rand_vertex_2[dimension]) / 2
            )
        start_point = v1.__class__(start_point_dimensions)
        for iteration in range(iterations):
            point_list = []
            rand_vertex = [v1, v2, v3][random.randrange(0, 3)]
            for dimension in range(len(v1)):
                point_list.append((rand_vertex[dimension] + start_point[dimension]) / 2)
            start_point = v1.__class__(point_list)
            start_point.plot()
            if output:
                Point2D.fig.savefig("src/images/output_sierpinski")
                print(f"Iteration: {iteration}")
                with Image(
                    filename="./src/images/output_sierpinski_for_gif.png"
                ) as img:
                    wand.sequence.append(img)
        if output:
            wand.type = "optimize"
            wand.save(filename="src/images/output_sierpinski_anim.gif")


def iterate_sierpinski_chaos_game_3d(
    v1: Point3D,
    v2: Point3D,
    v3: Point3D,
    v4: Point3D,
    iterations: int,
):
    if (
        v1.__class__ != v2.__class__
        or v2.__class__ != v3.__class__
        or v3.__class__ != v4.__class__
    ):
        raise DimensionalityError
    rand_vertex_1 = [v1, v2, v3, v4][random.randrange(0, 4)]
    rand_vertex_2 = [v1, v2, v3, v4][random.randrange(0, 4)]
    start_point_dimensions = []
    for dimension in range(len(v1)):
        start_point_dimensions.append(
            (rand_vertex_1[dimension] + rand_vertex_2[dimension]) / 2
        )
    start_point = v1.__class__(start_point_dimensions)
    for iteration in range(iterations):
        point_list = []
        rand_vertex = [v1, v2, v3, v4][random.randrange(0, 4)]
        for dimension in range(len(v1)):
            point_list.append((rand_vertex[dimension] + start_point[dimension]) / 2)
        start_point = v1.__class__(point_list)
        start_point.plot()


def rand_point_in_dimension(
    v1: Union[int, float], v2: Union[int, float], v3: Union[int, float]
):  # unused
    s = random.random()
    t = math.sqrt(random.random())
    return (1 - t) * v1 + t * ((1 - s) * v2 + s * v3)


def generate_2d_triangle_verticies(sidelength: int) -> list:
    v1 = Point2D(0, 0)
    v2 = Point2D(sidelength, 0)
    v3 = Point2D(sidelength / 2, sidelength / 2 * math.sqrt(3))
    return [v1, v2, v3]


def generate_3d_triangle_verticies(sidelength: int) -> list:
    v1 = Point3D(sidelength, 0, 0)
    v2 = Point3D(sidelength / 2, 0, sidelength * math.sqrt(3) / 2)
    v3 = Point3D(3 * sidelength / 2, 0, sidelength / 2 * math.sqrt(3))
    v4 = Point3D(
        sidelength,
        math.sqrt(6) / 3 * sidelength,
        sidelength - (sidelength / (2 * math.sqrt(3))),
    )
    return [v1, v2, v3, v4]


def iterate_sierpinski(v1: Point2D, v2: Point2D, v3: Point2D, iterations: int) -> None:
    if iterations <= 0:
        Point2D.axes.fill([v1.x, v2.x, v3.x], [v1.y, v2.y, v3.y])
    else:
        iterate_sierpinski(v1, midpoint_2d(v1, v2), midpoint_2d(v1, v3), iterations - 1)
        iterate_sierpinski(midpoint_2d(v1, v2), v2, midpoint_2d(v3, v2), iterations - 1)
        iterate_sierpinski(midpoint_2d(v1, v3), midpoint_2d(v2, v3), v3, iterations - 1)


def midpoint_2d(v1: Point2D, v2: Point2D):
    return Point2D((v1.x + v2.x) / 2, (v1.y + v2.y) / 2)
