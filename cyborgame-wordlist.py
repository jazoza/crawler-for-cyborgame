#! /usr/bin/python

import codecs, collections, sys #pygame
import itertools
#from pygame.locals import *

#pygame.init()
#screen = pygame.display.set_mode((40, 80))

try:
    fin = codecs.open("wordlist.txt", "r", encoding="utf-8")
    try:
        words = fin.readlines()
    finally:
        fin.close()
except IOError:
    pass

while True:
    choose=raw_input('which word?\n')
    try: 
        selection=eval(choose)
    except NameError:
        selection=1

    for i, word in enumerate(words):
        if i==selection:
            fout=codecs.open("the_word.txt", "w", encoding="utf-8")
            print word.upper()
            fout.write(word.upper())

