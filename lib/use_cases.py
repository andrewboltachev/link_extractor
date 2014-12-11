from .entities import (
    Page,
    Link,
)


class LinkExtractor(object):
    def __init__(self, downloader, parser):
        self.parser = parser
        self.downloader = downloader

    def run(self, root_url):
        pages = self.put_first_page_into_list(url)
        not_yet_loaded_links = self.get_not_yet_loaded_links(pages)
        while len(not_yet_loaded_links) > 0:
            self.load_links(pages, not_loaded_links)
        return pages

    def load_url(self, url):
        return self.load_link(Link(url))

    def load_link(self, link):
        return self.parser.parse(self.downloader.download(link.url))

    def put_first_page_into_list(self, url):
        return [self.load_url(url)]

    def get_already_loaded_links(self, pages):
        return [page.link for page in pages]

    def get_links_of_subpages(self, pages):
        return [sublink for page in pages for sublink in page.sublinks]

    def get_not_yet_loaded_links(self, pages):
        already_loaded_links = self.get_already_loaded_links(pages)
        sublinks = self.get_links_of_subpages(pages)
        not_yet_loaded_links = []
        for link in sublinks:
            if not link in already_loaded_links:
                not_yet_loaded_links.append(link)
        return not_yet_loaded_links
