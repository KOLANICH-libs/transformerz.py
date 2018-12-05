import typing

import lzo

from ..core import KaitaiCompressor, ProcessorContextStub

# pylint:disable=arguments-differ

try:
	from lzo import compress as _compress
	from lzo import decompress as _decompress
except ImportError:

	def _compress(d: bytes, level: int = None, mtime: int = None) -> bytes:
		with BytesIO() as oF:
			with lzo.LzoFile(mode="wb", fileobj=oF, compresslevel=level, mtime=mtime) as cf:
				cf.write(d)
			return oF.getvalue()

	def _decompress(d: bytes) -> bytes:
		with BytesIO(d) as iF:
			with lzo.LzoFile(mode="rb", fileobj=iF) as cf:
				return cf.read()


class LZO(KaitaiCompressor):
	__slots__ = ("level", "mtime")

	def __init__(self, level: int = None, mtime: int = None, *args, **kwargs) -> None:  # pylint:disable=unused-argument
		super().__init__()
		self.level = level
		self.mtime = mtime

	def process(self, data: typing.Union[bytes, bytearray]) -> ProcessorContextStub:
		return ProcessorContextStub(_decompress(data, self.level, self.mtime))

	def unprocess(self, data: typing.Union[bytes, bytearray]) -> ProcessorContextStub:
		return ProcessorContextStub(_compress(data))
