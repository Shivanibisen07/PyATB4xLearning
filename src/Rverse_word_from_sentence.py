def reverse_third_word(sentence):
    words = sentence.split()

    words[2] = words[2][::-1]

    return ' '.join(words)

sentence = input("Enter the Sentence- ")
result = reverse_third_word(sentence)
print("Modified sentence:",result)