word = input()

# print(word [::-1])

# решение в материалите: (ако print е в цикъла, принтира всяка итерация)
reversed_word = ""
for i in range (len(word) -1, -1, -1):
    reversed_word += word[i]
print(reversed_word)

    # решение Марио
for i in range(len(word) - 1, -1, -1):
    print(word[i], end='')
