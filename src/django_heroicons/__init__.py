import functools
import importlib.resources
from contextlib import closing
from copy import deepcopy
from xml.etree import ElementTree
from zipfile import ZipFile

__version__ = "0.1.0"


class IconDoesNotExist(Exception):
    """Raised when the requested heroicon or style does not exist."""


@functools.lru_cache(maxsize=128)
def _load_icon(style: str, name: str) -> ElementTree.Element:
    """Load and parse SVG element from the bundled heroicons zip archive."""
    zip_resource = importlib.resources.files("django_heroicons") / "heroicons.zip"
    with zip_resource.open("rb") as zip_data, closing(zip_data), ZipFile(zip_data, "r") as zip_file:
        try:
            svg_bytes = zip_file.read(f"{style}/{name}.svg")
        except KeyError:
            raise IconDoesNotExist(f"The icon {name!r} with style {style!r} does not exist.") from None

        svg = ElementTree.fromstring(svg_bytes.decode())
        for node in svg.iter():
            node.tag = ElementTree.QName(node.tag.removeprefix("{http://www.w3.org/2000/svg}"))
        return svg


_PATH_ATTR_NAMES = frozenset(
    {
        "stroke-linecap",
        "stroke-linejoin",
        "vector-effect",
    }
)


def _render_icon(icon_style: str, name: str, size: int | None, **kwargs: object) -> str:
    """Render inline SVG string with applied style, dimensions, and HTML attributes."""
    svg = deepcopy(_load_icon(icon_style, name))
    if size is not None:
        svg.attrib["width"] = svg.attrib["height"] = str(size)

    svg_attrs: dict[str, str] = {}
    path_attrs: dict[str, str] = {}
    for raw_name, value in kwargs.items():
        attr_name = raw_name.replace("_", "-")
        if attr_name in _PATH_ATTR_NAMES:
            path_attrs[attr_name] = str(value)
        else:
            svg_attrs[attr_name] = str(value)

    svg.attrib.update(svg_attrs)
    if path_attrs:
        for path in svg.findall("path"):
            path.attrib.update(path_attrs)

    string = ElementTree.tostring(svg, encoding="unicode")
    return string.replace(' xmlns="http://www.w3.org/2000/svg"', "", 1)
