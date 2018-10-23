from cryptography.fernet import Fernet


# function for encrypting text, which takes an argument as what to encrypt
# and returns a dictionary containing the generated encrypted text and
# a key that is required to decrypt the encrypted text
def encrypt(text):
    # generating a key required for encryption
    encryption_key = Fernet.generate_key()
    magic_box = Fernet(encryption_key)

    # generating encrypted text from given text (in byte code)
    encrypted_text = magic_box.encrypt(str.encode(text))

    # returning a dictionary containing both (encrypted text and key)
    return {"cipher_text": encrypted_text, "key": encryption_key}


# function for decrypting text, which takes 2 arguments,
# 1st as what to decrypt and 2nd as the key through which encryption was done.
# It returns a decrypted text
def decrypt(encrypted_text, key):
    magic_box = Fernet(key)

    # result is generated in byte code
    byte_decrypted_pass = magic_box.decrypt(encrypted_text)

    # byte code to string conversion
    decrypted_text = byte_decrypted_pass.decode()
    return decrypted_text
