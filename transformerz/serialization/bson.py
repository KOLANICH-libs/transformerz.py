__all__ = ("bsonSerializer", "bsonSerializableTypes")
from bson import BSON  # pymongo

from ..core import FileTransformer

bsonSerializableTypes = (list, dict)
bsonSerializer = FileTransformer("bson", BSON.encode, BSON.decode, bytes, bsonSerializableTypes, "bson", "application/bson")
