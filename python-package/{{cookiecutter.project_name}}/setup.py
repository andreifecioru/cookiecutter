from setuptools import setup, find_packages

import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
REQUIREMENTS = (HERE / "requirements.txt").read_text()


def requires():
    return [requirement for requirement in REQUIREMENTS.split("\n") if requirement]


if __name__ == "__main__":
    setup(
        name="{{cookiecutter.package.name}}",
        version="0.0.1",

        description="{{cookiecutter.package.description}}",
        long_description=README,
        long_description_content_type="text/markdown",

        author="{{cookiecutter.author.name}}",
        author_email="{{cookiecutter.author.email}}",

        package_dir={"": "."},
        packages=find_packages("."),

        scripts=["{{cookiecutter.package.name}}/scripts/{{cookiecutter.package.cli_script}}"],

        install_requires=requires(),

        license="Proprietary",
        url="https://git.corp.adobe.com/AAM/keystone"
    )
