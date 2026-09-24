from typing import Any

from django import template
from django.utils.safestring import SafeString, mark_safe

import django_heroicons

register = template.Library()


@register.simple_tag
def heroicon_micro(name: str, *, size: int | None = 16, **kwargs: Any) -> SafeString:
    """Render a 16x16 micro heroicon."""
    return _render_icon("micro", name, size, **kwargs)


@register.simple_tag
def heroicon_mini(name: str, *, size: int | None = 20, **kwargs: Any) -> SafeString:
    """Render a 20x20 mini heroicon."""
    return _render_icon("mini", name, size, **kwargs)


@register.simple_tag
def heroicon_outline(name: str, *, size: int | None = 24, **kwargs: Any) -> SafeString:
    """Render a 24x24 outline heroicon."""
    return _render_icon("outline", name, size, **kwargs)


@register.simple_tag
def heroicon_solid(name: str, *, size: int | None = 24, **kwargs: Any) -> SafeString:
    """Render a 24x24 solid heroicon."""
    return _render_icon("solid", name, size, **kwargs)


def _render_icon(icon_style: str, name: str, size: int | None, **kwargs: Any) -> SafeString:
    """Render heroicon HTML markup with clean string keyword arguments."""
    fixed_kwargs = {key: (value + "" if isinstance(value, SafeString) else value) for key, value in kwargs.items()}
    return mark_safe(django_heroicons._render_icon(icon_style, name, size, **fixed_kwargs))
