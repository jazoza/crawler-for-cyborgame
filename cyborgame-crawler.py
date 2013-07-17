#! /usr/bin/python

import codecs, collections, sys #pygame
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

characters={0:"title", 1:"LE PERSONNAGE DE ROMAN", 2:"LA VOIX", 3:"LE COLONEL", 4:"#scene description", 5:"#shouting", 6:"#battle", 7:"#shock"}

character=raw_input("choose the character/scene: \n0 : titles \n1 : Le Personnage \n2 : La Voix \n3 : Le Colonel \n4 : Scene description \n5 : Shouting (PART 1) \n6 : Battle title \n7 : Shouting (PART 3) \nor type in a word (case sensitive) \n>> ")

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
        if lookfor=="LA VOIX":
            print "to display SECONDE PARTIE only, choose dialogues from 33 to 60"
        
#the choice of the scene here:
        display=raw_input('which scene do you want to print?\n(to exit, press "ESC")\n')
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
            if lookfor=="LA VOIX":
                print "to display SECONDE PARTIE only, choose dialogues from 33 to 60"
                for i, word in enumerate(the_line.split(), 1):
                    if i%5:
                        print word, 
                        fout.write(word+' ')
                    else:
                        print word
                        fout.write(word+'\n')
            else:
                for i, word in enumerate(the_line.split(), 1):
                    if i%2:
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
part2: LA VOIX, chronologically; (starts with line 433, choose dialogues from 33 to 60; 
how much text appears? 
part3: combat titles, descriptions, WHAT IS WRITTEN IN BIG, +++

DONE
part1: titles, descriptions, characters: improvise, slash lines (#SHOUTING)
+ follow a person
"""
