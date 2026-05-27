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
    cipher_phrase = CaesarCipher(phrase, offset=key)
    print(cipher_phrase.encoded)

def encode2(phrase, key):
    #encode phrase as a ceasar cipher
    cipher_phrase = CaesarCipher(phrase, offset=key)
    cipher_phrase = cipher_phrase.encoded

    #encode phrase as base64
    cipher_b64_phrase = base64.b64encode(cipher_phrase.encode('ascii'))
    print(cipher_b64_phrase.encode('ascii'))

def encode3(phrase, key):
    #encode phrase as a ceasar cipher
    cipher_phrase = CaesarCipher(phrase, offset=key)
    cipher_phrase = cipher_phrase.encoded

    #encode phrase as base64
    cipher_b64_phrase = base64.b64encode(cipher_phrase.encode('ascii'))

    #encode phrase as base32
    cipher_b64_b32_phrase = base64.b32encode(cipher_b64_phrase)
    print(cipher_b64_b32_phrase.encode('ascii'))


def decode1(phrase, key):
    #Decrypt ceasar cipher
    cipher_phrase = CaesarCipher(phrase, offset=key)
    print(cipher_phrase.decoded)

def decode2(phrase, key):
    #decrypt b64
    b64_decrypt = base64.b64decode(phrase.encode('utf-8'))
    b64_decrypt = b64_decrypt.decode('utf-8')

    #Decrypt ceasar cipher
    cipher_decrypt = CaesarCipher(b64_decrypt, offset=key)
    print(cipher_decrypt.decoded)

def decode3(phrase, key):
    #decrypt b32
    b32_decrypt = base64.b32decode(phrase.encode('utf-8'))

    #decrypt b64
    b64_decrypt = base64.b64decode(b32_decrypt)
    b64_decrypt = b64_decrypt.decode('utf-8')
    
    #Decrypt ceasar cipher
    cipher_decrypt = CaesarCipher(b64_decrypt, offset=key)
    print(cipher_decrypt.decoded)

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


