class Website(object):
    def __init__(self, main_headline, minor_headlines, name):
        self.main_headline = main_headline
        self.minor_headlines = minor_headlines
        self.name = name

    def get_main_headline(self):
        return self.main_headline

    def get_minor_headlines(self):
        return self.minor_headlines

    def get_name(self):
        return self.name
