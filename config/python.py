import config.project

package_name = config.project.project_name

console_scripts = [
]

setup_requires = [
]

run_requires = [
    'enum34',  # for Enum
    'termcolor',  # for printing in colors
]

dev_requires = [
#    'pyclassifiers',  # for programmatic classifiers
#    'pypitools',  # for upload etc
#    'pydmt',  # for building
#    'Sphinx',  # for the sphinx builder
]

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=2.7"
