import unittest
from ..lib.use_cases import LinkExtractor
from ..lib.entities import (
    Page,
    Link,
)


class LinkExtractorTestCase(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        class MockDownloader():
            def download(self, url):
                return url


        class MockParser():
            def parse(self, html):
                if html == 'http://site.com':
                    return [
                        'http://site.com/subpage',
                    ]
                elif html == 'http://site.com/subpage':
                    return []

        self.downloader = MockDownloader()
        self.parser = MockParser()
        self.l = LinkExtractor(self.downloader, self.parser)


    def test_it_extracts_links(self):
        x = self.l.run('http://site.com')
        y = [
            Page(Link('http://site.com'), [
                Link('/subpage', parent=Link('http://site.com')),
            ]),
            Page(Link('http://site.com/subpage'))
        ]

        self.assertEqual(x, y)


    def test_put_first_page_into_list(self):
        x = self.l.put_first_page_into_list('http://site.com')
        y = [
            Page(Link('http://site.com'), [
                Link('/subpage', Link('http://site.com')),
            ]),
        ]

        self.assertEqual(x, y)

    def test_get_not_yet_loaded_links1(self):
        pages = [
            Page(Link('http://site.com'), [
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
            Page(Link('http://site.com'), [
                Link('http://site.com/subpage'),
            ]),
            Page(Link('http://site.com/subpage'), [
            ]),
        ]

        x = self.l.get_not_yet_loaded_links(pages)
        y = [
        ]

        self.assertEqual(x, y)
