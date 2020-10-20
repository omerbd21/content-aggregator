class Website(object):
    def __init__(self, main_headline, minor_headlines, name):
        self._main_headline = main_headline
        self._minor_headlines = minor_headlines
        self._name = name

    def get_main_headline(self):
        return self._main_headline

    def get_minor_headlines(self):
        return self._minor_headlines

    def get_name(self):
        return self._name
