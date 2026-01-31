"""
Config for sphinx
"""

import os
import sys
from pydmt.helpers.signature import get_copyright_years_long
import config.project
import config.personal
import config.version

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
]

# Add the projects "src" directory to the Python path.
# This allows Sphinx to find and import your package.
sys.path.insert(0, os.path.abspath("../src"))
sys.path.insert(0, os.path.abspath(".."))

# Treat all warnings as errors.
# This can also be set by passing the -W flag to the sphinx-build command.
warning_is_error = True

# Enable "nit-picky mode". This will issue warnings for all missing
# cross-references (e.g., a link to a class that doesnt exist).
# nitpicky = True

project = config.project.name
author = config.personal.fullname
project_copyright = get_copyright_years_long(repo="..")+" "+author
version = ".".join(str(x) for x in config.version.tup)
release = ".".join(str(x) for x in config.version.tup)

html_theme_options = {
        "show_powered_by": False,
}
# allow us to use |project| in our snipplets and rst files
rst_epilog = f"""
.. |project| replace:: {project}
"""
# title without a version
html_title = f"{project} Documentation"
# This is the default
# html_title = "%s %s Documentation" % (project, version)
