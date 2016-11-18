import re
import sys

class ParseText:
    def __init__(self, text):
	self.text = text
	self.parse_text_into_sections()
    def parse_text_into_sections(self):
        self.sections = []
        section_text = []
        for line in self.text.split('\n'): 
	    if line.strip() == '':
		continue
	    if line[:3] == '===':
	        if len(section_text)!=0:
		    self.sections.append(section_text)
		section_text = [line]
	    else:
		section_text.append(line)
	if len(section_text)>0:
		self.sections.append(section_text)

    def view_sections(self):
	for index, section_lines in enumerate(self.sections):
		print index, section_lines[0]
    def get_verb_translations(self):
	verb_flag = False
	for index, section_lines in enumerate(self.sections):
	    if 'Verb' in section_lines[0]:
		verb_flag = True
	    if 'Noun' in section_lines[0]:
		verb_flag = False
	    if 'Translations' in section_lines[0] and verb_flag:
		return self.translate_section(section_lines)
	return {}
    def translate_section(self, section_lines):
	self.sense_translations = {}
	sense = None
	for line in section_lines[1:]:
	    #print line
	    if line[:11] == '{{trans-top':
		#if sense is not None:
		#    print sense, self.sense_translations[sense]
		#print line
		splx = line.split('|')
		if len(splx) == 1:
		    sense = None
		    continue
		sense = line.split('|')[1].replace('}}', '')
		if not self.sense_translations.has_key(sense):
		    self.sense_translations[sense] = {}
	    elif '{{' == line[:2]:
		#ignorinf {{trans-mid, {{trans-bottom lines
		continue
	    elif '*' in line and line[2:].strip()!='':
		if sense is None:
		    continue
		line = re.sub("<.*?>", "", line) #remove html comments
		line = line[2:].strip()
		language = line.strip().split('{{')[0]
		word_trans = line[len(language):]
		language = language.replace(':', ' ')
		self.sense_translations[sense][language] = []
		#print language, word_trans
		if word_trans == '':
		    continue
		#print 'Word trans', type(word_trans), word_trans, word_trans.split('{{t+')
		if len(word_trans.split('{{t+'))>2:
		    word_formats = []
		    for val in word_trans.split('}},'):
			if val[-2:] != '}}':
			   word_formats.append(val+'}}')
			else:
			   word_formats.append(val)
		else:
		   word_formats = [word_trans]
		for word_format in word_formats:
		    if '{{t+' not in word_format:
			continue
		    word_format = word_format.strip()
		    for xformat in word_format.split():
		    	match_pattern = re.findall(r"\{\{([^}]+)\}", word_format)
			word_strings = match_pattern[0].split('|')
			if len(word_strings) <= 2:
			    continue
		    	trans_word = word_strings[2].replace('[', '').replace(']', '')
		    	self.sense_translations[sense][language].append(trans_word)
	return self.sense_translations
