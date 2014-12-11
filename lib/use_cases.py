from .entities import (
    Page,
    Link,
)


class LinkExtractor(object):
    def __init__(self, downloader, parser):
        self.parser = parser
        self.downloader = downloader

    def run(self, root_url):
        pages = self.put_first_page_into_list(root_url)
        not_yet_loaded_links = self.get_not_yet_loaded_links(pages)
        while len(not_yet_loaded_links) > 0:
            loaded_pages = self.load_pages(not_yet_loaded_links)
            for page in loaded_pages:
                pages.append(page)
            not_yet_loaded_links = self.get_not_yet_loaded_links(pages)
        return pages

    def load_pages(self, links):
        loaded_pages = [self.load_page(link) for link in links]
        return loaded_pages

    def load_url(self, url):
        return self.load_page(Link(url))

    def load_page(self, link):
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
