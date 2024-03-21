import re


def remove_extra_whitespace(sentence):
    # Use regular expression to replace multiple whitespaces with a single whitespace
    cleaned_sentence = re.sub(r'\s+', ' ', sentence)

    return cleaned_sentence


def morse_code_decoder(code):
    # Define the Morse code dictionary
    morse_code_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z'
    }

    # Split the Morse code into individual characters and words
    morse_chars = code.split(' ')

    decoded_message = ''
    for morse_char in morse_chars:
        if morse_char == '':
            decoded_message += ' '  # Add space for word separation
        else:
            decoded_message += morse_code_dict.get(morse_char, '')  # Get corresponding English alphabet

    return remove_extra_whitespace(decoded_message)
