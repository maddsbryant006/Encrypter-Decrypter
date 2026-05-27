import sys
from caesarcipher import CaesarCipher
import base64

encode_request = ""
decode_request = ""
encoder_key = 0
decoder_key = 0

def main_option_print():
    print("1. Encode a Phrase")
    print("2. Decode a Phrase")
    print("3. Quit")
    print("Make a selection: ")

def secondary_option_print():
    print("1. Level 1")
    print("2. Level 2")
    print("3. Level 3")
    print("Make a selection: ")

def encode1(phrase, key): 
    #encode phrase as a ceasar cipher
    new_phrase = CaesarCipher(phrase, offset=key)
    print(new_phrase.encoded)

def encode2(phrase, key):
    #encode phrase as a ceasar cipher
    new_phrase = CaesarCipher(phrase, offset=key)
    new_phrase = new_phrase.encoded

    #
    new_phrase = base64.b64encode(new_phrase.encode('ascii'))
    print(new_phrase)

def encode3(phrase, key):
    #encode phrase as a ceasar cipher
    new_phrase = CaesarCipher(phrase, offset=key)
    new_phrase = new_phrase.encoded

    #
    new_phrase = base64.b64encode(new_phrase.encode('ascii'))
    new_phrase = base64.b32encode(new_phrase)
    print(new_phrase)


def decode1(phrase, key):
    new_phrase = CaesarCipher(phrase, offset=key)
    print(new_phrase.decoded)

def decode2(phrase, key):
    new_phrase = base64.b64decode(phrase)
    new_phrase = CaesarCipher(new_phrase.decode('utf-8'), offset=key)
    new_phrase = new_phrase.decoded
    print(new_phrase)


def decode3(phrase, key):
    new_phrase = base64.b32decode(phrase)
    new_phrase = base64.b64decode(new_phrase.decode('utf-8'))
    new_phrase = CaesarCipher(new_phrase.decode('utf-8'), offset=key)
    new_phrase = new_phrase.decoded
    print(new_phrase)

print("Ceaser Cipher Encoder + Decoder")
print("-------------------------------")
main_option_print()
user_input = int(input())

while user_input != 3:
    if user_input == 1:
        #encoding
        print("Input the phrase you'd like to encode")
        encode_request = input()
        print("Input cipher key: ")
        encoder_key = int(input())

        print("Please select an encrpytion level")
        secondary_option_print()
        user_input2 = int(input())

        if user_input2 == 1:
            encode1(encode_request, encoder_key)
            main_option_print()
            user_input = int(input())
        elif user_input2 == 2:
            encode2(encode_request, encoder_key)
            main_option_print()
            user_input = int(input())
        elif user_input2 == 3:
            encode3(encode_request, encoder_key)
            main_option_print()
            user_input = int(input())
        else:
            print("Please enter a valid selection")
            print("Please select an encryption level")
            secondary_option_print()
            user_input2 = int(input())

    else:
        #decoding
        print("Input the phrase you'd like to decode")
        decode_request = input()
        print("Input cipher key: ")
        decoder_key = int(input())
        
        print("Please select a decoder level")
        secondary_option_print()
        user_input2 = int(input())

        if user_input2 == 1:
            decode1(decode_request, decoder_key)
            main_option_print()
            user_input = int(input())
        elif user_input2 == 2:
            decode2(decode_request, decoder_key)
            main_option_print()
            user_input = int(input())
        elif user_input2 == 3:
            decode3(decode_request, decoder_key)
            main_option_print()
            user_input = int(input())
        else:
            print("Please enter a valid selection")
            print("Please select a decoder level")
            secondary_option_print()
            user_input2 = int(input())


