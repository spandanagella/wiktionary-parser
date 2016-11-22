# -*- coding: utf-8 -*-
"""
This example extracts a number of words from the wiktionary xml file.
"""

import sys
sys.path.insert(0, '/disk/scratch/s1146856/project_codes/tools/sense_stuff/wiktionary-parser-xml/wiktionary_parser')
sys.path.insert(0, '/disk/scratch/s1146856/project_codes/tools/sense_stuff/wiktionary-parser-xml')
from wiktionary_parser.xml_parser import XMLPageParser
from wiktionary_parser.languages.fr.page import frPage
from wiktionary_parser.languages.fr.parseText import FrParseText

xml_file = open('../../../../../datasets/sense_disambiguation_datasets/frwiktionary-20161101-pages-articles-multistream.xml')
xml_parser = XMLPageParser(xml_file, frPage)

french_words = set(['sauter'])


#for title, page in xml_parser.from_titles(german_words):
#    found_words.add(title)
for page in xml_parser.from_titles(french_words):
    #print page.text
    parseData = FrParseText(page.text)
    print 'Title', page.title
    #parseData.view_sections()
    #print parseData.synonyms
    print parseData.verb_translations
    break
