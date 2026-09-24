from django import template

from .heroicons import (
    heroicon_micro,
    heroicon_mini,
    heroicon_outline,
    heroicon_solid,
)

register = template.Library()

register.simple_tag(heroicon_micro, name="heroicon_micro")
register.simple_tag(heroicon_mini, name="heroicon_mini")
register.simple_tag(heroicon_outline, name="heroicon_outline")
register.simple_tag(heroicon_solid, name="heroicon_solid")
