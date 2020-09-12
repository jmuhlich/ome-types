try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

try:
    from .model import OME
except ImportError:
    raise ImportError(
        "Could not import 'ome_types.model.OME'.\nIf you are in a dev environment, "
        "you may need to run 'python -m src.ome_autogen'"
    ) from None

from . import schema  # isort:skip

__all__ = ["OME", "schema"]
