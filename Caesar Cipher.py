#Caesar Cipher

a=input()
s=''
for i in a:
    if 'a' <= i <= 'z':
        s+=chr((ord(i) - ord('a') + 3) % 26 + ord('a'))
    elif 'A' <= i <= 'Z':
        s+=chr((ord(i)-ord('A')+3) %26 + ord('A'))
    else:
        s+=i
print(s)

# Test cases for Caesar cipher with shift 3:
# Input: hello         Output: khoor
# Input: abc xyz       Output: def abc
# Input: Python 3.8!   Output: Sbwkrq 3.8!
# Input: QWERTY        Output: TZHUWB
