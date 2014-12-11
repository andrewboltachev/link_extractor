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

    def test_equal_pages_are_equal(self):
        x = Page(Link('http://site1.com/subpage'))
        y = Page(Link('/subpage', Link('http://site1.com')))
        self.assertEqual(x, y)


class PageEqualityForSubLinksTestCase(unittest.TestCase):
    def test_equal_pages_are_equal(self):
        x = Page(Link('http://site1.com'), [Link('http://site1.com/subpage1')])
        y = Page(Link('http://site1.com'), [Link('http://site1.com/subpage2')])
        self.assertTrue(x == y)


class LinkTestCase(unittest.TestCase):
    def test_equal_links_are_equal(self):
        x = Link('http://site1.com')
        y = Link('http://site1.com')
        self.assertTrue(x == y)

    def test_non_equal_links_are_not_equal(self):
        x = Link('http://site1.com')
        y = Link('http://site2.com')
        self.assertFalse(x == y)


class PageReprTest(unittest.TestCase):
    def test_repr(self):
        p = Page(Link('http://site1.com'), [Link('http://site1.com/subpage1'), Link('http://site1.com/subpage2')])
        x = repr(p)
        y = '<Page: http://site1.com [<Link: http://site1.com/subpage1>, <Link: http://site1.com/subpage2>]>'
        self.assertEqual(x, y)
