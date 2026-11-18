"""Generate the professional image_demo.ipynb notebook."""

import nbformat as nbf

nb = nbf.v4.new_notebook()
nb["metadata"] = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3.12.10"},
}

cells = [
    nbf.v4.new_markdown_cell(
        "# Image Processing with Jupyter\n"
        "\n"
        "**[Portfolio Project](https://github.com/AlphaCortex-03/Jupiter-Notebook)**\n"
        "\n"
        "A hands-on demonstration of image manipulation using "
        "**Pillow** for image operations and **matplotlib** for visualization.\n"
        "\n"
        "### What this notebook covers\n"
        "\n"
        "1. Generating a synthetic RGB gradient image\n"
        "2. Converting to grayscale\n"
        "3. Resizing and rotating\n"
        "4. Computing pixel statistics with NumPy\n"
    ),
    nbf.v4.new_markdown_cell("## 1. Setup\n\nImport the required libraries and configure the output directory."),
    nbf.v4.new_code_cell(
        "from PIL import Image, ImageOps\n"
        "import matplotlib.pyplot as plt\n"
        "import numpy as np\n"
        "import os\n"
        "\n"
        "OUTDIR = os.path.join('..', 'images')\n"
        "os.makedirs(OUTDIR, exist_ok=True)\n"
        "\n"
        "print('Output directory:', os.path.abspath(OUTDIR))"
    ),
    nbf.v4.new_markdown_cell("## 2. Create a Gradient Image\n\nBuild a 400x300 image where red increases horizontally and green increases vertically."),
    nbf.v4.new_code_cell(
        "width, height = 400, 300\n"
        "img = Image.new('RGB', (width, height))\n"
        "\n"
        "for y in range(height):\n"
        "    for x in range(width):\n"
        "        r = int(255 * x / width)\n"
        "        g = int(255 * y / height)\n"
        "        b = 128\n"
        "        img.putpixel((x, y), (r, g, b))\n"
        "\n"
        "path = os.path.join(OUTDIR, 'sample_image.png')\n"
        "img.save(path)\n"
        "print('Saved:', path)\n"
        "print('Size:', img.size)"
    ),
    nbf.v4.new_markdown_cell("## 3. Display the Original Image"),
    nbf.v4.new_code_cell(
        "plt.figure(figsize=(8, 6))\n"
        "plt.imshow(img)\n"
        "plt.title('Original Color Image')\n"
        "plt.axis('off')\n"
        "plt.show()"
    ),
    nbf.v4.new_markdown_cell("## 4. Grayscale Conversion"),
    nbf.v4.new_code_cell(
        "gray = ImageOps.grayscale(img)\n"
        "\n"
        "fig, axes = plt.subplots(1, 2, figsize=(12, 5))\n"
        "axes[0].imshow(img)\n"
        "axes[0].set_title('Original')\n"
        "axes[0].axis('off')\n"
        "axes[1].imshow(gray, cmap='gray')\n"
        "axes[1].set_title('Grayscale')\n"
        "axes[1].axis('off')\n"
        "plt.tight_layout()\n"
        "plt.show()\n"
        "\n"
        "path = os.path.join(OUTDIR, 'sample_gray.png')\n"
        "gray.save(path)\n"
        "print('Saved:', path)"
    ),
    nbf.v4.new_markdown_cell("## 5. Resize and Rotate"),
    nbf.v4.new_code_cell(
        "resized = img.resize((200, 150))\n"
        "rotated = img.rotate(45, expand=True)\n"
        "\n"
        "fig, axes = plt.subplots(1, 3, figsize=(15, 5))\n"
        "axes[0].imshow(img)\n"
        "axes[0].set_title('Original (400x300)')\n"
        "axes[0].axis('off')\n"
        "axes[1].imshow(resized)\n"
        "axes[1].set_title('Resized (200x150)')\n"
        "axes[1].axis('off')\n"
        "axes[2].imshow(rotated)\n"
        "axes[2].set_title('Rotated 45 deg')\n"
        "axes[2].axis('off')\n"
        "plt.tight_layout()\n"
        "plt.show()\n"
        "\n"
        "resized.save(os.path.join(OUTDIR, 'sample_resized.png'))\n"
        "rotated.save(os.path.join(OUTDIR, 'sample_rotated.png'))\n"
        "print('Saved resized and rotated images')"
    ),
    nbf.v4.new_markdown_cell("## 6. Pixel Statistics"),
    nbf.v4.new_code_cell(
        "arr = np.array(img)\n"
        "print('Image shape:', arr.shape)\n"
        "print('Min pixel value:', arr.min())\n"
        "print('Max pixel value:', arr.max())\n"
        "print('Mean pixel value:', round(float(arr.mean()), 2))"
    ),
]

nb["cells"] = cells

with open(r"C:\Users\gopal\jupiter-repo\notebooks\image_demo.ipynb", "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print("notebook written")
