import sys

VERSION = '0.1.0'
def main():
    # cli args
    args = sys.argv[1:]

    if len(args) == 0:
        print("s",VERSION)
        print("for help:")
        print(" s help")
    elif len(args) == 1:
        if args[0] == "help":
            print("s commands:")
            print(" 1. s      -> show version")
            print(" 2. s help -> show this list")


if __name__ == "__main__":
    main()
