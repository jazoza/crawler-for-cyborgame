#! /usr/bin/python

import codecs, collections, pygame, sys
#from pygame.locals import *

#pygame.init()
#screen = pygame.display.set_mode((40, 80))

try:
    fin = codecs.open("CYBORGAME.txt", "r", encoding="utf-8")
    fout_oneliner = codecs.open("crawler_oneliner.txt", "w", encoding="utf-8")
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
            fout_oneliner.write(line.strip().upper()+"\t\t\t\t",)
            wdict[i]=line.strip().upper()
        elif line.startswith(word):
            key_found=True
        else:
            key_found=False
    #print wdict
    return wdict


### choose script content to analyse

characters={1:"LE PERSONNAGE DE ROMAN", 2:"LA VOIX", 3:"LE COLONEL", 4:"#SCENE DESCRIPTION", 5:"LUMIERE"}

character=raw_input("choose the character/scene: \n1 : Le Personnage \n2 : La Voix \n3 : Le Colonel \n4 : Scene intro \n5 : Atmosphere \nor type in a word (case sensitive) \n>> ")

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
        
#the choice of the scene here:
        display=raw_input('which scene do you want to print?\n(to exit, press "ESC"\n)')
        try:
            selection=eval(display)-1
        except NameError or SyntaxError:
            selection=display
    
# the choice of the number of lines:
#        lines=raw_input('how many lines?\n')
#        try:
#            n_lines=eval(lines)
#        except NameError:
#            n_lines=1

    
    for i, key in enumerate(lookfordictOrder):
    #print i, key
        """
        choose how manuy lines to display simultaneously
        """
        if i==selection:
            print key
            fout = codecs.open("crawler_for_subtitler.txt", "w", encoding="utf-8")
            print 'will write to "crawler_for_subtitler.txt"'
            the_line=lookfordictOrder[key]
            for i, word in enumerate(the_line.split(), 1):
                if i%3:
                    print word,
                    fout.write(word+' ')
                else:
                    print word
                    fout.write(word+'\n')
    #        fout.write('pisao sam')
    #        print 'updated crawler_for_subtitler.txt', the_line
            fout.close()
        elif selection=='f':
            print 'forward,', 'key', key
            the_line=next(lookfordictOrder.itervalues())
    

"""
TODO
! split line into three lines, write that to the file!!!
part1: titles, descriptions, characters: improvise, slash lines (#SHOUTING)
+ follow a person
part2: LA VOIX, chronologically; (starts with line 433, choose dialogues from 33 to 60; 
how much text appears? 
part3: combat titles, descriptions, WHAT IS WRITTEN IN BIG, +++
"""
