"""Pretty printing with syntax highlighting"""
from pprint import pformat
from typing import Any

try:
    from IPython.display import HTML, display
    from pygments import highlight
    from pygments.formatters import HtmlFormatter
    from pygments.lexers import PythonLexer
    JUPYTER_AVAILABLE = True
except ImportError:
    JUPYTER_AVAILABLE = False


def ppprint(
    obj: Any,
    width: int = 80,
    compact: bool = False,
    theme: str = "catppuccin-mocha"
) -> None:
    """
    Pretty print with syntax highlighting for Jupyter.
    
    Args:
        obj: Object to print
        width: Maximum line width (default: 80)
        compact: Use compact representation (default: False)
        theme: Pygments theme name (default: 'catppuccin-mocha')
        
    Example:
        >>> data = {"name": "John", "age": 30, "items": [1, 2, 3]}
        >>> ppprint(data)
    """
    if not JUPYTER_AVAILABLE:
        # Fallback to regular pprint if not in Jupyter
        from pprint import pprint
        pprint(obj, width=width, compact=compact)
        return
    
    formatted = pformat(obj, width=width, compact=compact)
    formatter = HtmlFormatter(style=theme)
    highlighted = highlight(formatted, PythonLexer(), formatter)
    css = formatter.get_style_defs(".highlight")
    display(HTML(f"<style>{css}</style>{highlighted}"))
