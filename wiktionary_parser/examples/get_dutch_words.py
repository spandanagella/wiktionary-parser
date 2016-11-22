# -*- coding: utf-8 -*-
"""
This example extracts a number of words from the wiktionary xml file.
"""

import sys
sys.path.insert(0, '/disk/scratch/s1146856/project_codes/tools/sense_stuff/wiktionary-parser-xml/wiktionary_parser')
sys.path.insert(0, '/disk/scratch/s1146856/project_codes/tools/sense_stuff/wiktionary-parser-xml')
from wiktionary_parser.xml_parser import XMLPageParser
from wiktionary_parser.languages.nl.page import nlPage
from wiktionary_parser.languages.nl.parseText import NlParseText

xml_file = open('../../../../../datasets/sense_disambiguation_datasets/nlwiktionary-20161120-pages-articles-multistream.xml')
xml_parser = XMLPageParser(xml_file, nlPage)

dutch_words = set(['springen'])


#for title, page in xml_parser.from_titles(german_words):
#    found_words.add(title)
for page in xml_parser.from_titles(dutch_words):
    print page.text
    parseData = NlParseText(page.text)
    print 'Title', page.title
    #parseData.view_sections()
    #print parseData.synonyms
    print parseData.verb_translations
    break
