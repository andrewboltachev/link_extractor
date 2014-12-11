import unittest
from ..lib.use_cases import LinkExtractor
from ..lib.enitites import (
    Page,
    Link,
)


class LinkExtractorTestCase(unittest.TestCase):
    def setUp(self):
        class MockDownloader():
            def download(self, url):
                return url


        class MockParser():
            def parse(self, html):
                if url == 'http://site.com':
                    return Page(
                        Link('http://site.com'),
                        [
                            Link('http://site.com/subpage'),
                        ]
                    )
                elif url == 'http://site.com/subpage':
                    return Page(
                        Link('http://site.com'),
                        []
                    )

        self.downloader = MockDownloader()
        self.parser = MockParser()
        self.l = LinkExtractor(self.downloader, self.parser)


    def te1st_it_extracts_links(self):
        x = self.l.run('http://site.com')
        y = [
            Page(Link('http://site.com'), [
                Link('http://site.com/subpage'),
            ]),
            Page(Link('http://site.com/subpage'))
        ]

        self.assertEqual(x, y)


    def test_put_first_page_into_list(self):
        x = self.l.put_first_page_into_list('http://site.com')
        y = [
            Page(Link('http://site.com'), [
                Link('http://site.com/subpage'),
            ]),
        ]

        self.assertEqual(x, y)
