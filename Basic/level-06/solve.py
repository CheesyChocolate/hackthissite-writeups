def decrypt_password(password):
    decrypted = ''
    for i, c in enumerate(password):
        decrypted += chr(ord(c) - i)
    return decrypted


if __name__ == "__main__":
    print(decrypt_password('4bciif7m'))
