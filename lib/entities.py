import operator


class Page(object):
    def __init__(self, link, sublinks=None):
        self.link = link
        self.sublinks = [] if sublinks is None else sublinks

    def __eq__(self, other):
        return self.link == other.link and self.sublinks == other.sublinks

    def __repr__(self):
        return '<Page: {} [{}]>'.format(self.link.url, ', '.join(map(repr, self.sublinks)))

class Link(object):
    def __init__(self, url, parent=None):
        self._url = url
        self.parent = parent

    def __eq__(self, other):
        return self.url == other.url

    def __repr__(self):
        return '<Link: {}>'.format(self.url)

    def chain(self):
        if self.parent is None:
            parent_chain = []
        else:
            parent_chain = self.parent.chain()
        return parent_chain + [self._url]

    @property
    def url(self):
        from urlparse import urljoin
        return reduce(urljoin, self.chain())
