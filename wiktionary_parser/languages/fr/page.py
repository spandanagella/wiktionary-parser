from wiktionary_parser.page import Page
from wiktionary_parser.sections import Level2Block, Section, FillerSection
from wiktionary_parser.wiktionary_utils.text_splitter import Chopper, FillerBlock
#from .sections import deLanguageSection

class frPage(Page):

    def __init__(self, *args, **kwargs):
        self.language = 'fr'
        super(frPage, self).__init__(*args, **kwargs)
