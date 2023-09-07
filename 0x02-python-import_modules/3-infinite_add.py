#!/usr/bin/python3
import sys


def main():
    result = 0
    for num in range(len(sys.argv) - 1):
        result += int(sys.argv[num + 1])
    print("{}".format(result))


if __name__ == "__main__":
    main()
