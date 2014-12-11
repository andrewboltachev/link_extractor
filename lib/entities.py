import operator


class Page(object):
    def __init__(self, link, sublinks=None):
        self.link = link
        self.sublinks = [] if sublinks is None else sublinks

    def __eq__(self, other):
        return self.link == other.link

    def __repr__(self):
        return '<Page: {} [{}]>'.format(self.link.url, ', '.join(map(repr, self.sublinks)))

class Link(object):
    def __init__(self, url):
        self.url = url

    def __eq__(self, other):
        return self.url == other.url

    def __repr__(self):
        return '<Link: {}>'.format(self.url)
