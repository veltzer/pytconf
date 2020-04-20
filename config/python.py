import config.project

package_name = config.project.project_name

console_scripts = [
]

setup_requires = [
]

run_requires = [
    'termcolor',  # for printing in colors
    'yattag',  # for generating html text
]

test_requires = [
    'pylogconf',  # for nicer logging
]

dev_requires = [
    'pyclassifiers',  # for programmatic classifiers
    'pypitools',  # for upload etc
    'pydmt',  # for building
    'Sphinx',  # for the sphinx builder
    'pylint',  # to check for lint errors
    'pytest',  # for testing
]

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=3.4"
