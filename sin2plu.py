import re

num = int(input())

words = [input() for _ in range(num)]
"""
for word in words:
    if ('s','sh','ch','o','x') in word:
        print("in")
    #word.sub('[a-z]*ch', 'ches', s))
    """
for word in words:
    if len(word)-word.rfind('s')==1:
        print(word + 'es')
    elif len(word)-word.rfind('sh')==2:
        print(word + 'es')
    elif len(word)-word.rfind('ch')==2:
        print(word + 'es')    
    elif len(word)-word.rfind('o')==1:
        print(word + 'es')
    elif len(word)-word.rfind('x')==1:
        print(word + 'es')
    elif len(word)-word.rfind('f')==1:
        print(word[:-1]+ 'ves')
    elif len(word)-word.rfind('fe')==2:
        print(word[:-2]+ 'ves')
    elif len(word)-word.rfind('y')==1:
        if (word[len(word)-2] == 'a'):
            print(word + 's')
        elif(word[len(word)-2] == 'i'):
            print(word + 's')
        elif(word[len(word)-2] == 'u'):
            print(word + 's')
        elif(word[len(word)-2] == 'e'):
            print(word + 's')
        elif(word[len(word)-2] == 'o'):
            print(word + 's')
        else:
            print(word[:-1] + 'ies')
            
    else:
        print(word + 's')
    
#print(words)
