#!/usr/bin/python
import sys,getopt
def encrypt(plainText, key, lookupTable):
    cipher = ''
    count = 0
    for p in plainText:
        cipher += lookupTable[p][key[count % len(key)]]
        count = count + 1

    return cipher

def decrypt(cipher, key, lookupTable):
    characterString = ''
    count = 0
    for c in cipher:
        characterString += lookupTable[c][key[count % len(key)]]
        count = count + 1

    return characterString
def createEncryptLUT(characters, emojis):
    rotatableEmoljis = emojis

    lookup = {}
    for c in characters:
        lookup[c] = {}
        count = 0
        for e in emojis:
            lookup[c][e] = rotatableEmoljis[count]
            count = count + 1

        rotatableEmoljis = rotatableEmoljis[-1:] + rotatableEmoljis[:-1]

    return lookup


def createDecryptLUT(characters, emojis):
    rotatableCharacters = characters

    lookup = {}
    for e in emojis:
        lookup[e] = {}
        count = 0
        for inTable in emojis:
            lookup[e][inTable] = rotatableCharacters[count]
            count = count + 1
        rotatableCharacters = rotatableCharacters[-1:] + rotatableCharacters[:-1]

    return lookup

def main():
    emojis = ['😀', '😂', '😍', '😛', '😠', '😗', '😮', '🍆', '😎', '😜', '😓', '😭', '👏', '😇', '😈', '💩', '👌', '🍔',
              '🍟', '🍕', '👾', '🎲', '💘', '🍑', '👍', '😊']

    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']

    encryptLookup = createEncryptLUT(characters, emojis)
    decryptLookup = createDecryptLUT(characters, emojis)

    print('Valid emojis are:')
    print(emojis)
    print('Valid letters are:')
    print(characters)


    choice = ''
    while choice != 'e' and choice != 'd' and choice != 'q':
        choice = input('Would you like to encrypt or decrypt?\nEncrypt: e\n Decrypt d:\n Quit q\n')



    if  choice != 'q':
        string = input('Please enter your input string!\n')
        key = input('Please enter your key!\n')
        if choice == 'e':
            print(encrypt(string, key, encryptLookup))
        if choice == 'd':
            print(decrypt(string, key, decryptLookup))




if __name__ == "__main__":
    main()