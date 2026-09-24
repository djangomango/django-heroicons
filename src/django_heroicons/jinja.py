from typing import Any

from markupsafe import Markup

import django_heroicons


def heroicon_micro(name: str, *, size: int | None = 16, **attrs: Any) -> Markup:
    """Render a 16x16 micro heroicon for Jinja templates."""
    return _render_icon("micro", name, size, **attrs)


def heroicon_mini(name: str, *, size: int | None = 20, **attrs: Any) -> Markup:
    """Render a 20x20 mini heroicon for Jinja templates."""
    return _render_icon("mini", name, size, **attrs)


def heroicon_outline(name: str, *, size: int | None = 24, **attrs: Any) -> Markup:
    """Render a 24x24 outline heroicon for Jinja templates."""
    return _render_icon("outline", name, size, **attrs)


def heroicon_solid(name: str, *, size: int | None = 24, **attrs: Any) -> Markup:
    """Render a 24x24 solid heroicon for Jinja templates."""
    return _render_icon("solid", name, size, **attrs)


def _render_icon(icon_style: str, name: str, size: int | None, **attrs: Any) -> Markup:
    """Render markup-safe heroicon string for Jinja templates."""
    return Markup(django_heroicons._render_icon(icon_style, name, size, **attrs))
