# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import business_case_task1
import business_case_task2
import general_programming_task1
import general_programming_task2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    business_case_task1.task_1()

    business_case_task2.task_2()

    # Test the function with the provided Morse code
    morse_code = '.- -   -.. .- .-- -.   .-.. --- --- -.-   - ---   - .... .   . .- ... -'
    decoded_message = general_programming_task1.morse_code_decoder(morse_code)
    print("Decoded message using MORSE: " + decoded_message)  # Output: "AT DAWN LOOK TO THE EAST"

    # Test the function with the provided example
    input_sentence = "AT DAWN LOOK TO THE EAST"
    encoded_sentence = general_programming_task2.encode_sentence(input_sentence)
    print("Encoded Sentence: " + encoded_sentence)  # Output: "AT NWAD KOOL TO THE TSAE"

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
