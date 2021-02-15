import string
A = input()
B = input()

for letter in string.ascii_lowercase:
    if A.count(letter) < B.count(letter):
        print('N')
        break
else:
    print('A')
