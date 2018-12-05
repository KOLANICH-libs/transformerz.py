import datetime
import subprocess
import typing

import polib

from ..core import FileTransformer


def dictToPo(dic: typing.Mapping[str, str]) -> polib.POFile:
	poF = polib.POFile(encoding="utf-8")

	dt = str(datetime.datetime.now(tz=datetime.timezone.utc))
	poF.metadata.update(
		{
			"Project-Id-Version": "emojifilt",
			"POT-Creation-Date": dt,
			"PO-Revision-Date": dt,
			"Language": "emoji",
			"Content-Type": "text/plain; charset=UTF-8",
		}
	)

	for k, v in dic.items():
		poF.append(polib.POEntry(msgid=k, msgstr=v))

	poF.sort()
	return poF


def dumpPo(dic: typing.Mapping[str, str]):
	return str(dictToPo(dic))


def compileMoToPo(poSource: str) -> bytes:
	"""`polib` built-in compilation doesn't create a hashtable"""
	return bytes(subprocess.run(["msgfmt", "-o", "-", "-"], input=poSource.encode("utf-8"), capture_output=True).stdout)


def dumpMoWithHashtable(dic: typing.Mapping[str, str]) -> bytes:
	return compileMoToPo(dumpPo(dic))


poSerializer = FileTransformer("libintl_po", dumpPo, None, str, typing.Mapping[str, str], "po")
moSerializerWithHashtable = FileTransformer("libintl_mo_with_hashtable", dumpMoWithHashtable, None, bytes, typing.Mapping[str, str], "mo")
