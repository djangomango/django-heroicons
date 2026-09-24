from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="django-heroicons",
    version="0.1.0",
    author="Adam Johnson",
    author_email="me@adamj.eu",
    maintainer="buswedg",
    maintainer_email="buswedg@djangomango.com",
    url="https://github.com/djangomango/django-heroicons/",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    package_data={
        "django_heroicons": ["heroicons.zip"],
    },
    include_package_data=True,
    install_requires=[
        "Django>=4.2",
    ],
    license="MIT",
    description="Use heroicons in your Django and Jinja templates.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Framework :: Django",
    ],
    python_requires=">=3.10",
)
