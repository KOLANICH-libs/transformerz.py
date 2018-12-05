__all__ = ("jsonSerializer", "jsonFancySerializer")

import json as jsonFancy
import typing

try:
	import mujson as json
except ImportError:
	try:
		import ujson as json
	except ImportError:
		json = jsonFancy

from ..core import FileTransformer
from . import NoneType, jsonSerializableTypes

dumps = json.dumps

if isinstance(dumps("1"), bytes):

	def dumps(*args, **kwargs):
		return json.dumps(*args, **kwargs).decode("utf-8")

	dumps.__wraps__ = json.dumps


jsonSerializer = FileTransformer("json", dumps, json.loads, str, jsonSerializableTypes, "json", "application/json")


def fancyJSONSerialize(v: typing.Union[jsonSerializableTypes]) -> str:
	return jsonFancy.dumps(v, indent="\t", ensure_ascii=False)


jsonFancySerializer = FileTransformer("json:fancy", fancyJSONSerialize, json.loads, str, jsonSerializableTypes, "json", "application/json")
