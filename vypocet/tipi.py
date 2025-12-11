import matplotlib.pyplot as plt
import numpy as np
import math

# -------------------------------------------------------
# 1) Funkce pro použití v packages.py (vrací jen délky!)
# -------------------------------------------------------
def get_delky_pruhu(r, a):
    full_strips = r // a
    rest = r % a

    y_levels = [i * a for i in range(int(full_strips) + 1)]
    if rest > 0:
        y_levels.append(r)

    delky = []

    for i in range(len(y_levels) - 1):
        y_bottom = y_levels[i]

        if i == 0:
            L = 2 * r                   # první pruh = průměr
        else:
            L = 2 * math.sqrt(max(0, r*r - y_bottom*y_bottom))

        delky.append(L)

    return delky


# -------------------------------------------------------
# 2) Plná funkce s grafem a výpisem (pro vizualizaci)
# -------------------------------------------------------
def tipi(r=600, a=145):

    full_strips = r // a
    rest = r % a

    y_levels = [i * a for i in range(int(full_strips) + 1)]
    if rest > 0:
        y_levels.append(r)

    pruhy = []
    delky = []

    for i in range(len(y_levels) - 1):
        y_bottom = y_levels[i]
        y_top = y_levels[i + 1]

        if i == 0:
            L = 2 * r
        else:
            L = 2 * math.sqrt(max(0, r*r - y_bottom*y_bottom))

        delky.append(L)

        pruhy.append({
            "index": i + 1,
            "y_bottom": y_bottom,
            "y_top": y_top,
            "delka": L
        })

    # ----------- GRAF -----------
    fig, ax = plt.subplots(figsize=(8, 6))

    theta = np.linspace(0, np.pi, 800)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.plot(x, y, color='orange', linewidth=2)

    colors = ["red", "blue", "magenta", "green", "grey", "orange"]

    for i, pruh in enumerate(pruhy):
        L = pruh["delka"]
        y0 = pruh["y_bottom"]
        y1 = pruh["y_top"]

        rect_x = -L / 2
        rect_w = L
        rect_h = y1 - y0

        ax.add_patch(plt.Rectangle(
            (rect_x, y0), rect_w, rect_h,
            fill=False, edgecolor=colors[i % len(colors)], linewidth=2))

        if y1 < r:
            x_int = math.sqrt(r*r - y1*y1)
            ax.scatter([x_int, -x_int], [y1, y1],
                       color=colors[i % len(colors)], s=60)
            ax.text(x_int + 10, y1 + 10, chr(ord('A') + i), color=colors[i % len(colors)])

    ax.axhline(0, color='black')
    ax.axvline(0, color='black')
    ax.set_aspect('equal', 'box')
    ax.set_xlim(-r - 50, r + 50)
    ax.set_ylim(0, r + 50)
    ax.grid(True)
    ax.set_title(f"Půlkruh s pruhy (r = {r} cm, šířka pruhu = {a} cm)")
    plt.show()

    # ----------------------------
    #         VÝPIS
    # ----------------------------
    print("Délky pruhů:")
    for pruh in pruhy:
        print(f"Pruh {pruh['index']}: {pruh['delka']:.2f} cm")

    return None


# ---------------------------
# Spuštění jen při přímém volání
# ---------------------------
if __name__ == "__main__":
    tipi(600, 145)
