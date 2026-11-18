# Jupiter Notebook

A professional Jupyter Notebook project for image processing with **Pillow** and **matplotlib**.

## Overview

This repository demonstrates a complete image processing workflow using Jupyter Notebooks:

- Creating a gradient color image programmatically
- Converting images to grayscale
- Resizing and rotating images
- Analyzing pixel statistics with NumPy

## Features

- **Image Generation** - Creates a smooth RGB gradient using Pillow
- **Image Manipulation** - Grayscale conversion, resize, and rotation
- **Data Analysis** - Pixel-level statistics (min, max, mean)
- **Visualization** - Side-by-side comparison plots with matplotlib

## Requirements

```bash
pip install pillow matplotlib numpy jupyter nbformat
```

## Project Structure

```
Jupiter-Notebook/
├── notebooks/
│   └── image_demo.ipynb          # Main Jupyter notebook
├── images/
│   ├── output.png                # Combined output visualization
│   ├── sample_image.png          # Original gradient image
│   ├── sample_gray.png           # Grayscale version
│   ├── sample_resized.png        # Resized image
│   └── sample_rotated.png        # Rotated image
├── scripts/
│   └── run_output.py             # Standalone script to generate outputs
└── README.md
```

## Usage

### Run as a Jupyter Notebook

```bash
jupyter notebook notebooks/image_demo.ipynb
```

Or open `image_demo.ipynb` directly in VS Code with the Jupyter extension.

### Run as a Standalone Script

```bash
python scripts/run_output.py
```

This generates all output images in the `images/` folder.

## Output

The program produces a 2x2 grid visualization:

| Subplot | Description |
|---------|-------------|
| Top-left | Original 400x300 RGB gradient |
| Top-right | Grayscale conversion |
| Bottom-left | Resized to 200x150 |
| Bottom-right | Rotated 45 degrees |

## Sample Output

```
Image shape: (300, 400, 3)
Min pixel value: 0
Max pixel value: 254
Mean pixel value: 127.1
```

## License

MIT