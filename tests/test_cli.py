from pathlib import Path
from typing import Any

import pytest

from django_heroicons import __main__  # noqa: F401
from django_heroicons.cli import main


def test_no_subcommand(capsys: Any) -> None:
    """Test CLI invocation with no subcommand exits with code 2."""
    with pytest.raises(SystemExit) as excinfo:
        main([])

    assert excinfo.value.code == 2
    out, err = capsys.readouterr()
    assert err == (
        "usage: __main__.py [-h] {update} ...\n" + "__main__.py: error: the following arguments are required: command\n"
    )
    assert out == ""


def test_help() -> None:
    """Test CLI help flag exits with code 0."""
    with pytest.raises(SystemExit) as excinfo:
        main(["--help"])

    assert excinfo.value.code == 0


def test_update_no_files(capsys: Any) -> None:
    """Test update command without file arguments exits with code 2."""
    with pytest.raises(SystemExit) as excinfo:
        main(["update"])

    assert excinfo.value.code == 2
    out, err = capsys.readouterr()
    assert err == (
        "usage: __main__.py update [-h] file [file ...]\n"
        + "__main__.py update: error: the following arguments are required: file\n"
    )
    assert out == ""


def test_update_empty(capsys: Any, tmp_path: Path) -> None:
    """Test update command on empty template file."""
    path = tmp_path / "example.html"
    path.write_text("")

    result = main(["update", str(path)])

    assert result == 0
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
    assert path.read_text() == ""


def test_update_django_no_rename(capsys: Any, tmp_path: Path) -> None:
    """Test template file requiring no renaming remains unmodified."""
    path = tmp_path / "example.html"
    source = '{% heroicon_outline "academic-cap" stroke_width=1' + ' data_controller="academia" %}\n'
    path.write_text(source)

    result = main(["update", str(path)])

    assert result == 0
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
    assert path.read_text() == source


def test_update_django_simple(capsys: Any, tmp_path: Path) -> None:
    """Test rewriting single heroicon outline name."""
    path = tmp_path / "example.html"
    path.write_text('{% heroicon_outline "adjustments" %}\n')

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert path.read_text() == '{% heroicon_outline "adjustments-vertical" %}\n'


def test_update_django_single_quotes(capsys: Any, tmp_path: Path) -> None:
    """Test rewriting single-quoted heroicon name."""
    path = tmp_path / "example.html"
    path.write_text("{% heroicon_outline 'archive' %}\n")

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert path.read_text() == "{% heroicon_outline 'archive-box' %}\n"


def test_update_django_solid(capsys: Any, tmp_path: Path) -> None:
    """Test rewriting solid heroicon name."""
    path = tmp_path / "example.html"
    path.write_text("{% heroicon_solid 'archive' %}\n")

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert path.read_text() == "{% heroicon_solid 'archive-box' %}\n"


def test_update_django_arguments(capsys: Any, tmp_path: Path) -> None:
    """Test rewriting heroicon tag with arguments."""
    path = tmp_path / "example.html"
    path.write_text('{% heroicon_outline "adjustments" stroke_width=1 data_year="2022" %}\n')

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert path.read_text() == ('{% heroicon_outline "adjustments-vertical" stroke_width=1' + ' data_year="2022" %}\n')


def test_update_django_no_space(capsys: Any, tmp_path: Path) -> None:
    """Test rewriting heroicon tag with no whitespace."""
    path = tmp_path / "example.html"
    path.write_text('{%heroicon_outline "adjustments"%}\n')

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert path.read_text() == '{%heroicon_outline "adjustments-vertical"%}\n'


def test_update_django_extra_space(capsys: Any, tmp_path: Path) -> None:
    """Test rewriting heroicon tag with extra whitespace."""
    path = tmp_path / "example.html"
    path.write_text('{%   heroicon_outline   "adjustments"   %}\n')

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert path.read_text() == '{%   heroicon_outline   "adjustments-vertical"   %}\n'
