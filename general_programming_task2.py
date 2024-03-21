def encode_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Initialize an empty list to store the encoded words
    encoded_words = []

    # Iterate through each word in the sentence
    for word in words:
        # Check if the length of the word exceeds 3 letters
        if len(word) > 3:
            # Reverse the word and add it to the encoded list
            encoded_words.append(word[::-1])
        else:
            # If the length of the word is 3 letters or less, add it as it is
            encoded_words.append(word)

    # Join the encoded words back into a sentence
    sentence = ' '.join(encoded_words)

    return sentence


# Test the function with the provided example
input_sentence = "AT DAWN LOOK TO THE EAST"
encoded_sentence = encode_sentence(input_sentence)
print(encoded_sentence)  # Output: "AT NWAD KOOL TO THE TSAE"
