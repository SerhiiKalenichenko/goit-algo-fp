import argparse
import math

import matplotlib.pyplot as plt


def draw_square(ax, x, y, size, angle):
    points = []
    for dx, dy in ((0, 0), (size, 0), (size, size), (0, size)):
        rx = x + dx * math.cos(angle) - dy * math.sin(angle)
        ry = y + dx * math.sin(angle) + dy * math.cos(angle)
        points.append((rx, ry))

    polygon = plt.Polygon(points, closed=True,
                          edgecolor="black", facecolor="green", linewidth=0.5)
    ax.add_patch(polygon)
    return points


def pythagoras_tree(ax, x, y, size, angle, level):
    if level == 0:
        return

    points = draw_square(ax, x, y, size, angle)
    p3 = points[3]
    p2 = points[2]

    vx = p2[0] - p3[0]
    vy = p2[1] - p3[1]

    new_size = math.hypot(vx, vy) * math.cos(math.radians(45))
    angle_left = angle + math.radians(45)
    angle_right = angle - math.radians(45)

    pythagoras_tree(ax, p3[0], p3[1], new_size, angle_left, level - 1)
    pythagoras_tree(ax, p2[0], p2[1], new_size, angle_right, level - 1)


def main(recursion_level: int):
    fig, ax = plt.subplots()
    pythagoras_tree(ax, x=0.0, y=0.0, size=1.0, angle=0.0, level=recursion_level)
    ax.set_aspect("equal")
    ax.axis("off")
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Візуалізація фрактала «дерево Піфагора»."
    )
    parser.add_argument(
        "--level",
        type=int,
        default=6,
        help="Рівень рекурсії (рекомендовано 5–9).",
    )
    args = parser.parse_args()
    main(args.level)