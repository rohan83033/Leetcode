to = "maham"
p = False
length = len(to)

for i in range(length):
    if to[i] != to[length - i - 1]:
        p = True
        break

if p:
    print(to, "is not a palindrome")
else:
    print(to, "is palindrome")
