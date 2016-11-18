# -*- coding: utf-8 -*-

from wiktionary_parser.formating_type import RegexFT
from wiktionary_parser.sections import FTSection
from wiktionary_parser.exceptions import InconsistentEntry
from wiktionary_parser.alerts import WordTitleMismatchAlert

def chop_prefix_get_data(section, groupdict):
    """
    Makes sure that the word in the regex matches that of the page.
    If it doesn't then chopping of the prefix was probably a mistake.
    """
    word = section.get_property('title')
    scraped_word = groupdict['word']
    if word != scraped_word:
        whole_word = groupdict['whole_word'].rstrip()
        #if word != whole_word:
        #    raise DodgyWord()
        groupdict['word'] = whole_word
    return groupdict

def no_word_get_data(section, groupdict):
    groupdict['word'] = section.get_property('title')
    return groupdict
    
    
class enLangTitleSection(FTSection):

    name = 'Language Title Section'

    def process_data(self, data):
        self.parent.set_property('language', data['language'])
        # Check that word is compatible with page title
        page_title = self.get_property('page').title
        word = data['word']
        if not self.word_matches_title(page_title, word, data['language']):
            message = '%s: %s does not match title %s' % (data['language'], word, page_title) 
            alert = WordTitleMismatchAlert(
                message=message, language=data['language'],
                title=page_title, word=word)
            self.alerts.append(alert)

    def word_matches_title(self, page_title, word, language):
        if language == 'Lateinisch':
            # FIXME: Could have a mapping from non-accented to accented letters.
            # Don't check Latin words because they put accents on word but not on title.
            return True
        if u'®' in word or u'[[' in word or u'!' in word or '?' in word or '&' in word:
            return True
        if '/' in page_title:
            return True
        #if language == 'Indogermanisch':
        #    word = word.replace('*', '')
        return (word == page_title)

