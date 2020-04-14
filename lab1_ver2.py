import codecs

def gap(s, word):
    temp1 = ''
    temp2 = ''
    for i in range(len(word)):
        temp1 += bin(ord(word[i])-848)[2::]  
    i = 0
    k = 0
    #2 пробела = 1, 1 пробел = 0
    while k < len(temp1):
        if ord(s[i]) == 10 and temp1[k] == '1':
            temp2 += '  \n'
            k += 1
        elif ord(s[i]) == 10 and temp1[k] == '0':
            temp2 += ' \n'
            k += 1
        elif ord(s[i]) != 13: #chr(13) - \r -carriage return
            temp2 += s[i]
        i += 1
    temp2 += s[i::]   
    f = codecs.open('output.txt', 'w', 'utf-8')
    f.write(temp2)
    f.close()        

def decode():
    f = codecs.open('output.txt', 'r', 'utf-8')
    s = f.read()
    f.close()
    temp = ''
    result = ''
    for i in range(len(s)):
        if s[i] == '\n':
            if s[i-1] == ' ':
                if s[i-2] == ' ':
                    temp += '1'
                else:
                    temp += '0'
    s1 = [temp[x:x+8] for x in range(0, len(temp), 8)]
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
    gap(s, word)
elif opt == '2':
    decode()
