import time

#This is an encryption algorithm called shift cipher
#We will use the method called caesar cipher, which was used by caesar before.


def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        #Basically we need a plain text and a key to encrypt the plaintext
    plainText = str(input("Type a message that you want to encrypt : "))
        #The key is the shift number
    key = int(input("Enter your key number : "))

    resultEnc = algorithm(plainText, key, alphabet)

    print(f'Message encrypted. Crypted text is : {resultEnc}')
    time.sleep(3)

    q = str(input("Would you like to decrypt the crypted text? (Y/N) : "))

    if q.upper() == "Y" : 
        resultDec = dec_algorithm(resultEnc, key, alphabet)

        print(f'Text decrypted. Plain text: {resultDec}')
    else:
        print()

    return plainText, key, alphabet

#Now we will use the algorithm to encrypt the plaintext

def algorithm(plainText, key, alphabet):
    crypted_text = ""  #An empty list to save encrypted letters

    letters = [letter for letter in plainText if letter.isalpha()] #we check the place of the letter in the alphabet 

    for letter in letters:                      #Finding the numbers of letters in the alphabet
        order = alphabet.index(letter.upper())

        new_order = (order + key)%26 #Encryption algorithm

        crypted_text += alphabet[new_order] #Adding the encrypted letter to the encrypted text
    return crypted_text

def dec_algorithm(crypted_text, key, alphabet): #Now we wil decrypt our encrypted plain text (crypted text)
    letters = [letter for letter in crypted_text if letter.isalpha()] #we check the place of the letter in the alphabet

    decrypted_text = ""  #An empty list to save decrypted letters


    for letter in letters:
        order = alphabet.index(letter.upper())

        new_order = (order - key)%26 #Decryption algorithm
        decrypted_text += alphabet[new_order]

    return decrypted_text


if __name__ == "__main__": main()



