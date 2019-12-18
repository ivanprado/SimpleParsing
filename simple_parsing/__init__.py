"""
:mod:`simple_parsing` -- Main module.
=============================================================================
.. module:: simple_parsing
   :platform: Unix
   :synopsis: Main module
"""
from .utils import Formatter, InconsistentArgumentError, MutableField
from .parsing import ArgumentParser, ConflictResolution

__all__ = [
    "ArgumentParser",
    "InconsistentArgumentError",
    "Formatter",
    "ConflictResolution",
    "MutableField"
]