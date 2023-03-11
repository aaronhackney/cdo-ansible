#!/usr/bin/python3
# Requires: pycryptodome
import sys
import json
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


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
    main(username, password, public_key)
