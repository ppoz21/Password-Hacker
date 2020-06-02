l1 = input()
l2 = sum(int(input()).to_bytes(2, byteorder='little'))
message = ''
for letter in l1:
    temp = ord(letter) + l2
    message += chr(temp)

print(message)
