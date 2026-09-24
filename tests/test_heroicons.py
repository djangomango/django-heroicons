from xml.etree import ElementTree

import pytest

import django_heroicons


def test_load_icon_success_outline() -> None:
    """Test loading outline icon element."""
    svg = django_heroicons._load_icon("outline", "academic-cap")
    assert isinstance(svg, ElementTree.Element)
    assert svg.tag == ElementTree.QName("svg")


def test_load_icon_success_solid() -> None:
    """Test loading solid icon element."""
    svg = django_heroicons._load_icon("solid", "academic-cap")
    assert isinstance(svg, ElementTree.Element)
    assert svg.tag == ElementTree.QName("svg")


def test_load_icon_success_mini() -> None:
    """Test loading mini icon element."""
    svg = django_heroicons._load_icon("mini", "academic-cap")
    assert isinstance(svg, ElementTree.Element)
    assert svg.tag == ElementTree.QName("svg")


def test_load_icon_fail_unknown() -> None:
    """Test exception raised when loading nonexistent icon."""
    with pytest.raises(django_heroicons.IconDoesNotExist) as excinfo:
        django_heroicons._load_icon("solid", "hoome")

    assert excinfo.value.args == ("The icon 'hoome' with style 'solid' does not exist.",)
