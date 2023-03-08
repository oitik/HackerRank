words = {}
length = 0
for i in range(int(input())):
    x = input()
    if x in words:
        words[x] += 1
    else:
        length += 1
        words[x] = 1
print(length)
for val in words:
    print(words[val], end=' ')
# Good luck mates
