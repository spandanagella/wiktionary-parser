from wiktionary_parser.page import Page
from wiktionary_parser.sections import Level2Block, Section, FillerSection
from wiktionary_parser.wiktionary_utils.text_splitter import Chopper, FillerBlock
#from .sections import deLanguageSection

class enPage(Page):

    def __init__(self, *args, **kwargs):
        self.language = 'en'
        super(enPage, self).__init__(*args, **kwargs)

    def title_OK(self):
        # Is it an info page
        if ':' in self.title:
            return False
        # Is it a conjugation page
        if '(Conjugation' in self.title:
            return False
        if '(Definition' in self.title or '(definition' in self.title or 'Definition)' in self.title:
            return False
        # for some Czech words.  Probably should be one of the above.
        if '(Possessiveadjective' in self.title:
            return False
        # Apparently it's a normal word.
        return True
