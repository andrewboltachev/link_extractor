import unittest
from ..lib.entities import (
    Page,
    Link,
)


class PageEqualityForLinksTestCase(unittest.TestCase):
    def test_equal_pages_are_equal(self):
        x = Page(Link('http://site1.com'))
        y = Page(Link('http://site1.com'))
        self.assertTrue(x == y)

    def test_non_equal_pages_are_not_equal(self):
        x = Page(Link('http://site1.com'))
        y = Page(Link('http://site2.com'))
        self.assertFalse(x == y)


class PageEqualityForSubLinksTestCase(unittest.TestCase):
    def test_equal_pages_are_equal(self):
        x = Page(Link('http://site1.com'), [Link('http://site1.com/subpage')])
        y = Page(Link('http://site1.com'), [Link('http://site1.com/subpage')])
        self.assertTrue(x == y)

    def test_non_equal_pages_are_not_equal(self):
        x = Page(Link('http://site1.com'), [Link('http://site1.com/subpage1')])
        y = Page(Link('http://site1.com'), [Link('http://site1.com/subpage2')])
        self.assertFalse(x == y)


class LinkTestCase(unittest.TestCase):
    def test_equal_links_are_equal(self):
        x = Link('http://site1.com')
        y = Link('http://site1.com')
        self.assertTrue(x == y)

    def test_non_equal_links_are_not_equal(self):
        x = Link('http://site1.com')
        y = Link('http://site2.com')
        self.assertFalse(x == y)
