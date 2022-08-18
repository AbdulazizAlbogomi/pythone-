#find 
text = 'why dose evryone use hello world as there first programing statment'
print(text.find('world'))
print(text.rfind('world'))

#تحويل النص إلى قائمة using split 
text2 = 'a b c d e f g'
string_to_list = text2.split(',')
print(string_to_list)

#التحويل إلى نص
listToStr = ' '.join(string_to_list)
print(listToStr)

#التحقق من النص
v = 'a989'
print(v.isalnum()) #if there is only text and num 
print(v.isdigit()) #if there is num only

#replace
v3 = '1/n2/n3/n4/n'
print(v3.replace('/n' , ','))

#strip 

