'''
using dictionaries to translate text
'''
from cecilialib import translated

text = "My favorite fruits are mango and kiwi ," \
        " because it tastes delicious."
list_text = text.split(' ')
print(list_text)

# # # put back the list of words into a text
new_text = ''
for word in list_text:
    new_text = new_text + ' ' + word

print(new_text)

# # build a dictionary
mydictionary = {'mango': input("some fruit"),'kiwi': input("some other fruit or thing"),'delicious': input("an adjective")}
print(mydictionary.keys())
print(mydictionary['mango'])

print(len(mydictionary))

for i in range(len(list_text)):
    for key in mydictionary.keys():
         if list_text[i] == key:
             list_text.remove(list_text[i])
             list_text.insert(i, mydictionary[key])
# put back the list of words into a text
new_text = ''
for word in list_text:
     new_text = new_text + ' ' + word

print(new_text)

# print(' '.join(list_text))
# print(mydictionary[mango])
# print()
print(mydictionary.get('mango'))

def translated(text1, dict1):
     list_text = text1.split()
     new_text = []
     for word in list_text:
         translation = dict1.get(word)
         new_text.append(translation if translation else word)
     return ' '.join(new_text)

print(translated(text, mydictionary))






