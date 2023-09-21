import string
from typing import List


def vigenere(key:List[int], message: str) -> str:
    """
    from https://justcryptography.com/vigenere-cipher-python-implementation/
    :param key: list of integer shifts
    :param message: string
    :return:
    """
    message = message.lower()
    message = "".join(c for c in message if c in string.ascii_lowercase)
    m = len(key)
    cipher_text = []
    for i in range(len(message)):
        letter = message[i]
        k = key[i % m]
        cipher_text.append(chr((ord(letter) - 97 + k) % 26 + 97))
    return "".join(cipher_text)


encrypt = vigenere


def decrypt(key,message):
    key = [-k for k in key]
    return vigenere(key,message)


def key(k:str):
    return [ord(letter) - 97 for letter in k]



if __name__ == '__main__':
  # a sample of encryption and decryption
  print('Encripting')
  k = 'vestal'
  mk = key(k)

  cipher_text = encrypt(mk, 'hello world')
  print('cipher text: ', cipher_text)

  print ('Decrypting')

  plain_text =  decrypt(mk, cipher_text)
  print ('Plain text: ', plain_text)
