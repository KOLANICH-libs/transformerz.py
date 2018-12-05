__all__ = ("yamlSerializer", "parseYAML")

import re
import typing
from io import StringIO

from ruamel.yaml import YAML

from ..core import FileTransformer
from . import jsonSerializableTypes

leadingTabsRx = re.compile("^( *)(\\t+)")
parser = YAML(typ="safe")


def _tabbedYaml2YamlReplacer(m):
	return m.group(1) + "  " * len(m.group(2))


def _tabbedYaml2Yaml(text: str) -> typing.Iterator[str]:
	for line in text.splitlines():
		yield leadingTabsRx.sub(_tabbedYaml2YamlReplacer, line)


def tabbedYaml2Yaml(text: str) -> str:
	"""Allows tabs to be used in YAML"""
	return "\n".join(_tabbedYaml2Yaml(text))


def parseYAML(text: str) -> typing.Mapping[str, typing.Any]:
	"""Just parses YAML."""
	return parser.load(tabbedYaml2Yaml(text))


def dumpYaml(o: typing.Any) -> str:
	yamlDumper = YAML(typ="rt")
	yamlDumper.indent(mapping=2, sequence=4, offset=2)
	yamlDumper.representer.represent_omap = lambda tag, omap: yamlDumper.representer.represent_dict(omap)
	with StringIO() as s:
		yamlDumper.dump(o, s)
		return s.getvalue()


yamlSerializer = FileTransformer("yaml", dumpYaml, parseYAML, str, jsonSerializableTypes, "yaml", None)
