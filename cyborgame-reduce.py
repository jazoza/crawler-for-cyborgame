import codecs, collections, sys

try:
    fin=codecs.open("CYBORGAME-edited.txt", "r", encoding="utf-8")
    try: 
        script=fin.readlines()
    finally:
        fin.close()
except IOError:
    pass

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
