#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, codecs
import random




def imfaot(ci,cf,co):
	path = 'data'
	if len(sys.argv) > 3:
		path = sys.argv[3]
	path += os.path.sep
    
	a = []
	for file_name in (ci,cf,co):
		with codecs.open(path+file_name, "r", "utf-8") as f:
			lines = f.readlines()
			line  = lines[random.choice(range(len(lines)))]
			a.append(line.rstrip("\n"))

	return *a,



def training():
	if len(sys.argv) <= 1:
		print("Введите -m или -f")
	elif sys.argv[1] == "-m" and sys.argv[2] == "-ru":
		mansiru = "imena_m_ru.txt"
		mansfru = "family_m_ru.txt"
		mansotchru = "otch_m_ru.txt"

		ci = mansiru
		cf = mansfru
		co = mansotchru
		imret, famret, otchmret = imfaot(ci,cf,co)
		print(imret)
		print(otchmret)
		print(famret)

	elif sys.argv[1] == "-f" and sys.argv[2] == "-ru":
		womaniru = "imena_f_ru.txt"
		womanfru = "family_f_ru.txt"
		womanotchru = "otch_f_ru.txt"

		ci = womaniru
		cf = womanfru
		co = womanotchru

		imret, famret, otchmret = imfaot(ci,cf,co)
		print(imret)
		print(otchmret)
		print(famret)

	elif sys.argv[1] == "-m" and sys.argv[2] == "-ua":
		mansiua = "imena_m_ua.txt"
		mansfua = "family_m_ua.txt"
		mansotchua = "otch_m_ua.txt"

		ci = mansiua
		cf = mansfua
		co = mansotchua
		imret, famret, otchmret = imfaot(ci,cf,co)
		print(imret)
		print(otchmret)
		print(famret)

	elif sys.argv[1] == "-f" and sys.argv[2] == "-ua":
		womaniua = "imena_f_ua.txt"
		womanfua = "family_f_ua.txt"
		womanotchua = "otch_f_ua.txt"

		ci = womaniua
		cf = womanfua
		co = womanotchua

		imret, famret, otchmret = imfaot(ci,cf,co)
		print(imret)
		print(otchmret)
		print(famret)	
	else:
		print("Неправильный аргумент командной строки")

	
	return 0

training()


