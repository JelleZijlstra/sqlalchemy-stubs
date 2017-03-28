# sqlalchemy-stubs

## About

This repository contains external type annotations (see
[PEP 484](https://www.python.org/dev/peps/pep-0484/)) for the
[SQLAlchemy](https://www.sqlalchemy.org/) package. Such type annotations are normally included
in [typeshed](https://www.github.com/python/typeshed), but SQLAlchemy's annotations were
frequently problematic and have therefore been deleted from typeshed. This repo provides SQLAlchemy
stubs with some issues fixed for those who find them useful. Hopefully it can eventually be merged
back into typeshed.

## Usage

To use these stubs, clone this repo and point your type checker to it. For example, to use them in
[mypy](http://github.com/python/mypy), you can set the `$MYPYPATH` environment variable or set
`mypy_path = /path/to/sqlalchemy-stubs` in your `mypy.ini`.

## Contributing

Contributions should follow the same style guidelines as
[typeshed](https://github.com/python/typeshed/blob/master/CONTRIBUTING.md).

## Git history

The early git history of this repo contains commits from typeshed, filtered to only changes that
affect typeshed (using `git filter-branch`). The SQLAlchemy stubs were moved around a few times
(from third_party/2.7 to third_party/2 to third_party/2and3), and commits from all of these
locations are included.

## Authors

This repository was created by Jelle Zijlstra. Numerous others have contributed to the
SQLAlchemy stubs; see the git history for details.

## TODOs

- Provide testing (both a local test script and a Travis setup)
- Document why the SQLAlchemy stubs were deleted
- Maybe provide an automated installation script. (For example, I think we could make a pip package
  that depends on mypy and installs these stubs inside mypy's copy of typeshed. Or we could wait
  for mypy to provide a standardized way to add third-party stubs.)
