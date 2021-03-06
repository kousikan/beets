"""Tests for the 'zero' plugin"""

from _common import unittest
from beets.library import Item
from beetsplug.zero import ZeroPlugin


class ZeroPluginTest(unittest.TestCase):
    def test_no_patterns(self):
        i = Item(
            comments='test comment',
            day=13,
            month=3,
            year=2012,
        )
        z = ZeroPlugin()
        z.debug = False
        z.fields = ['comments', 'month', 'day']
        z.patterns = {'comments': ['.'],
                      'month': ['.'],
                      'day': ['.']}
        z.write_event(i)
        self.assertEqual(i.comments, '')
        self.assertEqual(i.day, 0)
        self.assertEqual(i.month, 0)
        self.assertEqual(i.year, 2012)

    def test_patterns(self):
        i = Item(
            comments='from lame collection, ripped by eac',
            year=2012,
        )
        z = ZeroPlugin()
        z.debug = False
        z.fields = ['comments', 'year']
        z.patterns = {'comments': 'eac lame'.split(),
                      'year': '2098 2099'.split()}
        z.write_event(i)
        self.assertEqual(i.comments, '')
        self.assertEqual(i.year, 2012)

def suite():
    return unittest.TestLoader().loadTestsFromName(__name__)

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
