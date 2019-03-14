import sys
import hashlib
import pwnd as pawned


def main(argv):
    password = "".join(argv)
    hash = hashlib.sha1(password.encode())

    pwnd = pawned.Pwnd(hash.hexdigest())
    pwnd.check()


if __name__ == "__main__":
    main(sys.argv[1:])
