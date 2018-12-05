__all__ = ("bencodeSerializer",)

import typing

try:
	import bencode
except ImportError:
	import bencodepy as bencode

from ..core import FileTransformer

bencodeSerializableTypes = (int, list, dict, bytes)

bencodeSerializer = FileTransformer("bencode", bencode.encode, bencode.decode, bytes, bencodeSerializableTypes, "bencode")
