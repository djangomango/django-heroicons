# Django-Heroicons

Render Heroicons (outline, solid, mini, and micro) SVG icons directly in Django and Jinja templates.

---

## Installation

```bash
pip install git+https://github.com/djangomango/django-heroicons.git@0.1.0
```

Or add to your `requirements.txt`:

```txt
git+https://github.com/djangomango/django-heroicons.git@0.1.0
```

Add `django_heroicons` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    "django_heroicons",
    ...
]
```

---

## Usage

### 1. Template Tag Loading

Load the template tags at the top of your Django template:

```html
{% load django_heroicons %}
```

Or make the tags globally available across all templates by adding them to `builtins` in `settings.py`:

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "OPTIONS": {
            "builtins": [
                "django_heroicons.templatetags.heroicons",
            ],
        },
    }
]
```

### 2. Available Tags

The library provides four tags matching the Heroicon styles:

- `heroicon_outline` (24x24 outline stroke)
- `heroicon_solid` (24x24 solid fill)
- `heroicon_mini` (20x20 solid fill)
- `heroicon_micro` (16x16 solid fill)

### 3. Examples

```html
<!-- Default outline icon -->
{% heroicon_outline "academic-cap" %}

<!-- Custom size and CSS classes -->
{% heroicon_solid "academic-cap" size=40 class="w-10 h-10 text-blue-600" %}

<!-- Mini icon with custom attributes -->
{% heroicon_mini "check-circle" class="w-5 h-5 text-green-500" data_testid="status-check" %}
```

### 4. Migration CLI

To migrate templates from Heroicons v1 icon names to v2:

```bash
python -m heroicons update templates/**/*.html
```

---

## License & Credits

- Licensed under the **MIT License**.
- Icon designs by [Tailwind Labs](https://heroicons.com/).
- Originally created by [Adam Johnson](https://github.com/adamchainz/django-heroicons).
