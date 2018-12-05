import typing

import compressed_rtf

from ..core import KaitaiCompressor, ProcessorContextStub

# pylint:disable=arguments-differ


class LZFu(KaitaiCompressor):
	__slots__ = ()

	def __init__(self, *args, **kwargs) -> None:  # pylint:disable=unused-argument
		super().__init__()

	def process(self, data: typing.Union[bytes, bytearray]) -> ProcessorContextStub:
		return ProcessorContextStub(compressed_rtf.decompress(data))

	def unprocess(self, data: typing.Union[bytes, bytearray]) -> ProcessorContextStub:
		return ProcessorContextStub(compressed_rtf.compress(data))
