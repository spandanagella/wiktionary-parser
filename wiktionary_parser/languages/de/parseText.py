# -*- coding: utf-8 -*-
import re
import sys

class DeParseText:
    def __init__(self, text):
	self.text = text
	self.parse_text_into_sections()
	self.verb_flag = False
	self.checkVerb()
	self.synonyms = []
	self.updateSynonyms()
	self.verb_translations = {}
	self.get_verb_translations()
    def parse_text_into_sections(self):
        self.sections = []
        section_text = []
        for line in self.text.split('\n'): 
	    if line.strip() == '':
		continue
	    if (line[:2] == '{{' and line[-2:] == '}}') or line[:2] == '==':
	        if len(section_text)!=0:
		    self.sections.append(section_text)
		section_text = [line]
	    else:
		section_text.append(line)
	if len(section_text)>0:
		self.sections.append(section_text)

    def checkVerb(self):
	for section in self.sections:
	    if 'Wortart' in section[0]:
		match_pattern = re.findall(r"\{\{([^}]+)\}", section[0])[0]
		if match_pattern.split('|')[1] == 'Verb':
		    self.verb_flag = True	
	
    def updateSynonyms(self):
	for section in self.sections:
	    if 'Synonyme' in section[0]:
		for line in section[1:]:
		    for word in re.findall(r"\[\[([^]]+)\]", line):	
			self.synonyms.append(word)
	
    def view_sections(self):
	for index, section_lines in enumerate(self.sections):
		print index, section_lines[0]
    def get_verb_translations(self):
	if not self.verb_flag:
	    return self.verb_translations
	for index, section_lines in enumerate(self.sections):
	    #if '====' in section_lines[0] and 'Verb' not in section_lines[0]:
	    if u'Übersetzungen' in section_lines[0]: 
		self.translate_section(section_lines)
    def translate_section(self, section_lines):
	for line in section_lines[1:]:
	    line = line.strip()
	    if line[0]!='*':
		continue
	    else: # '*' in line and line[2:].strip()!='':
		match_pattern = re.findall(r"\{\{([^}]+)\}", line)
		if len(match_pattern) == 0:
		    continue
		language = match_pattern[0]
		words = []
		for word_format in match_pattern[1:]:
		    spl = word_format.split('|')
		    if len(spl)<=2:
			continue	
		    #print word_format, '--- Line---:', line
		    words.append(spl[2])
		self.verb_translations[language] = words
