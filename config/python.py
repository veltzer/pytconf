import config.project

package_name = config.project.project_name

console_scripts = []

setup_requires = []

run_requires = [
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
test_os = "[ubuntu-16.04, ubuntu-18.04, ubuntu-20.04]"
test_python = "[3.6, 3.7, 3.8]"
test_container = "[ 'ubuntu:18.04', 'ubuntu:20.04' ]"
