import argparse
import cmath
import matplotlib.pyplot as plt


def draw_square(ax, z, dz):
    p0 = z
    p1 = z + dz
    p2 = z + dz + dz * 1j
    p3 = z + dz * 1j

    xs = [p.real for p in (p0, p1, p2, p3, p0)]
    ys = [p.imag for p in (p0, p1, p2, p3, p0)]

    ax.fill(xs, ys, edgecolor="black", facecolor="green", linewidth=0.4)


def pythagoras_tree(ax, n, z, dz):
    if n == 0:
        return

    draw_square(ax, z, dz)

    z_top_left = z + dz * 1j
    dz_left = dz * (1 + 1j) / 2
    dz_right = dz * (1 - 1j) / 2

    pythagoras_tree(ax, n - 1, z_top_left, dz_left)
    pythagoras_tree(ax, n - 1, z_top_left + dz_left, dz_right)


def main(level: int):
    fig, ax = plt.subplots()

    z0 = -0.5 + 0j
    dz0 = 1 + 0j

    pythagoras_tree(ax, level, z0, dz0)

    ax.set_aspect("equal")
    ax.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", type=int, help="Рівень рекурсії (5–10 рекомендовано)")
    args = parser.parse_args()

    if args.level is None:
        try:
            level = int(input("Вкажіть рівень рекурсії (наприклад 7): "))
        except ValueError:
            level = 7
    else:
        level = args.level

    main(level)