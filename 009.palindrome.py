to = "maham"
p = False
q = len(to)

for i in range(q):
    if to[i] != to[q - i - 1]:
        p = True
        break

if p:
    print(to, "is not a palindrome")
else:
    print(to, "is palindrome")
