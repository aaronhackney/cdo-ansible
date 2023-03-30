import os

def load_package(lib_test, package):
    try:
        __import__(lib_test)
    except ImportError:
        os.system(f"{sys.executable} -m pip install {package} --user")

if __name__ == "__main__":
    load_package("Crypto.PublicKey", "pycryptodome")