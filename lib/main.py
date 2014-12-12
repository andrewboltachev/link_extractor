import requests
import sys
from .use_cases import LinkExtractor


class RequestsPageDownloader(object):
    def download(self, url):
        import sys
        sys.stderr.write('Visting {}\n'.format(url))
        r = requests.get(url)
        return r.content if r.status_code == 200 else ''


class BSPageParser(object):

    def parse(self, content):
        from bs4 import BeautifulSoup
        b = BeautifulSoup(content)
        urls_of_subpages = [x.attrs['href'] for x in b.findAll('a')]
        return urls_of_subpages


if __name__ == '__main__':
    if not len(sys.argv) == 2:
        sys.stderr.write('Must be only one argument!\n')
        sys.exit(1)

    link_extractor = LinkExtractor(
        downloader=RequestsPageDownloader(),
        parser=BSPageParser()
    )
    pages = link_extractor.run(sys.argv[1])
    unique_pages = []
    for page in pages:
        if page not in unique_pages:
            unique_pages.append(page)
            print page.link.url
