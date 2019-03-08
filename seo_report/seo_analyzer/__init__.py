""" Launch micro SEO analysis. """

from .page_title_analyzer import PageTitleAnalyzer
from .page_description_analyzer import PageDescriptionAnalyzer


class SEOAnalyzer():
    """ Instancy all micro SEO analyzers. """

    def __init__(self, metadata):
        self.page_title_analysis = PageTitleAnalyzer(metadata)
        self.page_description_analysis = PageDescriptionAnalyzer(metadata)
