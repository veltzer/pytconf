import config.project

package_name = config.project.project_name

console_scripts = []

setup_requires = []

run_requires = [
    "termcolor",
    "yattag",
]

test_requires = [
    "pymakehelper",
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "pylogconf",
]

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

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=3.6"

extras_require = {
}
