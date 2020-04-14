#. В третьей программе знак короткого тире «–» перед длинным «—» означает 0, наоборот – 1. 
import codecs
import random

def spec_sym(s, word):
    temp1 = ''
    temp2 = ''
    for i in range(len(word)):
        temp1 += bin(ord(word[i])-848)[2::]    
    i = 0
    k = 0
    #long dash = 1, short dash = 0
    while k < len(temp1):
        if s[i] == '—' and temp1[k] == '1':
            temp2 += '—–'
            k += 1
        elif s[i] == '—' and temp1[k] == '0':
            temp2 += '–—'
            k += 1
        elif ord(s[i]) != 13:
            temp2 += s[i]
        i += 1
    temp2 += chr(8195) # сперциальный симбол 
    j = i
    for j in range(len(s)):
        if s[j] == '—' and random.getrandbits(1) == 0: #random.getrandbits(1) return 0 or 1
            temp2 += '—–'
        elif s[j] == '—' and random.getrandbits(1) == 1:
            temp2 += '–—'
        else:
            temp2 += s[j]
            
    f = codecs.open('output.txt', 'w', 'utf-8')
    f.write(temp2)
    f.close()        

def decode():
    f = codecs.open('output.txt', 'r', 'utf-8')
    s = f.read()
    f.close()
    tmp = ''
    result = ''
    i = 0
    k = s.find(chr(8195)) #найти прециальный симбол
    while i < k:
        if s[i] == '—':
            tmp += '1'
            i += 2
        elif s[i] == '–':
            tmp += '0'
            i += 2
        else:
            i += 1
    s1 = [tmp[x:x+8] for x in range(0, len(tmp), 8)]
    for i in s1:
        result += chr(int(i, 2)+848)
    f = codecs.open('decoded.txt', 'w', 'utf-8')
    f.write(result)
    f.close()    

f = codecs.open('input.txt', 'r', 'utf-8')
s = f.read()
f.close()
opt = input('Type 1 for encode and 2 for decode: ')
if opt == '1':
    word = input('Input word: ')
    spec_sym(s, word)
elif opt == '2':
    decode()
