import requests
import sys
from .use_cases import LinkExtractor
from .entities import (
    Page,
    Link,
)


class RequestsPageDownloader(object):
    def download(self, url):
        import sys
        sys.stderr.write('Visting {}\n'.format(url))
        r = requests.get(url)
        return r.content if r.status_code == 200 else ''


class BSPageParser(object):

    def content_to_urls_of_subpages(self, content):
        from bs4 import BeautifulSoup
        b = BeautifulSoup(content)
        urls_of_subpages = [x.attrs['href'] for x in b.findAll('a')]
        return urls_of_subpages

    def parse(self, content):
        urls_of_subpages = self.content_to_urls_of_subpages(content)
        return list(map(Link, urls_of_subpages))


if __name__ == '__main__':
    if not len(sys.argv) == 2:
        sys.stderr.write('Must be only one argument!\n')
        sys.exit(1)

    link_extractor = LinkExtractor(
        downloader=RequestsPageDownloader(),
        parser=BSPageParser()
    )
    print link_extractor.run(sys.argv[1])
