import os, sys

parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)

from config import Config


class ObjectsConfig(Config):
    """Configuration for training on the toy objects dataset.
    Derives from the base Config class and overrides values specific
    to the toy objects dataset.
    """
    # Give the configuration a recognizable name
    NAME = "objects"

    # # Number of classes (including background)
    NUM_CLASSES = 1 + 1  # background + 1 object
