__all__ = ("msgpackSerializer",)
import typing
from collections.abc import Iterable, Mapping

from ..core import FileTransformer
from . import jsonSerializableTypes

try:
	import ormsgpack
except ImportError:
	import msgpack

	def _defaultHook(o: typing.Any):
		if isinstance(o, Mapping):
			return dict(o)
		elif isinstance(Iterable, o):
			return list(obj)
		return o

	msgpackPacker = msgpack.Packer(strict_types=True, default=_defaultHook)
	_packerF = msgpackPacker.pack
	_unpackerF = lambda d: msgpack.unpackb(d, raw=False)
else:
	_packerF = ormsgpack.packb
	_unpackerF = ormsgpack.unpackb

msgpackSerializer = FileTransformer("msgpack", _packerF, _unpackerF, bytes, jsonSerializableTypes, "msgpack", "application/msgpack")
