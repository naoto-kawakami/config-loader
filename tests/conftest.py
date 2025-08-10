import sys
from pathlib import Path


# Add the project root to the system path for module imports
sys.path.insert(0, Path(__file__).expanduser().absolute().parent.parent.as_posix())
