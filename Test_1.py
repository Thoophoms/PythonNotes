word = "hello"
word_list = []

for i in word:
    word_list.append(i)
    print(word_list)

if "h" in word_list:
    index_change = word_list.index("h")
    word_list[index_change] = "X"
    print(word_list)
    okay = "".join(word_list)
    print(okay)