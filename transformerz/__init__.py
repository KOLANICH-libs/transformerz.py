import typing


from warnings import warn

warn("We have moved from M$ GitHub to https://codeberg.org/KOLANICH-libs/transformerz.py , read why on https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo .")


from .core import TransformerMirroringTgtType


class DummyTransformer(TransformerMirroringTgtType):
	"""Does nothing"""

	__slots__ = ("tgtType",)

	def __init__(self, name: str, tgtType: type) -> None:
		self.tgtType = tgtType
		super().__init__(name)

	def unprocess(self, v: typing.Any) -> typing.Any:
		return v

	def process(self, v: typing.Any) -> typing.Any:
		return v


dummyTransformer = DummyTransformer("dummy", object)
