from .entities import (
    Page,
    Link,
)


class LinkExtractor(object):
    def __init__(self, downloader, parser):
        self.parser = parser
        self.downloader = downloader

    def run(self, root_url):
        pages = []
        not_yet_loaded_links = [Link(root_url)]
        while len(not_yet_loaded_links) > 0:
            loaded_pages = self.load_pages(not_yet_loaded_links, bound_url=root_url)
            for page in loaded_pages:
                pages.append(page)
            not_yet_loaded_links = self.get_not_yet_loaded_links(pages)
        return pages

    def load_pages(self, links, bound_url=None):
        loaded_pages = [self.load_page(link, bound_url) for link in links]
        return loaded_pages

    def get_urls(self, url):
        return self.parser.parse(self.downloader.download(url))

    def load_page(self, link, bound_url=None):
        urls = self.get_urls(link.url)
        sublinks = [Link(url, parent=link) for url in urls]
        if bound_url is not None:
            sublinks = [sublink for sublink in sublinks if sublink.url.startswith(bound_url)]
        return Page(
            link,
            sublinks
        )

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
