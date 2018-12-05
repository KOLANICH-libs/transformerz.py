__all__ = ("ubjsonSerializer",)

import typing

import ubjson

from ..core import FileTransformer
from . import NoneType, jsonSerializableTypes

ubjsonSerializer = FileTransformer("ubjson", ubjson.dumpb, ubjson.loadb, bytes, jsonSerializableTypes, "ubj", "application/ubjson")
