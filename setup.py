
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(name='convergence',
      version='0.1.1',
      description=('A Python program to Perform Calculations Associated with '
                   'a Grid Convergence Study'),
      long_description=README,
      long_description_content_type='text/markdown',
      license = "GPLv3",
      author='Mathew Topper',
      author_email='dataonlygreater@gmail.com',
      url='https://github.com/H0R5E/convergence',
      packages=['convergence'],
      python_requires='>=2.7, !=3.9.*, <4',
      extras_require={
        'test': ["pytest", "pytest-cov"]},
      entry_points = {'console_scripts': 
                           ['grid-convergence = convergence:main']},
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering"],
      )
