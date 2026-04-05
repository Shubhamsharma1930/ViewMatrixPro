# ViewMatrixPro 🚀

[![PyPI version](https://img.shields.io/pypi/v/ViewMatrixPro.svg)](https://pypi.org/project/ViewMatrixPro/)
[![Python versions](https://img.shields.io/pypi/pyversions/ViewMatrixPro.svg)](https://pypi.org/project/ViewMatrixPro/)
[![License](https://img.shields.io/pypi/l/ViewMatrixPro.svg)](https://github.com/entbappy/ViewMatrixPro/blob/main/LICENSE)

**ViewMatrixPro** is a lightweight Python library designed for Data Scientists and Jupyter Notebook users. It allows you to seamlessly render live websites and embed YouTube videos directly within your `.ipynb` environment (Jupyter Notebook, JupyterLab, Google Colab).

Stop switching tabs to read documentation or watch tutorials—view them right next to your code!

---

## ✨ Features

- **🌐 Website Rendering:** Render any HTTPS website directly in an output cell.
- **▶️ YouTube Integration:** intelligent parsing of YouTube URLs to embed the video player automatically.
- **📏 Customizable:** easily adjust width, height, and alignment of the viewport.
- **⚡ Lightweight:** Zero heavy dependencies; built on top of standard IPython display tools.

---

## 📦 Installation

You can install ViewMatrixPro via pip:

```bash
pip install ViewMatrixPro
```

```python
from ViewMatrixPro.youtube import render_youtube_video

render_youtube_video("https://www.youtube.com/watch?v=h25pePMdoPA&t=712s")
```

```python
from ViewMatrixPro.site import render_site

render_site("https://www.google.com")
```

# How to Install this package in Your System

```bash
conda create -n viewmatrixpro_env python=3.10 -y
```

```bash
conda activate viewmatrixpro_env
```

```bash
pip install -r requirements_dev.txt
```