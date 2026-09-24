from collections.abc import Callable
from importlib.resources import files
from typing import IO


def open_binary(pkg: str, filename: str) -> IO[bytes]:
    """Open bundled binary resource file from package."""
    return (files(pkg) / filename).open("rb")


str_removeprefix: Callable[[str, str], str] = str.removeprefix
