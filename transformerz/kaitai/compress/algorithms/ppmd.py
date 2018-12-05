import typing
from enum import Enum

import pyppmd

from ..core import KaitaiCompressor, ProcessorContextStub


class Variant(Enum):
	H = h = "H"
	I = i = "I"


class RestoreMethod(IntEnum):
	restart = pyppmd.PPMD8_RESTORE_METHOD_RESTART
	cut_off = pyppmd.PPMD8_RESTORE_METHOD_CUT_OFF


class PPMD(KaitaiCompressor):
	__slots__ = ("params",)

	def __init__(self, algo: Variant = Variant.I, max_order: int = 64, mem_size: int = 0x100_0000, restore_method: int = RestoreMethod.restart, *args, **kwargs) -> None:  # pylint:disable=redefined-builtin,too-many-arguments,too-many-locals,unused-argument,too-many-branches
		super().__init__()
		if isinstance(algo, str):
			algo = Variant[algo]

		self.params = {
			"max_order": max_order,
			"mem_size": mem_size,
			"restore_method": int(restore_method),
			"variant": algo.value,
		}

	def process(self, data: typing.Union[bytes, bytearray]) -> ProcessorContextStub:
		decompressor = pyppmd.PpmdDecompressor(**self.params)
		return ProcessorContextStub(decompressor.decompress(data))

	def unprocess(self, data: typing.Union[bytes, bytearray]) -> ProcessorContextStub:
		compressor = pyppmd.PpmdCompressor(**self.params)
		return ProcessorContextStub(compressor.compress(data) + compressor.flush())
