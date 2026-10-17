"""Generate the isometric line-art project icons into src/icons/.

Run: python3 scripts/gen_icons.py
"""
import math, pathlib

C30, S30 = math.cos(math.pi / 6), 0.5
INK, GROUND, TOP, LEFT, RIGHT = "#171717", "#fafafa", "#ffffff", "#f1f1f1", "#e6e6e6"


class Iso:
    def __init__(self, s, ox, oy):
        self.s, self.ox, self.oy, self.out, self.seen = s, ox, oy, [], []

    def p(self, x, y, z):
        q = (self.ox + (x - y) * C30 * self.s, self.oy + (x + y) * S30 * self.s - z * self.s)
        self.seen.append(q)
        return q

    def poly(self, pts, fill=GROUND, stroke=INK, sw=1, extra=""):
        d = " ".join(f"{a:.1f},{b:.1f}" for a, b in (self.p(*q) for q in pts))
        self.out.append(f'<polygon points="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>')

    def line(self, a, b, stroke=INK, sw=1, extra=""):
        (x1, y1), (x2, y2) = self.p(*a), self.p(*b)
        self.out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}" {extra}/>')

    def box(self, x, y, z, w, d, h, top=TOP, left=LEFT, right=RIGHT, extra=""):
        # visible faces: +y face (lower-left), +x face (lower-right), top
        self.poly([(x, y + d, z), (x + w, y + d, z), (x + w, y + d, z + h), (x, y + d, z + h)], left, extra=extra)
        self.poly([(x + w, y, z), (x + w, y + d, z), (x + w, y + d, z + h), (x + w, y, z + h)], right, extra=extra)
        self.poly([(x, y, z + h), (x + w, y, z + h), (x + w, y + d, z + h), (x, y + d, z + h)], top, extra=extra)

    def circle(self, c, r, plane, fill=GROUND, n=36, sw=1):
        cx, cy, cz = c
        pts = []
        for i in range(n):
            t = 2 * math.pi * i / n
            u, v = r * math.cos(t), r * math.sin(t)
            pts.append({"xz": (cx + u, cy, cz + v), "yz": (cx, cy + u, cz + v), "xy": (cx + u, cy + v, cz)}[plane])
        self.poly(pts, fill, sw=sw)

    def cylinder_y(self, x, z, r, y0, y1, fill=LEFT):
        # cylinder whose axis runs along y; silhouette = hull of both end caps
        pts = []
        for y in (y0, y1):
            for i in range(48):
                t = 2 * math.pi * i / 48
                pts.append(self.p(x + r * math.cos(t), y, z + r * math.sin(t)))
        hull = convex_hull(pts)
        d = " ".join(f"{a:.1f},{b:.1f}" for a, b in hull)
        self.out.append(f'<polygon points="{d}" fill="{fill}" stroke="{INK}" stroke-width="1"/>')
        self.circle((x, y1, z), r, "xz", fill=TOP)
        self.circle((x, y1, z), r * 0.35, "xz", fill=LEFT)

    def svg(self, w, h, label):
        # fit the drawing into a w x h box, centered, with a little padding
        xs, ys = [q[0] for q in self.seen], [q[1] for q in self.seen]
        pad = 4
        bw, bh = max(xs) - min(xs) + 2 * pad, max(ys) - min(ys) + 2 * pad
        k = max(bw / w, bh / h)
        vx, vy = (min(xs) + max(xs) - w * k) / 2, (min(ys) + max(ys) - h * k) / 2
        body = "\n    ".join(self.out)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vx:.1f} {vy:.1f} {w*k:.1f} {h*k:.1f}" width="{w}" height="{h}" role="img" aria-label="{label}" '
                f'stroke-linejoin="round" stroke-linecap="round">\n    {body}\n  </svg>')


def convex_hull(pts):
    pts = sorted(set(pts))
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo, hi = [], []
    for q in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], q) <= 0: lo.pop()
        lo.append(q)
    for q in reversed(pts):
        while len(hi) >= 2 and cross(hi[-2], hi[-1], q) <= 0: hi.pop()
        hi.append(q)
    return lo[:-1] + hi[:-1]


def traffic_light():
    g = Iso(14, 80, 34)
    g.box(-0.6, -0.6, 0, 2.6, 2.6, 0.35)            # base plate
    g.box(0.45, 0.45, 0.35, 0.5, 0.5, 1.6)          # pole
    g.box(0, 0, 1.95, 1.4, 1.2, 4.2)                # housing
    # claude-lights state colors (Okabe-Ito, colorblind-safe): vermillion, amber, bluish-green
    lamps = [(5.45, "#d55e0033"), (4.05, "#e69f0033"), (2.65, "#009e73")]
    for z, fill in lamps:
        g.circle((0.7, 1.2, z), 0.48, "xz", fill=LEFT)
        g.circle((0.7, 1.2, z), 0.36, "xz", fill=fill)
        g.box(0.12, 1.2, z + 0.42, 1.16, 0.45, 0.08)  # visor
    # glow rays from the lit lamp
    for dx, dz in [(-1.6, 0.0), (-1.4, -0.9), (-1.4, 0.9)]:
        g.line((0.7 + dx * 0.55, 1.6, 2.65 + dz * 0.55), (0.7 + dx, 1.9, 2.65 + dz), stroke="#009e73", extra='stroke-dasharray="2 2"')
    return g.svg(160, 130, "claude-lights: an isometric traffic light with the green lamp lit")


def scroll():
    g = Iso(13, 70, 40)
    L, D = 6.0, 3.4
    g.cylinder_y(-0.35, 0.35, 0.35, -0.3, D + 0.3)  # back roller
    g.box(0, 0, 0, L, D, 0.06, top=TOP)             # paper
    # vertical poem columns run along y; each "character" is a short dash
    for col in range(5):
        x = 4.9 - col * 0.75
        for row in range(5):
            y0 = 0.35 + row * 0.55
            g.line((x, y0, 0.06), (x, y0 + 0.32, 0.06), stroke="#8f8f8f")
    g.poly([(0.7, 2.2, 0.06), (1.2, 2.2, 0.06), (1.2, 2.7, 0.06), (0.7, 2.7, 0.06)], fill="#c0392b", stroke="#c0392b")
    g.cylinder_y(L + 0.35, 0.35, 0.35, -0.3, D + 0.3)  # front roller
    return g.svg(160, 130, "AI poetry: an isometric unrolled scroll with vertical text columns and a red seal")


def keyboard():
    g = Iso(7.2, 80, 22)
    W = 6.6
    def half(ox, mirror):
        # the right half is the left half mirrored: stagger reversed, thumb keys on the inner (left) side
        def kx(x, w):
            return ox + (W - x - w if mirror else x)
        g.box(ox, 0, 0, W, 4.2, 0.5)
        stagger = [0.3, 0.3, 0.1, 0, 0.1, 0.2]  # left half, outer pinky column first, like a Corne
        keys = [(kx(0.2 + c * 1.05, 0.85), 0.2 + r * 1.05 + stagger[c], 0.85, TOP) for c in range(6) for r in range(3)]
        keys += [(kx(3.3 + k * 1.05, 0.85), 3.45, 0.65, "#f6f6f6") for k in range(3)]  # thumb keys
        for x, y, d, top in sorted(keys, key=lambda k: k[0] + k[1]):  # painter's order: far to near
            g.box(x, y, 0.5, 0.85, d, 0.35, top=top)
    half(0, mirror=False)
    half(8.2, mirror=True)
    # TRRS cable between the halves, drawn first so the halves sit on top of it
    (x1, y1), (x2, y2) = g.p(6.6, 0.6, 0.25), g.p(8.2, 0.6, 0.25)
    (cx, cy) = g.p(7.4, -1.2, 0)
    g.out.insert(0, f'<path d="M{x1:.1f},{y1:.1f} Q{cx:.1f},{cy:.1f} {x2:.1f},{y2:.1f}" fill="none" stroke="{INK}" stroke-width="1"/>')
    return g.svg(160, 130, "zmk-corne: two isometric split keyboard halves joined by a cable")


def next_box():
    g = Iso(16, 80, 38)
    dash = 'stroke-dasharray="3 3"'
    g.box(0, 0, 0, 3, 3, 2.4, top="none", left="none", right="none", extra=dash)
    # a screen-aligned "+" on the box top (iso-aligned strokes read as an "x")
    cx, cy = g.p(1.5, 1.5, 2.4)
    g.out.append(f'<path d="M{cx-7:.1f},{cy:.1f} H{cx+7:.1f} M{cx:.1f},{cy-7:.1f} V{cy+7:.1f}" stroke="{INK}" stroke-width="1.2"/>')
    return g.svg(160, 130, "Next: an empty dashed box waiting for the next project")


if __name__ == "__main__":
    out = pathlib.Path(__file__).resolve().parent.parent / "src" / "icons"
    out.mkdir(exist_ok=True)
    for name, fn in {"lights": traffic_light, "scroll": scroll, "keyboard": keyboard, "next": next_box}.items():
        (out / f"{name}.svg").write_text(fn() + "\n")
        print(f"wrote src/icons/{name}.svg")
