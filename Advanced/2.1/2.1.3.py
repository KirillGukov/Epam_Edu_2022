import string

text = input()
simb = string.printable
ru_simb = 'а', 'б', 'в', 'п', 'р'
count = text.count(simb) + text.count(ru_simb)
print(count)