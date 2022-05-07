import config.project

package_name = config.project.project_name

dev_requires = [
    "pyclassifiers",
    "pypitools",
    "pydmt",
    "Sphinx",
    "pytest",
    "pytest-cov",
    "pylint",
    "pyflakes",
    "flake8",
    "black",
]
install_requires = [
    "termcolor",
    "yattag",
    "pyfakeuse",
]
test_requires = [
    "pymakehelper",
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "pylogconf",
]

python_requires = ">=3.10"

test_os = ["ubuntu-22.04"]
test_python = ["3.10"]
