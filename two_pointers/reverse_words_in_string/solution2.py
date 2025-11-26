def reverse_words(sentence):
    s = sentence.split(" ")
    b = []
    for i in range(len(s) - 1, -1, -1):
        if s[i] != "":
            b.append(s[i])
    return " ".join(b)
