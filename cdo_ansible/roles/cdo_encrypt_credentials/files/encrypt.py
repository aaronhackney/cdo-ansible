#!/usr/bin/python3
# Requires: pycryptodome
import pip
import sys
import json
import base64

def load_package(lib_test, package):
    try:
        print("Attempting to import needed library...")
        __import__(lib_test)
    except ImportError:
        print(f"Library {lib_test} not found attempting to install...")
        pip.main(['install', package])
    
def main(username, password, public_key):
    key = RSA.importKey(base64.b64decode(public_key))
    encryptor = PKCS1_v1_5.new(key)
    print(
        json.dumps(
            {
                "username": base64.b64encode(encryptor.encrypt(username.encode(encoding="UTF-8"))).decode(),
                "password": base64.b64encode(encryptor.encrypt(password.encode(encoding="UTF-8"))).decode(),
            }
        )
    )


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    public_key = sys.argv[3]
    load_package("Crypto.PublicKey", "pycryptodome")
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_v1_5
    main(username, password, public_key)
