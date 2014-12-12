import unittest
from ..lib.use_cases import LinkExtractor
from ..lib.entities import (
    Page,
    Link,
)


class MockDownloader():
    def download(self, url):
        import sys
        sys.stdout.write('Visting {}\n'.format(url))
        return url


class MockParser():
    def parse(self, html):
        if html == 'http://site.com/':
            return [
                'http://site.com/subpage',
            ]
        elif html == 'http://site.com/subpage':
            return []


class LinkExtractorTestCase(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.downloader = MockDownloader()
        self.parser = MockParser()
        self.l = LinkExtractor(self.downloader, self.parser)


    def test_it_extracts_links(self):
        x = self.l.run('http://site.com/')
        y = [
            Page(Link('http://site.com/'), [
                Link('/subpage', parent=Link('http://site.com/')),
            ]),
            Page(Link('http://site.com/subpage'))
        ]

        self.assertEqual(x, y)


    def test_get_not_yet_loaded_links1(self):
        pages = [
            Page(Link('http://site.com/'), [
                Link('http://site.com/subpage'),
            ]),
        ]

        x = self.l.get_not_yet_loaded_links(pages)
        y = [
            Link('http://site.com/subpage'),
        ]

        self.assertEqual(x, y)

    def test_get_not_yet_loaded_links2(self):
        pages = [
            Page(Link('http://site.com/'), [
                Link('http://site.com/subpage'),
            ]),
            Page(Link('http://site.com/subpage'), [
            ]),
        ]

        x = self.l.get_not_yet_loaded_links(pages)
        y = [
        ]

        self.assertEqual(x, y)


from ..lib.use_cases import BoundURLMixin


class BoundURLMixinTestCase(unittest.TestCase):
    def test_1(self):
        class Base(object):
            def get_urls(self, url):
                return [
                    'http://site1.com/subpage1',
                    'http://site1.com/subpage2',
                    'http://site2.com/subpage1',
                ]

        class Derivative(BoundURLMixin, Base):
            @property
            def bound_url(self):
                return 'http://site1.com/'

        self.assertEqual(
            Derivative().get_urls('http://site1.com/'),
            [
                'http://site1.com/subpage1',
                'http://site1.com/subpage2',
            ]
        )

    def test_2(self):
        class Base(object):
            def get_urls(self, url):
                return [
                    'http://site1.com/subpage1',
                    'http://site1.com/subpage2',
                    'http://site2.com/subpage1',
                ]

        class Derivative(BoundURLMixin, Base):
            @property
            def bound_url(self):
                return None

        self.assertEqual(
            Derivative().get_urls('http://site1.com/'),
            [
                'http://site1.com/subpage1',
                'http://site1.com/subpage2',
                'http://site2.com/subpage1',
            ]
        )


from ..lib.use_cases import LinkExtractorBoundToRootURL


class LinkExtractorBoundToRootURLTestCase(unittest.TestCase):
    def test_1(self):
        o = LinkExtractorBoundToRootURL(MockDownloader(), MockParser())
        self.assertIsInstance(o, BoundURLMixin)
        self.assertIsInstance(o, LinkExtractor)

    def test_2(self):
        o = LinkExtractorBoundToRootURL(MockDownloader(), MockParser())
        o.run('http://site.com/')
        self.assertEqual(o.bound_url, 'http://site.com/')
