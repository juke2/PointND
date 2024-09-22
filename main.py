import src.PointND as PointND_file
from src.PointND import PointND, Point2D, Point3D
import matplotlib.pyplot as plt
import math
import src.sierpinski as sier


def main() -> None:
    PointND_file.test_dot_product()
    PointND_file.test_distance()
    PointND_file.test_eq_and_ne()
    PointND_file.test_basic_math()
    PointND_file.test_str()
    PointND_file.test_from_str()
    PointND_file.test_iter()
    sier.iterate_sierpinski_chaos_game_2d(
        *sier.generate_2d_triangle_verticies(2), 1000, output=False
    )
    sier.iterate_sierpinski_chaos_game_3d(*sier.generate_3d_triangle_verticies(3), 200)
    Point2D.fig.savefig("src/images/output_sierpinski_chaos")
    Point3D.fig.savefig("src/images/output_sierpinski_chaos_3d")
    for iteration in range(1, 7):
        Point2D.axes.cla()
        sier.iterate_sierpinski(*sier.generate_2d_triangle_verticies(2), iteration)
        Point2D.fig.savefig(f"src/images/output_sierpinski_iteration_{iteration}")


if __name__ == "__main__":
    main()
