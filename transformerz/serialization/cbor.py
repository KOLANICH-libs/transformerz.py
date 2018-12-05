__all__ = ("cborSerializer",)
from ..core import FileTransformer
from . import jsonSerializableTypes

try:
	from functools import partial

	import cbor2 as cbor

	_cborDump = partial(cbor.dumps, value_sharing=True, string_referencing=True)
except ImportError:
	import cbor

	_cborDump = _cborDumps

cborSerializer = FileTransformer("cbor", _cborDump, cbor.loads, bytes, jsonSerializableTypes, "cbor", "application/cbor")
