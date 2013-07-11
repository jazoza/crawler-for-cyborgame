import codecs, collections

try:
    fin = codecs.open("CYBORGAME.txt", "r", encoding="utf-8")
    fout = codecs.open("crawler_for_subtitler.txt", "w", encoding="utf-8")
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
            fout.write(line.upper())
            fout_oneliner.write(line.strip().upper()+"\t\t\t\t",)
            wdict[i]=line.strip().upper()
        elif line.startswith(word):
            key_found=True
        else:
            key_found=False
    #print wdict
    return wdict


### handwork....

nom1="LE PERSONNAGE DE ROMAN"
nom2="LA VOIX"
nom3="LE COLONEL"
scen="#SCENE DESCRIPTION"
atmosphere="LUMIERE"
character=raw_input("choose the character/scene: \n1 : Le Personnage \n2 : La Voix \n3 : Le Colonel \n4 : Scene intro \n5 : Atmosphere \nor type in a word (case sensitive) \n>> ")

try:
    choice=eval(character)
except NameError:
    choice=character
#    print "not a valid choice"
if choice==1:
    lookfor=nom1
elif choice==2:
    lookfor=nom2
elif choice==3:
    lookfor=nom3
elif choice==4:
    lookfor=scen
elif choice==5:
    lookfor=atmosphere
else:
    lookfor=str(choice)
print 'looking for....', lookfor

lookfordict={}
crawler(script, lookfor, lookfordict)

lookfordictOrder = collections.OrderedDict(sorted(lookfordict.items()))
print 'this!', lookfordictOrder

#print "//////////////////////output saved to the file: crawler_for_subtitler.txt"
#print "//////////////////////and a one line version saved to: crawler_oneliner.txt"
while True:
    if any(lookfordict.values()):
        print 'you have', len(lookfordict), 'scenes'
        display=raw_input('which scene do you want to print?\n')
        try:
            selection=eval(display)-1
        except NameError:
            selection=display
    
    
    for i, key in enumerate(lookfordictOrder):
        #print i, key
        if i==selection:
            print key
            print lookfordictOrder[key]

