__all__ = ("jsonSerializer", "jsonFancySerializer")

import typing

import hcl2

from ..core import FileTransformer
from . import NoneType, jsonSerializableTypes


def serializeHCL2(v: typing.Union[jsonSerializableTypes]) -> str:
	raise NotImplementedError


hcl2Serializer = FileTransformer("hcl2", serializeHCL2, hcl2.loads, str, jsonSerializableTypes, "tf")
