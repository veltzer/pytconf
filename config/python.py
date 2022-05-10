import config.project

package_name = config.project.project_name

dev_requires = [
    "pypitools",
    "pyclassifiers",
    "black",
]
install_requires = [
    "termcolor",
    "yattag",
    "pyfakeuse",
]
test_requires = [
    "Sphinx",
    "pymakehelper",
    "pydmt",
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "pyflakes",
    "pylogconf",
]

python_requires = ">=3.10"

test_os = ["ubuntu-22.04"]
test_python = ["3.10"]
