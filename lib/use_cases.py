from .entities import (
    Page,
    Link,
)


class LinkExtractor(object):
    def __init__(self, downloader, parser):
        pass

    def run(self, root_url):
        pages = self.put_first_page_into_list(url)
        not_loaded_links = self.get_not_yet_loaded_links(pages)
        while len(not_loaded_links) > 0:
            self.load_links(pages, not_loaded_links)
        return pages

    def put_first_page_into_list(self, url):
        return [
            Page(Link('http://site.com'), [
                Link('http://site.com/subpage'),
            ]),
        ]
