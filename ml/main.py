import json
import matplotlib.pyplot as plt
import math

def stroke_length(stroke):
    """Return total length of one stroke (sum of distances between consecutive points)."""
    if len(stroke) < 2:
        return 0.0

    total = 0.0
    for i in range(1, len(stroke)):
        x1, y1 = stroke[i - 1]["x"], stroke[i - 1]["y"]
        x2, y2 = stroke[i]["x"], stroke[i]["y"]
        total += math.dist((x1, y1), (x2, y2))
    return total

def flatten_points(strokes):
    """Convert strokes -> single list of points."""
    pts = []
    for stroke in strokes:
        for p in stroke:
            pts.append((p["x"], p["y"]))
    return pts

def normalize_strokes(strokes, target_size=300):
    """
    Normalize drawing:
    - translate so min x,y becomes 0,0
    - scale so max side becomes target_size
    - keep aspect ratio
    Returns: new strokes list with normalized points.
    """
    pts = flatten_points(strokes)
    if not pts:
        return strokes

    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    width = max_x - min_x
    height = max_y - min_y
    scale = target_size / max(width, height) if max(width, height) != 0 else 1.0

    normalized = []
    for stroke in strokes:
        new_stroke = []
        for p in stroke:
            nx = (p["x"] - min_x) * scale
            ny = (p["y"] - min_y) * scale
            new_stroke.append({"x": nx, "y": ny})
        normalized.append(new_stroke)

    return normalized

with open("ml/strokes.json", "r") as file:
    strokes = json.load(file)
norm_strokes = normalize_strokes(strokes, target_size=300)





print("Number of strokes:", len(strokes))
for stroke in norm_strokes:
    x_vals = [point["x"] for point in stroke]
    y_vals = [point["y"] for point in stroke]

    plt.plot(x_vals, y_vals)
plt.gca().invert_yaxis()
plt.axis("equal")
plt.title("Normalized Replayed Drawing")

plt.show()
total_len = sum(stroke_length(stroke) for stroke in strokes)
print("Total drawing length:", round(total_len, 2))
def bounding_box(strokes):
    pts = flatten_points(strokes)
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)
print("Original bbox:", bounding_box(strokes))
print("Normalized bbox:", bounding_box(norm_strokes))


