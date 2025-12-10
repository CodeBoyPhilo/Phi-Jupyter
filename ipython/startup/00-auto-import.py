"""Auto-load jupyter utilities"""
import sys

# Only load in IPython/Jupyter environments
try:
    get_ipython()
except NameError:
    # Not in IPython, skip
    pass
else:
    try:
        from jupyter_utils import ppprint
        print("✓ jupyter_utils loaded (ppprint available)")
    except ImportError:
        print("⚠ jupyter_utils not installed - run: jupyter-config install")
