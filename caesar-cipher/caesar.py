"""
Name: Jax Jiang
PennKey: jiang13
Recitation: 201
Program Execution: python caesar.py encrypt text_file.txt G
                   python caesar.py decrypt encrypted_text_file.txt G
                   python caesar.py crack encrypted_file.txt english.txt
Description: This program implements a Caesar cipher. It can encrypt or decrypt
             a text file using a key letter (A to Z), and it can crack an
             encrypted file by trying all 26 shifts and choosing the decryption
             whose letter frequencies best match English (using english.txt).
"""

import sys


def string_to_symbol_list(message: str) -> list[int]:
    """
    Description: converts a string to a symbol list, where each element of the
                 list is an integer encoding of the corresponding element of
                 the string.
    Input:  the message text to be converted
    Output: the encoding of the message into a list of integers
    """

    # creating a variable to represent the list of int
    lst = []

    # converting each character in string into symbol and adding to the
    # list lst
    # n.upper() is used instead of n so all characters are capitalized
    # to ensure correct conversion
    for n in message:
        if 'A' <= n <= 'Z' or 'a' <= n <= 'z':
            number = ord(n.upper()) - 65
        else:   # non-letter: encode consistently but it will not be shifted
            number = ord(n) - 65
        lst.append(number)

    # return and store the value
    return lst


def symbol_list_to_string(symbol_list: list[int]) -> str:
    """
    Description: converts a list of symbols to a string, where each element
                 of the list is an integer encoding of the corresponding
                 element of the string.
    Input:  integer encoding of the message, stored in a list of integers.
    Output: the message text as a string
    """

    res = ""

    # converting each symbol in list into character and adding to the string
    for n in symbol_list:
        letter = chr(n + 65)
        res += letter

    # return and store the value
    return res


def shift(symbol: int, offset: int) -> int:
    """
    Description: shifts a symbol representing a letter (0 to 25) by the given
                 offset (between 0 and 25), adding offset symbols
                 outside the range 0 to 25 are returned unchanged
    Input:  symbol: an integer encoding of a character
            offset: an integer shift amount
    Output: the shifted symbol (int) if symbol is between 0 and 25, otherwise
            the original symbol
    """

    # determine of symbol is an alphabet
    if 0 <= symbol <= 25:
        res = (symbol + offset) % 26
    else:    # if non-alphabet: leave unchanged
        res = symbol

    return res


def unshift(symbol: int, offset: int) -> int:
    """
    Description: unshifts a symbol representing a letter (0 to 25) by the given
                 offset (between 0 and 25), subtracting the offset symbols
                 outside the range 0 to 25 are returned unchanged
    Input:  symbol: an integer encoding of a character
            offset: an integer unshift amount
    Output: the unshifted symbol (int) if symbol is between 0 and 25,
            otherwise the original symbol
    """

    # determine of symbol is an alphabet
    if 0 <= symbol <= 25:
        res = (symbol - offset) % 26
    else:    # if non-alphabet: leave unchanged
        res = symbol

    # returns a value
    return res


def encrypt(message: str, key: int) -> str:
    """
    Description: encrypts a message by converting it to a cipher by shifting
                 each letter by given key
    Input: message: a string of message to be encrypted
           key: the integer shift amount
    """

    # convert the message into a list of integers
    symbol_lst = string_to_symbol_list(message)

    # for each symbol(int) in list, shift to encrypt
    shifted_symbol_lst = []
    for symbol in symbol_lst:
        shifted_symbol = shift(symbol, key)
        shifted_symbol_lst.append(shifted_symbol)

    # convert the shifted list to cipher
    res = symbol_list_to_string(shifted_symbol_lst)

    # returns a value
    return res


def decrypt(cipher: str, key: int) -> str:
    """
    Description: decrypts a cipher by converting it to the original message
                 by unshifting each letter by given key
    Input: cipher: the encrypted string to be decrypted
           key: the integer unshift amount
    """

    # convert the message into a list of integers
    symbol_lst = string_to_symbol_list(cipher)

    # for each symbol(int) in list, unshift to decrypt
    unshifted_symbol_lst = []
    for symbol in symbol_lst:
        unshifted_symbol = unshift(symbol, key)
        unshifted_symbol_lst.append(unshifted_symbol)

    # convert the unshifted list to original message
    res = symbol_list_to_string(unshifted_symbol_lst)

    # returns a value
    return res


def get_letter_frequencies(frequencies_filename: str) -> list[float]:
    """
    Description: reads a file containing 26 lines of English letter frequencies
                 (one per line, in order from 'A' to 'Z') and returns them as
                 a list of floats
    Input: frequencies_filename: name of the file containing the frequencies
    Output: a list of 26 floats where index 0 is the frequency of letter 'A',
            index 1 is the frequency of 'B', and so on up to 'Z'
    """

    float_lst = []

    # open and access given file, adding the frequencies to the list of float
    file = open(frequencies_filename, "r")
    lines_lst = file.readlines()
    for line in lines_lst:
        float_lst.append(float(line.strip()))

    file.close()

    # returns a value
    return float_lst


def find_frequencies(symbols: list[int]) -> list[float]:
    """
    Description: calculates the frequency of each letter (A to Z) in the
                 given symbol list by dividing the number of times a letter
                 appears by the total number of all letters ONLY present
    Input: a list of integers(symbols) representing encoded characters
    Output: a list of 26 floats where index 0 is the frequency of 'A',
            index 1 is the frequency of 'B', and so on.
            Non-letter symbols (outside range 0 to 25) are ignored.
    """

    counts_lst = [0] * 26
    count = 0   # number of letters

    # determine number of times each letter appeared
    # and total count of all letters
    for i in symbols:
        if 0 <= i <= 25:
            counts_lst[i] += 1
            count += 1

    # if no letter is present (total number of all letters = 0)
    if count == 0:
        return [0.0000] * 26

    # final list of frequencies (in float)
    freq_lst = [f / count for f in counts_lst]

    # returns a value
    return freq_lst


def score_frequencies(
    expected_frequencies: list[float], actual_frequencies: list[float]
) -> float:
    """
    Description: calculates a score representing how different two letter
                 frequency distributions are (lower score suggests a
                 closer match)
    Input: expected_frequencies: a list of 26 floats representing
           expected English letter frequencies
           actual_frequencies: a list of 26 floats representing
           the actual frequencies from a given text
    Output: a float equal to the sum of the absolute differences
            between corresponding entries in the two lists
    """

    score = 0.0000

    # finding sum of differences
    for i in range(26):
        each_diff = abs(expected_frequencies[i] - actual_frequencies[i])
        score += each_diff

    # returns a value
    return score


def crack(cipher: str, english_filename: str) -> str:
    """
    Description: attempts to break a Caesar cipher without knowing the
                 key by trying all 26 possible shifts and selecting the
                 decryption whose letter frequency distribution most
                 closely matches standard English letter frequencies
    Input: cipher: the encrypted message (a string)
           english_filename: name of a file containing 26 English letter
           frequencies (A to Z), one per line (such as the given file
           english.txt)
    Output: the decrypted message (string) whose letter frequency
            distribution most closely matches the English letter
            frequencies (lowest score)
    """

    # derive a frequency list of english.txt
    english_freq = get_letter_frequencies(english_filename)
    best_score = float('inf')
    best_msg = ""

    # try each letter shift from 0(A) to 25(Z)
    for i in range(26):
        decrypted = decrypt(cipher, i)
        decrypted_lst = string_to_symbol_list(decrypted)
        decrypted_freq = find_frequencies(decrypted_lst)
        new_score = score_frequencies(english_freq, decrypted_freq)

        # determines the lowest score
        if new_score < best_score:
            best_score = new_score
            best_msg = decrypted

    # returns a value
    return best_msg


def main():
    """
    Description: the program performs Caesar cipher encryption, decryption,
                 or frequency-based cracking depending on the command-line
                 action provided by the user.
    """

    # reads from command line
    action = sys.argv[1]
    filename = sys.argv[2]
    file = open(filename, "r")
    message = file.read()
    file.close()

    # determine whether to encrypt, decrypt or crack
    match action:
        case "encrypt":
            # converts key from A–Z to 0–25
            key = ord(sys.argv[3].upper()) - 65
            res = encrypt(message, key)
        case "decrypt":
            # converts key from A–Z to 0–25
            key = ord(sys.argv[3].upper()) - 65
            res = decrypt(message, key)
        case "crack":
            res = crack(message, sys.argv[3])
        case _:
            print("Invalid action")
            return

    # prints out the results of encrypting, decrypting or cracking
    print(res)


# This snippet sets the main() function as the entry-point to the program.
if __name__ == "__main__":
    main()
