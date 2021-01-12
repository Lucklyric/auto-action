from importlib import import_module
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def load_yaml(fileName):
    """load_yaml.

    Args:
        fileName:
    """
    with open(fileName, 'r') as f:
        return load(f, Loader=Loader)
