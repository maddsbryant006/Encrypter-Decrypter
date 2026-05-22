import sys
from caesarcipher import CaesarCipher

encode_request = ""
decode_request = ""
encoder_key = 0
decoder_key = 0

def option_print():
    print("1. Encode a Phrase")
    print("2. Decode a Phrase")
    print("3. Quit")
    print("\nMake a selection: ")

def encode(phrase, key):
    new_phrase = CaesarCipher(phrase, offset=key)
    print(new_phrase.encoded)

def decode(phrase, key):
    new_phrase = CaesarCipher(phrase, offset=key)
    print(new_phrase.decoded)

print("Ceaser Cipher Encoder + Decoder")
print("-------------------------------")
option_print()
user_input = int(input())

while user_input != 3:
    if user_input == 1:
        #encoding
        print("Input the phrase you'd like to encode")
        encode_request = input()
        print("Input cipher key: ")
        encoder_key = int(input())
        encode(encode_request, encoder_key)
        option_print()
        user_input = int(input())
    else:
        #decoding
        print("Input the phrase you'd like to decode")
        decode_request = input()
        print("Input cipher key: ")
        decoder_key = int(input())
        decode(decode_request, decoder_key)
        option_print()
        user_input = int(input())
