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

def crawler(word, wdict):
    for i, line in enumerate(script):
    #    print line 
        if word in line:
            #print "found in line: ", i
            key=word+" "+str(i)
            if choice>4: #stupid way
                dialogue=line.upper()
            elif "(" in line and "e)" not in line:
                dialogue=script[i+2].upper()
            else:
                dialogue=script[i+1].strip('\n').upper()
            print "dialogue", dialogue
            fout.write(dialogue+"\n\n")
            fout_oneliner.write(dialogue+"\t\t",)
            wdict[key]=dialogue #.decode('utf-8')
    return wdict

### handwork....

nom1="LE PERSONNAGE DE ROMAN"
nom2="LA VOIX"
nom3="LE COLONEL"
scen="#SCENE DESCRIPTION"
atmosphere="LUMIERE"
choose=raw_input("choose the character/scene: \n1 : Le Personnage \n2 : La Voix \n3 : Le Colonel \n4 : Scene intro \n5 : Atmosphere \nor type in a word (case sensitive) \n>> ")

try:
    choice=eval(choose)
except NameError:
    choice=choose
#    print "not a valid choice"
if choice==1:
    print choice, "success"
    lookfor=nom1
    print lookfor
elif choice==2:
    lookfor=nom2
elif choice==3:
    lookfor=nom3
elif choice==4:
    lookfor=scen
elif choice==5:
    lookfor=atmosphere
else:
    lookfor=choice
print lookfor

lookfordict={}
lookfordictOrder = collections.OrderedDict(sorted(lookfordict.items()))
#print lookfordictOrder

crawler(lookfor, lookfordict)

print "//////////////////////output saved to the file: crawler_for_subtitler.txt"
print "//////////////////////and a one line version saved to: crawler_oneliner.txt"
