import sys
import hashlib
import pwnd as pawned


def main(argv):
    password = "".join(argv)
    h = hashlib.sha1(password.encode()).hexdigest().upper()

    pwnd = pawned.Pwnd(h)
    pwnd.check()


if __name__ == "__main__":
    main(sys.argv[1:])
