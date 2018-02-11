import setuptools

import pyconf.version

setuptools.setup(
    name='pyconf',
    version=pyconf.version.version_str,
    description='pyconf handles configuration, config files and command line parsing',
    long_description='pyconf handles configuration, config files and command line parsing',
    url='https://veltzer.github.io/pyconf',
    download_url='https://github.com/veltzer/pyconf',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    maintainer='Mark Veltzer',
    maintainer_email='mark.veltzer@gmail.com',
    license='MIT',
    platforms=['python'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='click argparse optparse command lineparsing',
    packages=setuptools.find_packages(),
    install_requires=[
        'enum',  # for Enum
    ],
)
