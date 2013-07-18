#! /usr/bin/python

import codecs, collections, sys #pygame
import itertools
#from pygame.locals import *

#pygame.init()
#screen = pygame.display.set_mode((40, 80))

try:
    fin = codecs.open("CYBORGAME.txt", "r", encoding="utf-8")
    try:
        script = fin.readlines()
    finally:
        fin.close()
except IOError:
    pass

def crawler(wfile, word, wdict):
    key_found=False
    stopper=''
    for i, line in enumerate(wfile):
        if key_found and line.strip()!=stopper:
            wdict[i]=line.strip().upper()
        elif line.startswith(word):
            key_found=True
        else:
            key_found=False
    #print wdict
    return wdict


def breaklines(line, filez, n):
    for i, word in enumerate(line.split(), 1):
        if i%n:
            print word, 
            filez.write(word+' ')
        else:
            print word
            filez.write(word+'\n')

### choose script content to analyse

characters={0:"title", 1:"LE PERSONNAGE DE ROMAN", 2:"LA VOIX", 3:"LE COLONEL", 4:"#scene description", 5:"#shouting", 6:"#battle", 7:"#shock", 8: "#words"}

character=raw_input("choose the character/scene: \n0 : titles \n1 : Le Personnage \n2 : La Voix \n3 : Le Colonel \n4 : Scene description \n5 : Shouting (PART 1) \n6 : Battle title \n7 : Shouting (PART 3) \n8 : SLASH words \nor type in a word (case sensitive) \n>> ")

try:
    lookfor=characters[eval(character)]
except NameError:
    lookfor=str(character)
#    print "not a valid choice"

print 'looking for....', lookfor

### add content to dictionary

lookfordict={}
crawler(script, lookfor, lookfordict)

lookfordictOrder = collections.OrderedDict(sorted(lookfordict.items()))
#print 'this!', lookfordictOrder

### main loop ###

while True:
    if any(lookfordict.values()):
        print 'you have', len(lookfordict), 'scenes'
        
# the choice of the line here:
        display=raw_input('which line do you want to print?\n(to exit, press "ESC")\n')
        try:
            selection=eval(display)-1
        except NameError or SyntaxError:
            selection=display

# how many lines to print:
        saucisson=raw_input('how many lines: ')
    
# iterates through the ordered dictionary:
    it = iter(lookfordictOrder)
    for i, key in enumerate(lookfordictOrder):
        try:
            #print iter(lookfordictOrder[key])
            it.next()
            #print 'next', it.next()
            if i == selection:
                fout = codecs.open("crawler_for_subtitler.txt", "w", encoding="utf-8")
                fout_multiline = codecs.open("multiline_crawler_for_subtitler.txt", "w", encoding="utf-8")
                fout_wrap = codecs.open("wrapped_crawler_for_subtitler.txt", "w", encoding="utf-8")
                #print key
                the_line=lookfordictOrder[key] 
                print 'to fout', the_line
                fout.write(the_line)
                breaklines(the_line, fout_wrap, 5)
                for j in range(int(saucisson)):
                    next_line=lookfordictOrder[it.next()]
                    print 'to fout_multiline', next_line
                    print "----"
                    fout_multiline.write(next_line)
                    fout_multiline.write("\n")
                
                print 'wrote the', selection, 'st/nd/rd line to "crawler_for_subtitler.txt"'
                print 'wrote the', selection, 'line and the', saucisson, ' consecutive line(s) to "multiline_crawler_for_subtitler.txt"'
                print 'wrote the first line wrapped to "wrapped_crawler_for_subtitler.txt"'
                fout.close()
                fout_multiline.close()
                fout_wrap.close()
        except StopIteration:
            continue



"""
TODO
part1: descriptions > always three lines!!! follow the actors with descriptions
prepare a list of titles or live writing (ERASE, SLASH, 
part2: LA VOIX, chronologically; (starts with line 433, choose dialogues from 33 to 60; 
how much text appears? 
part3: combat titles, descriptions, WHAT IS WRITTEN IN BIG, +++

DONE
part1: titles, descriptions, characters: improvise, slash lines (#SHOUTING)
+ follow a person
"""
