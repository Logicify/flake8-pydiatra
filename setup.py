#    Pydiatra plugin for flake8.
#    Copyright (C) 2019 Kirill Malyshev
#    The MIT License (MIT)
#    
#    Permission is hereby granted, free of charge, to any person obtaining
#    a copy of this software and associated documentation files
#    (the "Software"), to deal in the Software without restriction,
#    including without limitation the rights to use, copy, modify, merge,
#    publish, distribute, sublicense, and/or sell copies of the Software,
#    and to permit persons to whom the Software is furnished to do so,
#    subject to the following conditions:
#    
#    The above copyright notice and this permission notice shall be
#    included in all copies or substantial portions of the Software.
#    
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import io
import re
from distutils.cmd import Command

import setuptools


def get_version(filename):
    with open(filename, "r") as fp:
        contents = fp.read()
    return re.search(r"__version__ = ['\"]([^'\"]+)['\"]", contents).group(1)


def get_readme():
    with io.open('README.md', encoding='ASCII') as file:
        return file.read()


class UpdateCopyrightCommand(Command):
    """
    Command to update source files copyright headers.
    """
    description = 'update source files copyright headers'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import copyright
        copyright.App.main(['-c', 'development/copyright.json', '.'])


if __name__ == '__main__':
    setuptools.setup(
        name='flake8-pydiatra',
        version=get_version('flake8_pydiatra.py'),
        description='flake8 integration for pydiatra code analyzer',
        long_description=get_readme(),
        long_description_content_type='text/markdown',
        url='https://github.com/Logicify/flake8-pydiatra',
        license='MIT',
        author='Kirill Malyshev',
        install_requires=[
            'flake8>3.0.0',
            'pydiatra<1',
        ],
        extras_require={
            'dev': ['copyright'],
        },
        python_requires='>=3.5',
        py_modules=['flake8_pydiatra'],
        entry_points={
            "flake8.extension": ["PYD0 = flake8_pydiatra:PydiatraChecker"]
        },
        cmdclass={
            'copyright': UpdateCopyrightCommand,
        },
        classifiers=[
            "Framework :: Flake8",
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Topic :: Software Development :: Quality Assurance',
        ],
    )
