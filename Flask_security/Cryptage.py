import string


def encode(input, shift):
    # create an empty string
    foo = ''
    # a for loop to shift the letters by the shift input
    for x in input:
        # changes only ascii letters
        if x in string.ascii_letters:
            # upper case end of alphabet, to loop back to A
            if ord(x) > ord("Z") - shift and ord(x) <= ord("Z"):
                new_ord = ord(x) + shift - 26
            # lower case end of alphabet
            elif ord(x) > ord("z") - shift and ord(x) <= ord("z"):
                new_ord = ord(x) + shift - 26
            else:
                new_ord = ord(x) + shift
        # other characters will remain unchanged
        else:
            new_ord = ord(x)

        new_chr = chr(new_ord)
        foo += new_chr
    return foo


def decode(input, shift):
    # create an empty string
    foo = ''
    # a for loop to shift the leters by the shift input
    for x in input:
        # changes only ascii letters
        if x in string.ascii_letters:
            # upper case start of alphabet, to loop back to Z
            if ord(x) - shift < ord("A") and ord(x) >= ord("A"):
                new_ord = ord(x) - shift + 26
            # lower case end of alphabet
            elif ord(x) - shift < ord("a") and ord(x) >= ord("a"):
                new_ord = ord(x) - shift + 26
            else:
                new_ord = ord(x) - shift
        # other characters will remain unchanged
        else:
            new_ord = ord(x)
        new_chr = chr(new_ord)
        foo += new_chr
    return foo
