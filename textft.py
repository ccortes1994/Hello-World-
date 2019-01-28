ptext = " Once upon a time, there was a kid named Jack who believed he would be forever alone.\
He had nowhere to go and no place to call home. The only friend he had was the man on the moon,\
although he too would sometimes go away. Then one night as Jack closed his eyes he saw a shadow flying high.\
He came to him with the sweetest smile and told him he wanted to talk to him for awhile.\
He said,' Peter Pan is what they call me I promise that you will never be lonely.'\
Ever since then Jack became a lost boy from Neverland always hanging out with Peter Pan."

list_ptext = ptext.split()
#print(list_ptext)

new_ptext = ''
for word in list_ptext:
    new_ptext = new_ptext + ' ' + word
print(new_ptext)

pdict = {"Jack": input("boy name"),"flying": input("synonym of flying"),
         "shadow": input("synonym for shadow"),"Neverland": input("another place")}


for i in range(len(list_ptext)):
    for key in pdict.keys():
         if list_ptext[i] == key:
             list_ptext.remove(list_ptext[i])
             list_ptext.insert(i, pdict[key])


def translated(text1, dict1):
    list_ptext = text1.split()
    new_ptext = []
    for word in list_ptext:
        translation = dict1.get(word)
        new_ptext.append(translation if translation else word)
    return ' '.join(new_ptext)








