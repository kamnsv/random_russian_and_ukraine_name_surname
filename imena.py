#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, codecs
import random

def imfaot(pol=None, lang=None):
	ci,cf,co = "imena_%s_%s.txt", "family_%s_%s.txt", "otch_%s_%s.txt"
	
	path = 'data'
	if len(sys.argv) > 3:
		path = sys.argv[3]
	path += os.path.sep
	if not pol in ['m','f']: pol = ['m','f'][random.choice(range(2))]
	if not lang in ['ru','ua']: lang = ['ru','ua'][random.choice(range(2))]
    
	a = []
	for file_name in (cf,ci,co):
		file_name = file_name % (pol, lang)
		with codecs.open(path+file_name, "r", "utf-8") as f:
			lines = f.readlines()
			line  = lines[random.choice(range(len(lines)))]
			a.append(line.rstrip("\n").rstrip("\t").rstrip())

	return a

if "__main__" == __name__ :  # вызов из консоли
	print(' '.join(imfaot(input('Пол [m, f]: '), input('Язык [ru, ua]: '))))