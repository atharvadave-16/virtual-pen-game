import json
import matplotlib.pyplot as plt
with open("ml/strokes.json", "r") as file:
    strokes = json.load(file)

print("Number of strokes:", len(strokes))
for stroke in strokes:
    x_vals = [point["x"] for point in stroke]
    y_vals = [point["y"] for point in stroke]

    plt.plot(x_vals, y_vals)
plt.gca().invert_yaxis()
plt.title("Replayed Drawing from Data")
plt.show()
