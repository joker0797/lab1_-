
#=============Программа 1:Метод замены символов одинакового начертания============
import codecs # модуль для открыта файла
#-----------------
# in ACSII table russian alphabet 'a' = 1072 .... 'я' = 1104
def changesym(s, word): #encode symbol in file 
    temp1 = '' 
    temp2 = ''
    k = 0
    for i in range(len(word)): #range(start, stop[, step])
        temp1 += bin(ord(word[i])-848)[2::] # alphabet-> binany 
    #русская о = 1, русская е = 0
    i = 0
    while k < len(temp1):
        if s[i] == 'о' and temp1[k] == '1':
            temp2 += 'o'
            k += 1
        elif s[i] == 'е' and temp1[k] == '0':
            temp2 += 'e'
            k += 1
        else:
            temp2 += s[i]
        i += 1
    temp2 += s[i::]
    f = codecs.open('output.txt', 'w', 'utf-8')
    f.write(temp2)
    f.close()    
    
#-------------------------    
def decode():
    f = codecs.open('output.txt', 'r', 'utf-8')
    s = f.read()
    f.close()
    temp = ''
    result = ''
    for i in range(len(s)):
        if s[i] == 'o':
            temp += '1'
        if s[i] == 'e':
            temp += '0'
    s1 = [temp[x:x+8] for x in range(0, len(temp), 8)]
    for i in s1:
        result += chr(int(i, 2)+848) #binany -> alphabet
    
    f = codecs.open('decoded.txt', 'w', 'utf-8')
    f.write(result)
    f.close()    

#-------------------------------
f = codecs.open('input.txt', 'r', 'utf-8') #open file input.txt
s = f.read()
f.close()
opt = input('Type 1 for encode and 2 for decode: ')
if opt == '1':
    word = input('Input word: ')
    changesym(s, word)
elif opt == '2':
    decode()
