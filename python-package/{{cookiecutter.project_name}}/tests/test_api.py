from .context import {{cookiecutter.package.name}}
from {{cookiecutter.package.name}}.api import math


def test_api_math_sum() -> None:
    result = math.sum(1, 2)
    assert result == 3