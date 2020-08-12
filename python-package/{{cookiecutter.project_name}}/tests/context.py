import sys
from pathlib import Path

HERE: Path = Path(__file__).parent.parent
sys.path.append(HERE.absolute().as_posix())

import {{cookiecutter.package.name}} # noqa # pylint: disable=unused-import, wrong-import-position
