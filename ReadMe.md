transformerz.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
===============
~~[wheel (from GHA via `nightly.link`)](https://nightly.link/KOLANICH-libs/transformerz.py/workflows/CI/master/transformerz-0.CI-py3-none-any.whl)~~
~~![GitLab Build Status](https://gitlab.com/KOLANICH/transformerz.py/badges/master/pipeline.svg)~~
~~[![GitHub Actions](https://github.com/KOLANICH-libs/transformerz.py/workflows/CI/badge.svg)](https://github.com/KOLANICH-libs/transformerz.py/actions)~~
~~![GitLab Coverage](https://gitlab.com/KOLANICH/transformerz.py/badges/master/coverage.svg)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-libs/transformerz.py.svg)](https://libraries.io/github/KOLANICH-libs/transformerz.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

**We have moved to https://codeberg.org/KOLANICH-libs/transformerz.py, grab new versions there.**

Under the disguise of "better security" Micro$oft-owned GitHub has [discriminated users of 1FA passwords](https://github.blog/2023-03-09-raising-the-bar-for-software-security-github-2fa-begins-march-13/) while having commercial interest in success and wide adoption of [FIDO 1FA specifications](https://fidoalliance.org/specifications/download/) and [Windows Hello implementation](https://support.microsoft.com/en-us/windows/passkeys-in-windows-301c8944-5ea2-452b-9886-97e4d2ef4422) which [it promotes as a replacement for passwords](https://github.blog/2023-07-12-introducing-passwordless-authentication-on-github-com/). It will result in dire consequencies and is competely inacceptable, [read why](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

If you don't want to participate in harming yourself, it is recommended to follow the lead and migrate somewhere away of GitHub and Micro$oft. Here is [the list of alternatives and rationales to do it](https://github.com/orgs/community/discussions/49869). If they delete the discussion, there are certain well-known places where you can get a copy of it. [Read why you should also leave GitHub](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

---

Just a set of composable processor objects that can be stacked, and path can be automatically routed.

Each class/object has 2 members of type `type`:

* `tgtType`
* `srcType`

and 2 functions

* `process` - converts a value of `srcType` to the `tgtType`. Should parse the data from the representation useful for storing on disk.
* `unprocess` - converts a value of  `tgtType` to `srcType` Should serialize the data from the representation useful for storing on disk.
.

The names of functions are inherited from `kaitai.process` library (Kaitai Struct is a parsing framework, so `process` historically means parsing), so are some classes (and I hope to get the stuff from this package merged supported by KS somewhen).

There are 3 base classes:

* `TransformerBase` - for objects with `srcType` and `tgtType` hardcoded in class definitions or available as props
* `Transformer` - for objects with `srcType` and `tgtType` stored in slots
* `FileTransformer` - for transformations when `unprocess`ed form can be stored in a file with a well-known extension and possible MIME type.
* `BinaryProcessor` - adapter for Kaitai Struct stuff


There are transformers are of different types and reside in different submodules:

* `.serialization` - packages to serialize various objects
	* `.json.jsonSerializer` -  Uses `ujson` if it is available which is faster than built-in `json` module.
	* `.bson.bsonSerializer` - Available if `pymongo` is installed.
	* `.msgpack.msgpackSerializer` - Available if a package for MsgPack serialization is installed.
	* `.cbor.cborSerializer` - Available packages for CBOR serialization: either `cbor` or `cbor2` - are installed.
	* `.pon.ponSerializer` - "Python Object Nonation" - stuff like JSON that can be safely evaluated using `literal_eval`
* `.processors` - process binary data. This module contains the adapters allowing to use the stuff written to be used in `process` attr in Kaitai Struct specs.
* `.compression` - packages to compress binary data. Take various params.
* `.text` - convert text to bytes and back
* `.struct` - parses data to tuples and back using `struct.Struct`. Numbers binary representations also go here. But not all. Some cannot be parsed by `struct`, so they go to ...
* `.numpy` - parsing and serializing arrays of numbers using `numpy` machinery. Mostly needed for IEEE 751 floats not built into python.

Tutorial
--------

The tutorial is available. [`tutorial.ipynb`](./tutorial.ipynb) [![NBViewer](https://nbviewer.org/static/ico/ipynb_icon_16x16.png)](https://nbviewer.org/urls/codeberg.org/KOLANICH-libs/transformerz.py/raw/master/tutorial.ipynb)
