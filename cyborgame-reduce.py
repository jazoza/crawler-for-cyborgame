#! /usr/bin/python

import codecs, collections, sys, textwrap

### open files, read original and wrap it by the input number of characters ###
try:
    fin=codecs.open("CYBORGAME-edited.txt", "r", encoding="utf-8")
    filez=codecs.open("CYBORGAME-wrapped.txt", "w", encoding="utf-8")
#    try: 
#        script=filez.readlines()
#    finally:
#        fin.close()
except IOError:
    pass

wrapping=raw_input("wrap at how many characters?\n(default 48)\n")
try:
    to_wrap=eval(wrapping)
except NameError:
    to_wrap=48

for line in fin:
    list_to_write=textwrap.wrap(line, to_wrap)
    #print 'wrapped', list_to_write
    #line_to_write=""
    for item in list_to_write:
        filez.write(item+'\n')
#filez.close()
try:
    fout=codecs.open("CYBORGAME-wrapped.txt", "r", encoding="utf-8")
    try:
        script=fout.readlines()
    finally:
        fout.close()
except IOError:
    pass

### start line processing ####

i = 0
saucisson = ""
while True:
    
    gonext=raw_input("press x\n")
    for line in script:
        if gonext=="x":
            i+=1
            if line[:1]!="#":
                    saucisson += line.strip().upper() + "\n"
            if i%4 == 0:
                fout=codecs.open("out.txt", "w", encoding="utf-8") 
                fout.write(saucisson)
                fout.close()
                print "----"
                print saucisson
                saucisson = ""
                gonext=raw_input("press x\n")



