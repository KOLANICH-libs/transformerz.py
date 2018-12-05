__all__ = ("plistSerializer",)
from functools import partial
from plistlib import FMT_BINARY, FMT_XML, dumps, loads

from ..core import FileTransformer
from . import jsonSerializableTypes

plistSerializerXML = FileTransformer("plist", partial(dumps, fmt=FMT_XML, sort_keys=True, skipkeys=False), partial(loads, fmt=FMT_XML, dict_type=dict), bytes, jsonSerializableTypes, "plist", "application/x-plist")
plistSerializerBinary = FileTransformer("plist", partial(dumps, fmt=FMT_BINARY, sort_keys=True, skipkeys=False), partial(loads, fmt=FMT_BINARY, dict_type=dict), bytes, jsonSerializableTypes, "plist", "application/x-plist")
plistSerializer = plistSerializerBinary
