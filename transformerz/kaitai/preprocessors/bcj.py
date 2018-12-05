import typing
from enum import IntEnum

from bcj import ArmDecoder, ArmEncoder, ArmtDecoder, ArmtEncoder, BCJDecoder, BCJEncoder, PpcDecoder, PpcEncoder, SparcDecoder, SparcEncoder

from ..compress.core import KaitaiCompressor, ProcessorContextStub

__all__ = ("BCJ",)

# pylint:disable=arguments-differ


class Arch(IntEnum):
	arm = 40
	arm_thumb = -arm
	x86 = 3
	sparc = 2
	ppc = 20


_archs = {
	Arch.arm: (ArmDecoder, ArmEncoder),
	Arch.arm_thumb: (ArmtDecoder, ArmtEncoder),
	Arch.x86: (BCJDecoder, BCJEncoder),
	Arch.sparc: (SparcDecoder, SparcEncoder),
	Arch.ppc: (PpcDecoder, PpcEncoder),
}


class BCJ(KaitaiCompressor):
	__slots__ = ("encoderCtor", "decoderCtor")

	def __init__(self, arch: Arch, *args, **kwargs) -> None:  # pylint:disable=unused-argument
		super().__init__()
		if isinstance(arch, str):
			arch = Arch[arch]
		elif isinstance(arch, int):
			arch = Arch(arch)

		self.decoderCtor, self.encoderCtor = _archs[arch]

	def process(self, data: typing.Union[bytes, bytearray]) -> ProcessorContextStub:
		d = self.decoderCtor(len(data))
		return ProcessorContextStub(d.decode(data))

	def unprocess(self, data: typing.Union[bytes, bytearray]) -> ProcessorContextStub:
		e = self.encoderCtor()
		return ProcessorContextStub(e.encode(data))
