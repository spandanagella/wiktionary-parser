# -*- coding: utf-8 -*-
"""
This example extracts a number of words from the wiktionary xml file.
"""

import sys
import os
import pickle
from wiktionary_parser.xml_parser import XMLPageParser
from wiktionary_parser.languages.en.page import enPage
from wiktionary_parser.languages.en.parseText import ParseText

xml_file = XML_FILE_PATH
xml_parser = XMLPageParser(xml_file, enPage)

words = ['ride', 'jump']

out_dir = OUT_DIR_PATH
for page in xml_parser.from_titles(words):
    file_path = os.path.join(out_dir, '%s.pkl' %(page.title))
    print file_path
    parseData = ParseText(page.text)
    verb_sense_translations = parseData.get_verb_translations()
    pickle.dump(verb_sense_translations, open(file_path, 'w'))
