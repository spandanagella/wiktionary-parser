# -*- coding: utf-8 -*-
import re
import sys

class NlParseText:
    def __init__(self, text):
	self.text = text
	self.translation_text = []
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
	    line = line.strip()
	    if line.strip() == '':
		continue
	    if line[0] == '*':
		self.translation_text.append(line)
	    #if (line[:2] == '{{' and line[-2:] == '}}') or line[:2] == '==':
	    if line[:3] == '===':
	        if len(section_text)!=0:
		    self.sections.append(section_text)
		section_text = [line]
	    else:
		section_text.append(line)
	if len(section_text)>0:
		self.sections.append(section_text)

    def checkVerb(self):
	for section in self.sections:
	    if 'verbe' in section[0]:
		match_pattern = re.findall(r"\{\{([^}]+)\}", section[0])[0]
		if match_pattern.split('|')[1] == 'verbe':
		    self.verb_flag = True	
	
    def updateSynonyms(self):
	for section in self.sections:
	    if 'synonymes' in section[0]:
		for line in section[1:]:
		    for word in re.findall(r"\[\[([^]]+)\]", line):	
			self.synonyms.append(word)
	
    def view_sections(self):
	for index, section_lines in enumerate(self.sections):
		print index, section_lines[0]
    def get_verb_translations(self):
	self.translate_section()
    def translate_section(self):
	sense_translations = {}
	for line in self.translation_text:
	    line = line.strip()
	    if line[0]!='*':
		continue
	    else: # '*' in line and line[2:].strip()!='':
		match_pattern = re.findall(r"\{\{([^}]+)\}", line)
		#print match_pattern
		if len(match_pattern) == 0 or len(match_pattern) == 1:
		    continue
		words = []
		language = 'None'
		for word_format in match_pattern[1:]:
		    spl = word_format.split('|')
		    if len(spl)<3:
			continue
		    language = spl[1]
		    if not self.verb_translations.has_key(language):
		        self.verb_translations[language] = []
		    words.append(spl[2])
		if language== 'None' or len(words) == 0:
		    continue
		self.verb_translations[language].extend(words)
