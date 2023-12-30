from typing import List


config_requires: List[str] = []
dev_requires: List[str] = [
    "pypitools",
    "black",
]
install_requires: List[str] = [
    "termcolor",
    "yattag",
]
make_requires: List[str] = [
    "pyclassifiers",
    "sphinx",
    "pymakehelper",
    "pydmt",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "pyflakes",
    "mypy",
    "pylogconf",
    "types-termcolor",
    "types-PyYAML",
]
requires = config_requires + install_requires + make_requires + test_requires
