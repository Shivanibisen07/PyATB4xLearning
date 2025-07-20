def reverse_third_word(sentence):
    words = sentence.split()

    # Check if the sentence has at least 3 words
    if len(words) < 3:
        return "The sentence has less than 3 words."

    # Reverse the 3rd word
    reversed_word = words[2][::-1]
    words[2] = reversed_word

    # Count character occurrences in reversed word
    char_count = {}
    for char in reversed_word:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the character with maximum frequency
    max_char = max(char_count, key=char_count.get)
    max_freq = char_count[max_char]

    # Final sentence after reversing 3rd word
    modified_sentence = ' '.join(words)

    return modified_sentence, reversed_word, max_char, max_freq

# Input from user
sentence = input("Enter the Sentence- ")
modified_sentence, reversed_word, max_char, max_freq = reverse_third_word(sentence)

print("Modified sentence:", modified_sentence)
print("Reversed 3rd word:", reversed_word)
print(f"Character '{max_char}' occurs the most in the reversed word, {max_freq} times.")