__all__ = ("dhallSerializer",)

import typing
from warnings import warn

warn('dhall seems like a bloated and having PRIVACY/SECURITY issue (http requests, also it is too flexible, so shouldn\'t be used to deserialize untrusted data), and dhall python serializes in "normalized" way, in which everything is copied as much as it can be. So it is no more useful for serialization than JSON.')
import dhall

from ..core import FileTransformer
from . import NoneType, jsonSerializableTypes

dhallSerializer = FileTransformer("dhall", dhall.dumps, dhall.loads, str, jsonSerializableTypes, "dhall", "application/x-dhall")
