
def isVowel(char = ""):
    if chr(ord(char.upper())) == chr(ord("A")):
        return True
    if chr(ord(char.upper())) == chr(ord("E")):
        return True
    if chr(ord(char.upper())) == chr(ord("I")):
        return True
    if chr(ord(char.upper())) == chr(ord("O")):
        return True
    if chr(ord(char.upper())) == chr(ord("U")):
        return True



# def LetterChanges(str):
#     # code goes here
#     newWord = ""
#
#     for letter in str:
#         if letter.isalpha():
#             if letter.upper() == 'Z':
#                 newWord = newWord + "A"
#             else:
#                 new_letter = chr(ord(letter) + 1)
#                 if isVowel(new_letter):
#                     newWord = newWord + new_letter.upper()
#                 else:
#                     newWord = newWord + new_letter
#         else:
#             newWord = newWord + letter
#
#     return newWord

def LetterChanges(str):
    # our new string with the modified characters
    newString = ""

    # begin by looping through each character in the string
    for char in str:

        # check if the current character is an alphabetic character
        if char.isalpha():

            # check if character is z
            if char.lower() == 'z':
                char = 'a'

            # if alphabetic character then add 1 to its ASCII value
            # by using the built-in ord function then convert back to character
            else:
                char = chr(ord(char) + 1)

        # if new character is a vowel then capitalize it
        if char in 'aeiou':
            char = char.upper()

        # add this modified character to the new string
        newString = newString + char

    return newString


print(LetterChanges("fun times!"))