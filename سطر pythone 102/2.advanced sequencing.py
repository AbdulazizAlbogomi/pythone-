#indexing 
import secrets


alphabet = 'abcdefghijklmnopqstuvwxyz'
print(alphabet[5])
print(alphabet[-1])

#slicing 
text= 'this is pythone'
print(text[0:8])
print(text[0:7:2])

#index يجيب اول تطابق
text =' hello how are you'
print(text.index('h'))

#length 
print(len(alphabet))

#count 

print(text.count('h'))

#in it comes back with yes or no 

print('you' in text)

#دمح
FIRSTN = 'ZEZO'
SECN = 'AHMED'
print(FIRSTN + ' ' + SECN*6)
