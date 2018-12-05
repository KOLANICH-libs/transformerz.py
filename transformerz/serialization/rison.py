__all__ = ("risonSerializer",)

import typing

try:
	import prison as rison
except ImportError:
	import rison

from ..core import FileTransformer
from . import jsonSerializableTypes

risonSerializer = FileTransformer("rison", rison.dumps, rison.loads, str, jsonSerializableTypes, "rison")
