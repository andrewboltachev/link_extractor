import operator


class Page(object):
    def __init__(self, link, sublinks=None):
        self.link = link
        self.sublinks = sublinks

    def __eq__(self, other):
        return self.link == other.link and self.sublinks == other.sublinks


class Link(object):
    def __init__(self, url):
        self.url = url

    def __eq__(self, other):
        return self.url == other.url
