#!/usr/bin/env python
#
# Anagram Matcher
# License: MIT

try:
	from setuptools import setup
	setup_kwargs = {'entry_points': {'console_scripts':['anagram=anagram.anagram:__main__']}}
except ImportError:
	from distutils.core import setup
	setup_kwargs = {'scripts': ['bin/anagram']}

from anagram import __version__

def readme():
	with open('README.rst') as f:
		return f.read()

with open('requirements.txt') as fid:
	INSTALL_REQUIRES = [l.strip() for l in fid.readlines() if l]

with open('requirements-dev.txt') as fid:
	TEST_REQUIRES = [l.strip() for l in fid.readlines() if l]

setup(
	name='anagram',
	version=__version__,
	description='A basic anagram matching utility, group like words in ' +
	'dictionaries and wordlists',
	long_description=readme(),
	author='Nathan Casler',
	author_email='npcasler@gmail.com',
	url='https://github.com/npcasler/anagram',
	packages=['anagram'],
	include_package_data=True,
	license='MIT',
	platforms='Posix; MacOS X',
	install_requires=INSTALL_REQUIRES,
	test_suite='nose.collector',
	tests_require=TEST_REQUIRES,
	**setup_kwargs
)
