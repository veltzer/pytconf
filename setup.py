import setuptools

"""
The documentation can be found at:
http://setuptools.readthedocs.io/en/latest/setuptools.html
"""
setuptools.setup(
    # the first three fields are a must according to the documentation
    name='pyconf',
    version='0.0.1',
    packages=[
        'pyconf',
    ],
    # from here all is optional
    description='pyconf handles configuration, config files and command line parsing',
    long_description='pyconf handles configuration, config files and command line parsing',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    maintainer='Mark Veltzer',
    maintainer_email='mark.veltzer@gmail.com',
    keywords=[
        'click',
        'argparse',
        'optparse',
        'command-line-parser',
        'configuration',
    ],
    url='https://veltzer.github.io/pyconf',
    download_url='https://github.com/veltzer/pyconf',
    license='MIT',
    platforms=[
        'python2',
    ],
    install_requires=[
        'enum34',
        'termcolor',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    data_files=[
    ],
    entry_points={'console_scripts': [
    ]},
    python_requires='>=2.7',
)
