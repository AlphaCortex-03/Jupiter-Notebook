"""Image processing demo using Pillow and matplotlib.

Generates a gradient color image and applies grayscale, resize,
and rotate transformations. Saves all outputs to the images/ folder.
"""

import os
import sys

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps

OUTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images")
os.makedirs(OUTDIR, exist_ok=True)

width, height = 400, 300
img = Image.new("RGB", (width, height))

for y in range(height):
    for x in range(width):
        r = int(255 * x / width)
        g = int(255 * y / height)
        b = 128
        img.putpixel((x, y), (r, g, b))

gray = ImageOps.grayscale(img)
resized = img.resize((200, 150))
rotated = img.rotate(45, expand=True)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].imshow(img); axes[0, 0].set_title("Original (400x300)"); axes[0, 0].axis("off")
axes[0, 1].imshow(gray, cmap="gray"); axes[0, 1].set_title("Grayscale"); axes[0, 1].axis("off")
axes[1, 0].imshow(resized); axes[1, 0].set_title("Resized (200x150)"); axes[1, 0].axis("off")
axes[1, 1].imshow(rotated); axes[1, 1].set_title("Rotated 45 deg"); axes[1, 1].axis("off")

arr = np.array(img)
stats = f"shape={arr.shape}  min={arr.min()}  max={arr.max()}  mean={arr.mean():.1f}"
fig.suptitle("Jupyter Image Program Output\n" + stats, fontsize=11)
plt.tight_layout()

outpath = os.path.join(OUTDIR, "output.png")
plt.savefig(outpath, dpi=100)
plt.close()

print(f"Saved output.png to: {OUTDIR}")
print("Image shape:", arr.shape)
print("Min pixel value:", arr.min())
print("Max pixel value:", arr.max())
print("Mean pixel value:", round(float(arr.mean()), 2))
