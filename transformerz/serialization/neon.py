__all__ = ("neonSerializer",)

import re
import typing
from io import StringIO

import neon

from ..core import FileTransformer
from . import jsonSerializableTypes

neonSerializer = FileTransformer("neon", neon.encode, neon.decode, str, jsonSerializableTypes, "neon", None)
