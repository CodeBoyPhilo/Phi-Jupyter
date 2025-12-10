# Philo's Jupyter Configuration and Utilities Backup

A backup of my personal configurations and utilities for jupyter lab. It gives you a pre-configured jupyter envrionment with nice defaults.

> [!CAUTION]
> This project, including this README file, is generated with Claude-Sonnet-4.5. Use at your own risk.

> [!CAUTION]
> Only tested on linux (NixOS). It may not work on your machine.

## ✨ Features

- 🎨 **Syntax-highlighted pretty printing** - Beautiful output with Catppuccin Mocha theme
- ⚙️ **Consistent JupyterLab settings** - Editor font, theme, and preferences synced across machines
- 🔌 **Pre-configured extensions** - Vim mode, Git integration, code formatting, and more
- 🚀 **Auto-loaded utilities** - Common functions available in every notebook without importing
- 📦 **One-command install** - Get everything set up instantly
- 🔄 **Easy updates** - Stay in sync with latest improvements

## 📦 Installation

### Requirements

`Python 3.10+`

`uv`

[Maple Mono](https://github.com/subframe7536/maple-font.git) (NF CN variant)

- First, clone this repo to your host machine:

  ```bash
  git clone https://github.com/CodeBoyPhilo/Phi-Jupyter.git /path/to/local/phi-jupyter
  ```

- You can either install it via:

  ```bash
  uv pip install -e /path/to/local/phi-jupyter
  ```

- or add it as a dependency in your `pyproject.toml`, for example:

  ```toml
  # add to your dependency:
  [project]
  name = "cool project"
  version = "X.X.X"
  dependencies = [
      "phi-jupyter",
  ]

  # then add the following:
  [tool.uv.sources]
  phi-jupyter = { path = "/path/to/local/phi-jupyter", editable = true}
  ```

  and run `uv sync`.

- This will install a jupyter environment with plugins. See [what gets installed](#what-gets-installed-and-enabled-by-default).

- Next, you will have to link my configurations and utilities to your `.ipython` and `.jupyter` folder respectively.
  This project provides a nice command line utility that does this for you.
  Simply run the following after installation:

  ```bash
  phi-jupyter-install
  ```

### What Gets Installed and Enabled by Default
- **Python utilities** 
    - `ppprint`, which is pretty print with syntax highlighting. using Catppuccin Mocha style as default.
- **JupyterLab extensions**:
  - Catppuccin Mocha theme
  - Vim keybindings 
  - Code formatter (Black, isort, Ruff): format on save enabled
- **Editor settings**: Maple Mono NF CN font, line numbers, auto close brackets, etc.
- **IPython startup scripts**: Auto-load utilities in every notebook

## 🚀 Usage

- `ppprint`: 

    ```python
    ppprint('Hello World')
    ```
    additional keyword params:
    - `width: int = 80`
    - `theme: str = "catppuccin-mocha"`
    - `compact: bool = False`

