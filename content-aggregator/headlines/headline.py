class MainHeadline(object):
    def __init__(self, text, url):
        self.text = text
        self.url = url

    def get_text(self):
        return self.text

    def get_url(self):
        return self.url


class MinorHeadline(object):
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text
