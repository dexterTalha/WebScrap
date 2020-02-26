def split(word):
    return [char for char in word]

inp = "hellomorning"
words = split(inp)
w = slice(0, len(words), 3)
print(inp[w])
count = 0
# for word in words:

