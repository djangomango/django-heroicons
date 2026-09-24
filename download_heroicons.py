import argparse
import subprocess
from io import BytesIO
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def main(argv: list[str] | None = None) -> int:
    """Download and optimize heroicons bundle from GitHub release."""
    parser = argparse.ArgumentParser()
    parser.add_argument("version", help="dotted version number")
    args = parser.parse_args(argv)
    version: str = args.version

    proc = subprocess.run(
        [
            "curl",
            "--fail",
            "--location",
            f"https://github.com/tailwindlabs/heroicons/archive/v{version}.zip",
        ],
        stdout=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        raise SystemExit(1)

    input_zip = ZipFile(BytesIO(proc.stdout))
    input_prefix = f"django_heroicons-{version}/optimized/"

    output_path = Path("src/django_heroicons/heroicons.zip")
    if output_path.exists():
        output_path.unlink()

    with ZipFile(output_path, "w", compression=ZIP_DEFLATED, compresslevel=9) as output_zip:
        for name in sorted(input_zip.namelist()):
            if name.startswith(input_prefix) and name.endswith(".svg"):
                info = input_zip.getinfo(name)
                data = input_zip.read(name).replace(b' data-slot="icon"', b"")

                new_name = rename_file(name[len(input_prefix) :])

                info.filename = new_name
                output_zip.writestr(info, data)
                print(new_name)

    print("\nWritten!")
    return 0


def rename_file(filename: str) -> str:
    """Map release archive icon paths to standard style folder paths."""
    if filename.startswith("24/solid") or filename.startswith("24/outline"):
        return filename[len("24/") :]
    elif filename.startswith("20/solid"):
        return f"mini{filename[len('20/solid') :]}"
    elif filename.startswith("16/solid"):
        return f"micro{filename[len('16/solid') :]}"
    else:
        raise ValueError(f"Unknown filename {filename!r}")


if __name__ == "__main__":
    raise SystemExit(main())
