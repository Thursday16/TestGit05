# app.py

def reduce_to_20_chars(input_string):
    """
    Reduces a 40-character string to a 20-character string by taking the first 20 characters.

    :param input_string: The 40-character input string
    :return: The reduced 20-character string
    """
    if len(input_string) < 20:
        raise ValueError("Input string must be at least 20 characters long")

    return input_string[:20]


def convert_to_original(input_string, original_string):
    """
    Converts a reduced 20-character string back to the original 40-character string by padding it with spaces
    and appending it to the original string.

    :param input_string: The reduced 20-character string
    :param original_string: The original 40-character string
    :return: The original 40-character string
    """
    if len(input_string) != 20:
        raise ValueError("Input string must be exactly 20 characters long")

    return original_string + input_string.ljust(20)


def run():
    original_string = "ABCD1234EFGH5678IJKL9012MNOP3456QRST"
    reduced_string = reduce_to_20_chars(original_string)
    print("Reduced String:", reduced_string)

    # To convert it back to the original string:
    restored_string = convert_to_original(reduced_string, original_string)
    print("Restored String:", restored_string)