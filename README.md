# NakshPy

NakshPy is a Python library for generating and visualizing South Asian textile-inspired geometric patterns using computational geometry and symmetry transformations.

## Features

- Generate regular polygons
- Generate star patterns
- Generate simple Ajrak-inspired motifs
- Rotate, translate, scale, and reflect patterns
- Visualize patterns with Matplotlib
- Export patterns as PNG images

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/naqsh-py.git
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

## Quick Start

```python
import nakshpy as nk

star = nk.star_pattern(
    points=8,
    outer_radius=2,
    inner_radius=1
)

star = nk.rotate(star, 30)

nk.draw(star)

nk.save("star_pattern.png")
```

## Project Structure

```
naqsh-py/
│
├── examples/
├── nakshpy/
│   ├── geometry.py
│   ├── symmetry.py
│   ├── motifs.py
│   ├── visualization.py
│   ├── export.py
│   └── __init__.py
│
├── tests/
├── README.md
├── requirements.txt
└── pyproject.toml
```

## Future Development

- Additional South Asian textile motifs
- SVG export
- More symmetry operations
- Interactive visualization
- Pattern tiling and tessellation

## License

This project is licensed under the MIT License.
