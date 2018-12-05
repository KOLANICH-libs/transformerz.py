__all__ = ("jsonSerializer", "jsonFancySerializer")

import json as jsonFancy
import typing

try:
	import ujson as json
except ImportError:
	json = jsonFancy

from ..core import FileTransformer
from . import NoneType, jsonSerializableTypes

jsonSerializer = FileTransformer("json", json.dumps, json.loads, str, jsonSerializableTypes, "json", "application/json")


def fancyJSONSerialize(v: typing.Union[jsonSerializableTypes]) -> str:
	return jsonFancy.dumps(v, indent="\t")


jsonFancySerializer = FileTransformer("json", fancyJSONSerialize, json.loads, str, jsonSerializableTypes, "json")
