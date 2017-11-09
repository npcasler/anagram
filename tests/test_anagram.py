# Anagram Utility
# License: MIT

""" Tests for anagram"""

import unittest
import errno
import shutil
from os.path import join

import anagram.anagram as anagram

class TestAnagram(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.parser = anagram.args_options()
		cls.mock_path = '/path/to/folder'

	@classmethod
	def tearDownClass(cls):
		try:
			shutil.rmtree('path')
		except OSError as exc:
			if exc.errno != errno.ENOENT:
				raise

	def test_incorrect_dict_path(self):
		""" Test read from non-existant file """

		args = ['--input', 'tests/samples/test']
		with self.assertRaises(IOError):
			anagram.main(self.parser.parse_args(args))
	
	def test_negative_threshold(self):
		""" Test an negative value for the character threshold """

		args = ['--count', '-1']
		
		with self.assertRaises(ValueError):
			anagram.main(self.parser.parse_args(args))

	def test_empty_output(self):
		""" Test an empty output """
		
		args = ['--input', 'tests/samples/empty']
		self.assertEquals(anagram.main(self.parser.parse_args(args)),
						  'Input dataset is empty')
